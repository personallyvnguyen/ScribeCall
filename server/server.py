from flask import Flask, render_template, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


def welcome_message() -> str:
    'Returns a welcome message'
    return f"""
    Welcome to ScribeCall's Python backend.
    Written by Adam, Kevin, Nathan, Van
    {'*'*40}
    The feature is returning a basic api request to /ping.
    Run the vue app in client with "npm run
    serve" and go to localhost:8080/ping.
    If it is successful, the client should display pong.
    If not, then nothing will be displayed.
    """


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == "__main__":
    print(welcome_message())
    app.run(debug=True)
