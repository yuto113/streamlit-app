import streamlit as st
from datetime import datetime
import requests
from deep_translator import GoogleTranslator

# 日付を取得
today = datetime.today().strftime('%Y-%m-%d')

# 天気の説明を簡略化する関数
def simplify_weather_description(description):
    if 'clear' in description:
        return '晴れ'
    elif 'cloud' in description:
        return 'くもり'
    elif 'rain' in description or 'drizzle' in description:
        return '雨'
    else:
        return 'その他'

# 天気情報を取得する関数
def get_weather(city):
    translator = GoogleTranslator(source='auto', target='en')
    city_en = translator.translate(city)
    api_key = '4ed8711daa86837bebae208dfc828d9e'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + 'q=' + city_en + '&appid=' + api_key + '&units=metric'
    response = requests.get(complete_url)
    data = response.json()
    if data['cod'] != '404':
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        description = weather['description']
        
        # 天気の説明を簡略化して日本語に翻訳
        simplified_description = simplify_weather_description(description)
        description_ja = GoogleTranslator(source='en', target='ja').translate(simplified_description)
        return temperature, description_ja
    else:
        return None, None

# Streamlitアプリの設定
st.title('日付と天気を表示するアプリ')

# 日付を表示
st.write(f'今日の日付: {today}')

# 天気情報を表示
city = st.text_input('都市名を入力してください', '名古屋')
if city:
    temperature, description = get_weather(city)
    if temperature is not None:
        st.write(f'{city}の天気: {description}, 気温: {temperature}°C')
    else:
        st.write('天気情報を取得できませんでした。')