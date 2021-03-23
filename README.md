# About
ScribeCall is a voice to text program written in Python.\
Users can connect into voice chat and talk with one another.\
All voice inputs are converted into text for the other person.\

# Setup for client.
Install node.\
Run 'npm install' in /client\
Run 'npm run serve'\

# Setup for python
Cd into /server\
source env/bin/activate\
Run python3.9 server.py\

# Feature 1 - Recording audio and playing it back on the website.
You can go to localhost:8080/, record audio, and play it back.\

# Feature 2 - Ping/pong request.
Server responds to a request to localhost:8080/ping with "pong!".\
If server is offline, nothing will be displayed on the website.\
