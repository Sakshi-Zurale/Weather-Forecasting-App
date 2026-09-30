import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

st.set_page_config(page_title="Weather App" , page_icon="🌤️")

st.title("Weather Buddy🌤️")

st.write("Enter city name and click on button to fetch weather data")

city = st.text_input("Enter a city name")

if(st.button("Fetch weather data")):
    API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(API_URL)

    if(response.status_code==200):
        st.success('Weather data feteched successfully')

        data = response.json()
        #extrating temperature
        temperature = data['main']['temp']
        # extrat humidity
        humidity = data['main']['humidity']
        # extract wind and speeed
        wind_speed = data['wind']['speed']
        # current weather
        condition = data['weather'][0]['main']
        # extract city name
        city_name = data['name']
        # extract country
        country = data['sys']['country']

        # Display the data
        st.header(f'{city_name},{country}')
        col1,col2 = st.columns(2)
        col3,col4 = st.columns(2)

        col1.metric('Temperature',f'{temperature}°C🌡️')
        col2.metric('Humidity',f'{humidity}%💦')
        col3.metric('Wind_Speed',f'{wind_speed}m/s🌪️')
        col4.metric('Weather Condition',f'{condition}☁️')
    else:
        st.error('Invalid City Name')


