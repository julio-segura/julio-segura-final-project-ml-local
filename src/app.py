import streamlit as st
from pickle import load

with open(r"../models/rwanda-co2-emissions-xgboost.sav", 'rb') as f:
    model = load(f)

st.title ('CO2 Emissions Prediction in Rwanda')

st.header('Overview')

multi = '''The ability to accurately monitor carbon emissions is a critical step in the fight against climate change.  
Precise carbon readings allow researchers and governments to understand the sources and patterns of carbon mass output.  


This project uses the data provided in the **Predict CO2 Emissions in Rwanda** challenge from Kaggle.  
It's main objective is to create a machine learning model using open-source CO2 emissions data from Sentinel-5P satellite observations to predict future carbon emissions.'''

st.markdown(multi)

st.header('Calculate the Prediction')

latitude = st.slider('Latitude', min_value = -2.84, max_value = -1.04, step = 0.01 )

year = st.slider('Year', min_value = 2019, max_value = 2022, step = 1 )
# year = st.selectbox('Year', '2019', '2020', '2021', '2022')
# st.write('Emmission': year)

SulphurDioxide_sensor_azimuth_angle  = st.slider('Sulphur Dioxide Sensor Azimuth Angle' , min_value = 0, max_value = 360, step = 1)

SulphurDioxide_solar_azimuth_angle  = st.slider('Sulphur Dioxide Solar Azimuth Angle' , min_value = 0, max_value = 360, step = 1)

CarbonMonoxide_CO_column_number_density  = st.slider('Carbon Monoxide Column number density' , min_value = 0.0, max_value = float(1), step = 0.001)

CarbonMonoxide_solar_azimuth_angle  = st.slider('Carbon Monoxide Solar azimuth Angle' , min_value = 0, max_value = 360, step = 1)

NitrogenDioxide_NO2_column_number_density  = st.slider('Nitrogen Dioxide Column number Density' , min_value = 0.0, max_value = float(1), step = 0.001)

NitrogenDioxide_stratospheric_NO2_column_number_density  = st.slider('Nitrogen Dioxide stratospheric NO2 Column number density' , min_value = 0.0, max_value = float(1), step = 0.001)

NitrogenDioxide_NO2_slant_column_number_density  = st.slider('Nitrogen Dioxide Slant Column number density' , min_value = 0.0, max_value = float(1), step = 0.001)

NitrogenDioxide_absorbing_aerosol_index  = st.slider('Nitrogen Dioxide Absorbing Aerosol Index' , min_value = 0.0, max_value = 100.0, step = 1.0)

NitrogenDioxide_sensor_azimuth_angle  = st.slider('Nitrogen Dioxide Sensor Azimuth Angle' , min_value = 0, max_value = 360, step = 1)

NitrogenDioxide_solar_azimuth_angle  = st.slider('Nitrogen Dioxide Solar Azimuth Angle' , min_value = 0, max_value = 360, step = 1)

Formaldehyde_tropospheric_HCHO_column_number_density  = st.slider('Formaldehyde Tropospheric  column number density' , min_value = 0.0, max_value = float(1), step = 0.001)

Formaldehyde_tropospheric_HCHO_column_number_density_amf  = st.slider('Formaldehyde Tropospheric  Column number density  amf' , min_value = 0.0, max_value = float(1), step = 0.001)

Formaldehyde_solar_azimuth_angle  = st.slider('Formaldehyde Solar Azimuth Angle' , min_value = 0, max_value = 360, step = 1)

Formaldehyde_sensor_azimuth_angle  = st.slider('Formaldehyde Sensor Azimuth Angle' , min_value = 0, max_value = 360, step = 1)

UvAerosolIndex_absorbing_aerosol_index  = st.slider('UvAerosol Index Absorbing Aerosol Index' , min_value = 0.0, max_value = 100.0, step = 1.0)

Ozone_O3_effective_temperature  = st.slider('Ozone Effective Temperature' , min_value = 0.0, max_value = 100.0, step = 1.0)

Cloud_surface_albedo  = st.slider('Cloud Surface Albedo' , min_value = 0.0, max_value = 100.0, step = 1.0)

km_to_worst = st.slider('Distance to the worst point of CO2 emision (in Km)', min_value = 0.0, max_value = 10000.0, step = 1.0 )


if st.button('Predict'):
    data_a_predecir = [[
        latitude,
        year,
        SulphurDioxide_sensor_azimuth_angle,
        SulphurDioxide_solar_azimuth_angle,
        CarbonMonoxide_CO_column_number_density,	
        CarbonMonoxide_solar_azimuth_angle,	
        NitrogenDioxide_NO2_column_number_density,	
        NitrogenDioxide_stratospheric_NO2_column_number_density,	
        NitrogenDioxide_NO2_slant_column_number_density,
        NitrogenDioxide_absorbing_aerosol_index,	
        NitrogenDioxide_sensor_azimuth_angle,	
        NitrogenDioxide_solar_azimuth_angle,	
        Formaldehyde_tropospheric_HCHO_column_number_density,	
        Formaldehyde_tropospheric_HCHO_column_number_density_amf,	
        Formaldehyde_solar_azimuth_angle,	
        Formaldehyde_sensor_azimuth_angle,	
        UvAerosolIndex_absorbing_aerosol_index,	
        Ozone_O3_effective_temperature,	
        Cloud_surface_albedo,
        km_to_worst
        ]]
    prediction = model.predict(data_a_predecir)
    st.write('Emission', prediction)
