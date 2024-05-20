Creating a virtual environment
python -m venv env
env/Scripts/activate

Install reuirements
pip install -r requirements.txt

1 project but multiple apps for different functionalities

JWT - permissions to access backend from frontend
access token - requests
refresh token - to get new access token when access token expires
when refresh token expires, user needs to sign back in
