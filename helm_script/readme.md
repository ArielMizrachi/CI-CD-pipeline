install kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.10.4/deploy/static/provider/cloud/deploy.yaml

steps i took to install helm
1. installing helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bash_profile
source ~/.bash_profile

2. kubectl
KUBECTL_VERSION=$(curl -s https://cdn.dl.k8s.io/release/stable.txt)
curl -LO https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client

3. edit the RABC to let the instance in
kubectl -n kube-system get configmap aws-auth -o yaml > aws-auth.yaml
code aws-auth.yaml #open for edit and add your instance
mapRoles: |
  - rolearn: arn:aws:iam::543157868473:role/example-eks-node-group-20250616112323815100000002
    username: system:node:{{EC2PrivateDNSName}}
    groups:
      - system:bootstrappers
      - system:nodes
  - rolearn: arn:aws:iam::543157868473:role/ssm-role-agent-instance
    username: ec2-user
    groups:
      - system:masters
