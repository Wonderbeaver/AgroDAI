import datetime as dt
import meteomatics.api as api

# I want to warn that this is just a prototype to show off my idea
def check_drought_or_flood(data):
    drought_days = 0
    flood_risk = False
    flood_dis = 'No flood risks identified'
    drought_dis = 'No drought risks identified'
    for index, row in data.iterrows():
        precip = row['precip_24h:mm']
        
        # Drought check
        if precip < 10:
            drought_days += 1
        else:
            drought_days = 0

        # Flood Check
        if precip > 200:  # Let's say this is a flood criterion
            flood_risk = True

        # If the drought continues for 20 days
        if drought_days >= 20:
            drought_start_date = row.name[2] # Drought date
            drought_dis = f"Засуха ожидается с {drought_start_date.strftime('%d-%m-%Y')}"
            break
        
    if flood_risk:
        flood_dis = "Риск наводнения в ближайшие дни!"
    return drought_dis, flood_dis

def get_disaster_pred(lat, lng):
    username = 'crystal____'
    password = 'SC14Odvk5h'

    # Coordinates and parameters
    coordinates = [(lat, lng)]  # Use lat and long from the request
    parameters = ['t_2m:C', 'precip_24h:mm', 'wind_speed_10m:ms']
    model = 'mix'

    # Time range for the data
    startdate = dt.datetime.utcnow().replace(minute=0, second=0, microsecond=0)
    enddate = startdate + dt.timedelta(days=120)
    interval = dt.timedelta(days=1)

    # Call the API
    weather_data = api.query_time_series(coordinates, startdate, enddate, interval, parameters, username, password, model=model)

    # # DEBUG: Print the data to inspect it
    # print(weather_data)

    # Return the results
    drought_dis, flood_dis = check_drought_or_flood(weather_data)
    return drought_dis, flood_dis
