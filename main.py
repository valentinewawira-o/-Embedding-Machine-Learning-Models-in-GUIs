import  streamlit as st
import pandas as pd
import numpy as np
import os
import uuid
 
#generation of unique 
def password_key():
    return str(uuid.uuid4())



st.set_page_config(
    page_title="EMBEDDING ML MODELS IN GUIs", page_icon="🌍", layout="wide")


st.title('EMBEDDING ML MODEL IN GUIs')
st.subheader('Customer Churn Prediciton app')
st.text_input('username')


image_url="https://media.istockphoto.com/id/1473149698/photo/business-finance-data-analytics-graph-advisor-using-kpi-dashboard-on-virtual-screen-financial.jpg?s=612x612&w=0&k=20&c=-IjSeic-dsswhjDbsV9yQHDHIVOzAwrBR2pSvQT9rmQ="
st.image(image_url,caption="DATA MISSION", use_column_width=True)









