from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def hello_world():
    message = "Hello !!! everyone this my first web python program using docker."
    return message


# Access http://localhost:5000/author
@app.route('/author')
def author():
    message = "Author is Sourav Singh."
    return message

if __name__ == '__main__':
    # Run the application on localhost, port 5000
    app.run(debug=True)
