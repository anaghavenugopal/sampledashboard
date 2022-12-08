from io import StringIO
import pandas as pd
import streamlit as st
from plotly.tools import FigureFactory as ff
import plotly.graph_objects as go

df_uploaded = st.sidebar.file_uploader('Choose txt file:')

@st.cache(hash_funcs={StringIO: StringIO.getvalue}, suppress_st_warning=True)
def load_data(file_uploaded):
    st.write("File Upload Successful") # <--- this should be printed on the app each time this function is run
    return pd.read_xml(file_uploaded)

if df_uploaded:
    df = load_data(df_uploaded)
    cols = list(df.columns)
    cols.remove('time')
    select_cols = st.selectbox('Choose column for analysis', cols)
    chart_button = st.button('Generate Chart for Column', on_click=None)

    if chart_button == True:
        
        # fig = ff.create_distplot(
        #         df[[select_cols]].to_numpy().reshape((1,df.shape[0])), [select_cols], bin_size=[.1, .25, .5])

        fig = go.Figure([go.Scatter(x=df['time'], y=df[select_cols])])

        # Plot!
        st.plotly_chart(fig, use_container_width=True)
