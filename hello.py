
import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt 
import graphviz as graphviz


st.title ("SIMPLY IS POWER")
st.header("Thien Phat")

st.image("python.jpg")
st.video("flex.mp4")

st.balloons()
st.sidebar.title("SIMPLY IS POWER")
st.sidebar.button("Click")
st.sidebar.radio("chọn giới tính của bạn",["Nam","Nữ"])

container=st.container()
container.write("SIMPLY IS POWER")
st.write("ENJOY THE MOMENT")


rand=np.random.normal(1,2,size=20)

fig,ax=plt.subplots()

ax.hist(rand,bins=15)
st.pyplot(fig)

df = pd.DataFrame(
    np.random.randn(10,2),
    columns=['x','y']
)
st.line_chart(df)

st.bar_chart(df)

st.area_chart(df)

df1=pd.DataFrame(
    np.random.randn(500,3),
    columns=['x','y','z']
)
c=alt.Chart(df1).mark_circle().encode(
    x='x',y='y',size='z',color='z',tooltip=['x','y','z']
)
st.altair_chart(c,use_container_width=True)

df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [10.77, 106.57],columns=['lat', 'lon'])
st.map(df)