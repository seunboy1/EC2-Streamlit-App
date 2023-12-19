# EC2-Streamlit-App

This is a simple project that shows how to deploy a GPT-3 app built with Streamlit on an AWS EC2 instance. 
Deployment of a GPT streamlit app on ec2

### Connect to your ec2 instance
ssh -i "testkey.pem" ubuntu@ec2-52-202-251-189.compute-1.amazonaws.com

### Create Virtual Environment
apt install python3.10-venv
python3 -m venv streamlit

### Activate Virtual Environment
source streamlit/bin/activate

### git clone this repo
git clone https://github.com/seunboy1/EC2-Streamlit-App.git

### Install necessary libraries
pip install -r requirements.txt

### Run streamlit app in background
nohup streamlit app.py &


