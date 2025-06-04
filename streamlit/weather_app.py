import streamlit as st 
import psycopg 
import pandas as pd


def get_weather_data():
    dbconn = st.secrets["DBCONN"]
    conn = psycopg.connect(dbconn)
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM weather_data;")
    df = pd.DataFrame(cur.fetchall(), columns=["date", "city", "temp", "feels", "description"])
    
    cur.close()
    conn.close()
    
    return df
    
data = get_weather_data()
print(data)

city = st.selectbox("Select city", options=["Berlin", "Sydney", "Tokyo"])
st.write(data)