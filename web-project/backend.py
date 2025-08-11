#activate venv
#. .venv/bin/activate
import API_weather as API_weather
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/" ,methods = ['POST', 'GET'])
def form_page():
    if request.method == 'POST':

        country = request.form['country']
        city = request.form['city']

        #in case the form was made redirct it to report
        #redirect well...redirects to the url
        #url_for create the url for the specified name (using the route)
        return redirect(url_for('report', country = country, city = city))
    else: 
        return render_template('home.html')


@app.route('/report')
def report():
    country = request.args.get('country', None)
    city = request.args.get('city', None)
    weather_list = API_weather.get_weather(city, country)

    #to show in the output country if city is none
    if city == '':
        place = country
    else:
        place = city

    #if there is an error (list = False) return to the from page   
    if weather_list:
        return render_template('report.html', weather_list = weather_list, place = place) 
    else:
        return render_template('home.html', error_message = "Invalid input")

if __name__ == '__main__':
    app.run()


 
