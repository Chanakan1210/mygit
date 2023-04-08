from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

#st.header("Chanakan")
#st.image("./pic/NPRU.png")
#st.image("./pic/chana.jpg")

col1, col2, col3  = st.columns(3)

with col1:
   st.header(" ")
   st.image("./pic/npru.jpg")

with col2:
   st.header(" ")
   st.image("./pic/chana.jpg")
with col2:
   st.header(" ")
   st.image("./pic/Setosa.jpg")


html_8 = """
<div style="background-color:#F2B2E4;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูลดอกไม้</h5></center>
</div>
"""

st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")


dt = pd.read_csv("./data/iris.csv")

st.write(dt.head(10))

dt1 = dt['petal.length'].sum()
dt2 = dt['petal.width'].sum()
dt3 = dt['sepal.length'].sum()
dt4 = dt['sepal.width'].sum()

dx = [dt1, dt2, dt3, dt4]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4"])
if st.button("แสดงการจินตทัศน์ข้อมูล"):
    #st.write(dt.head(10))
    st.bar_chart(dx2)
    st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

html_8 = """
<div style="background-color:#6BD5DA;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ทำนายข้อมูล</h5></center>
</div>
"""
st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

pt_len=st.slider("กรุณาเลือกข้อมูล petal.length")
pt_wd=st.slider("กรุณาเลือกข้อมูล petal.width")
sp_len=st.number_input("กรุณาเลือกข้อมูล sepal.length")
sp_wd=st.number_input("กรุณาเลือกข้อมูล sepal.width")

if st.button("ทำนายผล"):
       
   X = dt.drop('variety', axis=1)
   y = dt.variety
   Knn_model = KNeighborsClassifier(n_neighbors=3)
   Knn_model.fit(X, y)   

   x_input = np.array([[pt_len, pt_wd, sp_len, sp_wd]])
   st.write(Knn_model.predict(x_input))
   
   out=Knn_model.predict(x_input)

   if out[0] == 'Setosa':
    st.image("./pic/Setosa.jpg")
   else:       
    st.writ('xxx')    
   #st.button("ไม่แสดงข้อมูล")
   if out[1] == 'Virginica':
        st.image("./pic/Virginica.jpg")
   else:       
    st.writ('xxx')    
   if out[2] == 'Versicolor':
        st.image("./pic/Versicolor.jpg")
   else:       
    st.writ('xxx')  

else:
   st.write("ไม่แสดงข้อมูล")

#st.image("./pic/chanakan.jpg")