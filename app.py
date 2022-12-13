from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "<h1>Hello World :) </h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<temperature>')
def convert_celsius_to_fahrenheit(temperature=""):
    return f"{float(temperature) * 9 / 5 + 32}"


if __name__ == '__main__':
    app.run()
