import pickle
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# I want to make a warning, that its just a prototype. 
# I didnt have enough time to make a complete machine learning model, 
# so i made just a simple one to show off the possibilities and function
def model_prediction(sm, prep, temp, st, ct, ah, ws):
    with open('model_06-10-24.pickle', 'rb') as f:
        unpickled_data = pickle.load(f)
        
    ct_carrot = 0
    ct_corn = 0
    ct_potato = 0
    ct_rice = 0
    ct_soybean = 0
    ct_wheat = 0
    
    if ct == 'Carrot':
        ct_carrot = 1
    elif ct == 'Corn':
        ct_corn = 1
    elif ct == 'Potato':
        ct_potato = 1
    elif ct == 'Rice':
        ct_rice = 1
    elif ct == 'Soybean':
        ct_soybean = 1
    elif ct == 'Wheat':
        ct_wheat = 1


    st_clay = 0
    st_loam = 0
    st_peat = 0
    st_sand = 0
    st_silt = 0

    if st == 'Clay':
        st_clay = 1
    elif st == 'Loam':
        st_loam = 1
    elif st == 'Peat':
        st_peat = 1
    elif st == 'Sand':
        st_sand = 1
    elif st == 'Silt':
        st_silt = 1


    X = pd.DataFrame({
        'Soil Moisture':sm,
        'Precipitation':prep,
        'Temperature':temp,
        'Air Humidity':ah,
        'Wind Speed':ws,
        
        'Soil Type_Clay':st_clay,
        'Soil Type_Loam':st_loam,
        'Soil Type_Peat':st_peat,
        'Soil Type_Sand':st_sand,
        'Soil Type_Silt':st_silt,

        'Crop Type_Carrot':ct_carrot,
        'Crop Type_Corn':ct_corn,
        'Crop Type_Potato':ct_potato,
        'Crop Type_Rice':ct_rice,
        'Crop Type_Soybean':ct_soybean,
        'Crop Type_Wheat':ct_wheat,

        }
        ,index=[0])
        
    res = unpickled_data.predict(X)

    return res