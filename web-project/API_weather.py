import requests

def get_weather(city, country):
    """ gets the weather and humidity using 2 API form mateo. the first API
    gives the coordinates (using the country and city names) and the second 
    one use those coordinates to get the weathe and humidity"""

    #in case the city is empty
    if city == '':
        lat_lon_req = requests.get(
            f"https://geocoding-api.open-meteo.com/v1/search?name={country}"
            ).json()
    else:    
        lat_lon_req = requests.get(
            f"https://geocoding-api.open-meteo.com/v1/search?name={city}%2C+{country}"
            ).json()
        
   #check if we got a vaild coordinates     
    try:
        # getting the lan and lon 
        data = lat_lon_req.get('results')[0]
        latitude = data.get('latitude')
        longitude = data.get('longitude')   
         
    except:
        return False
    
    # we get the hourly temerature and humidity each day gives 4 results 
    # (temporal_resolution=hourly_6)
    weather_req = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
                        "&hourly=temperature_2m,relative_humidity_2m&temporal_resolution=hourly_6").json()
    
    temperature = weather_req.get('hourly').get('temperature_2m')
    humidity = weather_req.get('hourly').get('relative_humidity_2m')
    time = weather_req.get('hourly').get('time')
    i = 1
    weather_list =[]

    # here we go over the both dictionaries and establish a list where each 
    # day is a seperate dict we advance the i by 4 to reach the average of 
    # the day and night(each day have 4 entries)
    while i < len(temperature):
        time_ed = time[i]
        weather_list.append({"date": time_ed[8:10] + time_ed[4:7] + '-' + time_ed[0:4],
                             "day_temp" : temperature[i], 
                             "night_temp" : temperature[i+2], 
                             "day_humidity" : humidity[i], 
                             "night_humidity" : humidity[i+2]})
        i += 4  
    return(weather_list)


if __name__ == '__main__':
    get_weather(None, 'canada')