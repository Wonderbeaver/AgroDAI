from flask import Flask, render_template, redirect, request, session
from scripts.information import get_data
from scripts.unpickling import model_prediction
from scripts.disaster import get_disaster_pred
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

@app.route('/')
def index():
    session.clear()
    session['drought'] = 'No drought risks identified'
    session['flood'] = 'No flood risks identified'
    return render_template('main.html')

@app.route('/home')
def home():
    print(session)
    return render_template('main.html', session=session)


@app.route('/get_info', methods=['POST'])
def get_info():
    lat = request.form['lat']
    lng = request.form['lon']
    data = get_data(lat, lng)
    session['data'] = data
    df = pd.DataFrame(data, columns=['Date', 'Max temperature', 'Min temperature', 'Precipitation', 'Wind speed'])
    df.to_excel('static/data/data.xlsx', index=False)
    return redirect('/home#table')

@app.route('/predict', methods=['POST'])
def predict():
    soil_mos = float(request.form['soil_mos'])
    precip = float(request.form['precip'])
    temp = float(request.form['temp'])
    soil_type = request.form['soil_type']
    crop_type = request.form['crop_type']
    air_hum = float(request.form['air_hum'])
    wind_speed = float(request.form['wind_speed'])

    res = model_prediction(soil_mos, precip, temp, soil_type, crop_type, air_hum, wind_speed)

    session['res'] = round(res[0], 3)
    return redirect('/home#prediction')

@app.route('/get_disaster', methods=['POST'])
def get_disaster():
    lat = request.form['lat']
    lng = request.form['lon']
    drought_dis, flood_dis = get_disaster_pred(lat, lng)
    print(drought_dis, flood_dis)
    session['drought'] = drought_dis
    session['flood'] = flood_dis
    return redirect('/home#disaster')


app.run(host="0.0.0.0")

