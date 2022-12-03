import streamlit as st
import pandas as pd
import plost
from googleapiclient.discovery import build
from google.oauth2 import service_account


st.set_page_config(layout='wide', initial_sidebar_state='expanded')

from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

st.sidebar.markdown('''
---
Created with ❤️ by [Data Professor](https://youtube.com/dataprofessor/).
''')


# Row A
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# Row B
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1tm1UXEUrQtD8QzYcShgmGuz0s9WSb8kJrocMsmm0YRU'

service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
sheet = service.spreadsheets()
df = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sheet1!A1:N46").execute()
result2 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sheet2!A1:J73").execute()
values = df.get('values',[])

# values2 = result2.get('values',[])


# Inject CSS with Markdown
st.markdown("### Details Table")
st.dataframe(values)




# c1, c2 = st.columns((7,3))
# with c1:
#     st.markdown('### Heatmap')
#     plost.time_hist(
#     data=values2,
#     date='From Datedate',
#     x_unit='week',
#     y_unit='day',
#     color=time_hist_color,
#     aggregate='median',
#     legend=None,
#     height=345,
#     use_container_width=True)
# with c2:
#     st.markdown('### Donut chart')
#     plost.donut_chart(
#         data=values,
#         theta=donut_theta,
#         color='Lead Stage',
#         legend='bottom', 
#         use_container_width=True)

# Row C
st.markdown('### Line chart')
st.line_chart(values, x='Lead_Date', y='Sent')
