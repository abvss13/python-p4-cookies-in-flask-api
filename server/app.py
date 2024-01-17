# Import necessary modules from Flask
from flask import Flask, request, session, make_response, jsonify

# Import jsonify explicitly from flask.json
from flask.json import jsonify

# Create a Flask app instance
app = Flask(__name__)

# Disable JSON compact formatting in the app
app.json.compact = False

# Set a secret key for session security
app.secret_key = b'?w\x85Z\x08Q\xbdO\xb8\xa9\xb65Kj\xa9_'

# Define a route for handling session information
@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):

    # Initialize or retrieve session variables
    session["hello"] = session.get("hello") or "World"
    session["goodnight"] = session.get("goodnight") or "Moon"

    # Create a JSON response with session details and cookies
    response = make_response(jsonify({
        'session': {
            'session_key': key,
            'session_value': session[key],
            'session_accessed': session.accessed,
        },
        'cookies': [{cookie: request.cookies[cookie]}
                    for cookie in request.cookies],
    }), 200)

    # Set a custom cookie named 'mouse'
    response.set_cookie('mouse', 'Cookie')

    return response

# Run the Flask app on port 5555 if the script is executed directly
if __name__ == '__main__':
    app.run(port=5555)
