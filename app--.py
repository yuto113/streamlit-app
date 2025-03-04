import streamlit as st
from datetime import datetime
import requests

# 日付を取得
today = datetime.today().strftime('%Y-%m-%d')

# 天気情報を取得する関数
def get_weather(city):
    api_key = '4ed8711daa86837bebae208dfc828d9e'  # OpenWeatherMapのAPIキーをここに入力
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + 'q=' + city + '&appid=' + api_key + '&units=metric'
    response = requests.get(complete_url)
    data = response.json()
    if data['cod'] != '404':
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        description = weather['description']
        return temperature, description
    else:
        return None, None

# Streamlitアプリの設定
st.title('日付と天気を表示するアプリ')

# 日付を表示
st.write(f'今日の日付: {today}')

# 天気情報を表示
city = st.text_input('都市名を入力してください', 'Nagoya')
if city:
    temperature, description = get_weather(city)
    if temperature is not None:
        st.write(f'{city}の天気: {description}, 気温: {temperature}°C')
    else:
        st.write('天気情報を取得できませんでした。')