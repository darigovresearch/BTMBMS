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


@app.route('/batteries', methods=['POST', 'GET'])
def batteries():

    df = pd.read_csv("..//Data//Batteries.csv")
    parsed_data = df.to_html()

    if request.method == 'GET':
        return render_template(
                                'batteries.html',
                                data=parsed_data
                              )
    elif request.method == 'POST':
        form_data = request.form
        print(form_data)
        battery_name = form_data["Battery-name"]

        # adding value
        df.loc[len(df.index)] = [battery_name]
        # saving to csv
        df.to_csv("..//Data//Batteries.csv", sep=",", index=False)

        # rendering new result
        parsed_data = df.to_html()
        return render_template(
                                'batteries.html',
                                data=parsed_data
                              )
    else:

        return render_template('batteries.html')


@app.route('/locations', methods=['POST', 'GET'])
def locations():

    df = pd.read_csv("..//Data//Locations.csv")
    parsed_data = df.to_html()

    if request.method == 'GET':
        return render_template(
                                'locations.html',
                                data=parsed_data
                              )
    elif request.method == 'POST':
        form_data = request.form
        print(form_data)
        battery_name = form_data["Battery-name"]
        location_name = form_data["Location"]
        start_name = form_data["Start"]
        end_name = form_data["End"]

        # adding value
        df.loc[len(df.index)] = [battery_name, location_name, start_name, end_name]
        # saving to csv
        df.to_csv("..//Data//Locations.csv", sep=",", index=False)

        # rendering new result
        parsed_data = df.to_html()
        return render_template(
                                'locations.html',
                                data=parsed_data
                              )
    else:

        return render_template('locations.html')


@app.route('/status', methods=['POST', 'GET'])
def status():

    df = pd.read_csv("..//Data//Status.csv")
    parsed_data = df.to_html()

    # calculating latest data
    latest_df = df.sort_values('Date').groupby('Battery').tail(1)
    latest_df.reset_index(drop=True, inplace=True)
    latest_data = latest_df.to_html()

    if request.method == 'GET':
        return render_template(
                                'status.html',
                                data=parsed_data,
                                latest_data=latest_data
                              )
    elif request.method == 'POST':
        form_data = request.form
        print(form_data)
        battery_name = form_data["Battery-name"]
        soc_name = form_data["SOC"]
        date_name = form_data["Date"]
        time_name = form_data["Time"]
        notes_name = form_data["Notes"]

        # adding value
        df.loc[len(df.index)] = [battery_name, soc_name, date_name, time_name, notes_name]
        # saving to csv
        df.to_csv("..//Data//Status.csv", sep=",", index=False)

        # rendering new result
        parsed_data = df.to_html()
        latest_df = df.sort_values('Date').groupby('Battery').tail(1)
        latest_df.reset_index(drop=True, inplace=True)
        latest_data = latest_df.to_html()

        return render_template(
                                'status.html',
                                data=parsed_data,
                                latest_data=latest_data
                              )
    else:

        return render_template('status.html')


@app.route('/settings', methods=['GET'])
def settings():

    return render_template('settings.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8766", debug=True)
