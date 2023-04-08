from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

#st.header("Chanakan")
st.image("./pic/NPRU.png")

html_8 = """
<div style="background-color:#F2B2E4;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูลดอกไม้</h5></center>
</div>
"""

st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")


dt = dt.read_csv("./data/iris.csv")

st.write(dt.head(10))





#st.image("./pic/chanakan.jpg")