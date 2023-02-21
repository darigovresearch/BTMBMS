# app.py is code that runs a flask web app for the user interface

from flask import Flask, render_template, request, send_file
import pandas as pd
import datetime

import btmbms

app = Flask(__name__)
# line to prevent cache from not updating static files
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# running file checks onload
try:
    df = pd.read_csv("..//Data//Status.csv")
except Exception as e:
    print("No files found, initiallising folders & files")
    btmbms.initialise()


@app.route('/', methods=['GET'])
def home():

    return render_template('index.html')


@app.route('/batteries', methods=['POST', 'GET'])
def batteries():

    df = pd.read_csv("..//Data//Batteries.csv")
    df = df.sort_values('Label')
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
        acquisition_year = form_data["Acquisition-year"]
        acquisition_month = form_data["Acquisition-month"]
        chemistry = form_data["Chemistry"]
        cycle_schedule = form_data["Cycle-schedule"]
        notes_name = form_data["Notes"]

        # adding value
        df.loc[len(df.index)] = [battery_name, acquisition_year, acquisition_month, chemistry, cycle_schedule, notes_name]
        # saving to csv
        df.to_csv("..//Data//Batteries.csv", sep=",", index=False)

        # rendering new result
        df = df.sort_values('Label')
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
        submit_type = request.args.get("submit")
        print(submit_type)

        if submit_type == "add":
            form_data = request.form
            print(form_data)
            battery_name = form_data["Battery-name"]
            location_name = form_data["Location"]
            start_name = form_data["Start"]
            end_name = form_data["End"]
            notes_name = form_data["Notes"]

            # adding value
            df.loc[len(df.index)] = [battery_name, location_name, start_name, end_name, notes_name]
            # saving to csv
            df.to_csv("..//Data//Locations.csv", sep=",", index=False)

            # rendering new result
            parsed_data = df.to_html()
            return render_template(
                                    'locations.html',
                                    data=parsed_data
                                  )

        elif submit_type == "edit":
            form_data = request.form
            print(form_data)
            row = int(form_data["Row-number"])
            battery_name = form_data["Battery-name"]
            location_name = form_data["Location"]
            start_name = form_data["Start"]
            end_name = form_data["End"]
            notes_name = form_data["Notes"]

            # adding value
            df.loc[row] = [battery_name, location_name, start_name, end_name, notes_name]
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


@app.route('/settings', methods=['POST', 'GET'])
def settings():

    if request.method == 'GET':
        return render_template('settings.html')
    elif request.method == 'POST':
        print("form submitted")
        submit_type = request.args.get("submit")
        print(submit_type)

        if submit_type == "import":
            print("Import requested")
            form_data = request.form
            print(form_data)
            file = request.files['import-file']        
            status = pd.read_excel(file, sheet_name="Status")
            print(status)
            status.to_csv("..//Data//Status.csv", index=False)
            locations = pd.read_excel(file, sheet_name="Locations")
            print(locations)
            locations.to_csv("..//Data//Locations.csv", index=False)
            batteries = pd.read_excel(file, sheet_name="Batteries")
            print(batteries)
            batteries.to_csv("..//Data//Batteries.csv", index=False)
            return render_template('settings.html')

        elif submit_type == "export":
            print("Export requested")

            # getting data
            status = pd.read_csv("..//Data//Status.csv")
            locations = pd.read_csv("..//Data//Locations.csv")
            batteries = pd.read_csv("..//Data//Batteries.csv")

            # generating export in ods format
            today = datetime.datetime.now()
            today_string = "-".join([str(today.year), str(today.month), str(today.day)])
            filename = "..//Data//Export " + today_string + ".ods"
            with pd.ExcelWriter(filename) as export:
                status.to_excel(export, sheet_name="Status", index=False)
                locations.to_excel(export, sheet_name="Locations", index=False)
                batteries.to_excel(export, sheet_name="Batteries", index=False)

            return send_file(export, as_attachment=True)

        elif submit_type == "delete":
            print("Deleting data")
            status = pd.read_csv("..//Data//Status.csv")
            status = status.head(0)
            status.to_csv("..//Data//Status.csv", index=False)
            locations = pd.read_csv("..//Data//Locations.csv")
            locations = locations.head(0)
            locations.to_csv("..//Data//Locations.csv", index=False)
            batteries = pd.read_csv("..//Data//Batteries.csv")
            batteries = batteries.head(0)
            batteries.to_csv("..//Data//Batteries.csv", index=False)
            return render_template('settings.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8766", debug=True)
