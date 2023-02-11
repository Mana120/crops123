import streamlit as st
import pandas as pd
l=[]
COLUMNS_SELECTED = None
Data = None
r = pd.DataFrame()
Data_df = pd.DataFrame()


def filter_df(columns_name,df):    
    df = df[columns_name]
    return df

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    COLUMNS_SELECTED = st.multiselect('Select options', df.columns.to_list())
      
if COLUMNS_SELECTED:
      Data = filter_df(COLUMNS_SELECTED, df)
      Data_df = Data_df.append(Data)
      
button_sent_1 = st.button("Button 1")

if button_sent_1:
    st.write("Data_df shape",Data_df.shape)
    r = r.append(Data_df)
    st.write("AP_data shape",r.shape)
    

button_sent_2 = st.button("Button 2")

if button_sent_2:
    st.write("Data_df shape",Data_df.shape)
    st.write("AP_Data shape",r.shape)