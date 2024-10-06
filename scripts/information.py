import datetime as dt
import meteomatics.api as api

def get_data(lat, lng):
    # My user data
    username = 'crystal____'
    password = 'SC14Odvk5h'

    # Coordinates and parameters
    coordinates = [(lat, lng)]
    parameters = ['t_max_2m_24h:C', 't_min_2m_24h:C', 'precip_24h:mm', 'wind_speed_10m:ms']
    model = 'mix'

    # Time period: 10 day forecast
    startdate = dt.datetime.now(dt.timezone.utc).replace(minute=0, second=0, microsecond=0)
    enddate = startdate + dt.timedelta(days=9)  # 10 day forecast
    interval = dt.timedelta(days=1)  # Daily interval

    # API call to get data
    try:
        weather_data = api.query_time_series(coordinates, startdate, enddate, interval, parameters, username, password, model=model)
        
        res = []
        for i in range(weather_data.shape[0]):
            row_data = weather_data.iloc[i].values.tolist()
            date = startdate + dt.timedelta(days=i)
            row_data.insert(0, date.strftime('%d.%m.%Y'))
            res.append(row_data)

        return res
    except Exception as e:
        return f"Ошибка при запросе данных: {e}"


# get_data(44.83714, 65.50507)


