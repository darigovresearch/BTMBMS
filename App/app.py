# app.py is code that runs a flask web app for the user interface

from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)
# line to prevent cache from not updating static files
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/', methods=['GET'])
def home():

    df = pd.read_csv("..//Data//Status_example.csv")
    parsed_data = df.to_html()

    if request.method == 'GET':
        return render_template(
                                'index.html',
                                data=parsed_data
                              )
    else:

        return render_template('index.html')


@app.route('/batteries', methods=['GET'])
def batteries():

    df = pd.read_csv("..//Data//Batteries.csv")
    parsed_data = df.to_html()

    if request.method == 'GET':
        return render_template(
                                'batteries.html',
                                data=parsed_data
                              )
    else:

        return render_template('batteries.html')


@app.route('/locations', methods=['GET'])
def locations():

    df = pd.read_csv("..//Data//Locations.csv")
    parsed_data = df.to_html()

    if request.method == 'GET':
        return render_template(
                                'locations.html',
                                data=parsed_data
                              )
    else:

        return render_template('locations.html')


@app.route('/status', methods=['GET'])
def status():

    df = pd.read_csv("..//Data//Status.csv")
    parsed_data = df.to_html()

    if request.method == 'GET':
        return render_template(
                                'status.html',
                                data=parsed_data
                              )
    else:

        return render_template('status.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8766", debug=True)