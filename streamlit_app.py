import streamlit as st, datetime
import os, random, pandas as pd, numpy as np

cp = os.path.dirname(os.path.abspath(__file__))

st.write("""
# My First App
Hello *world*
""")

st.write(cp)

x = st.slider("x")
st.write(x, 'squared is', x * x)

label = st.selectbox('Filter to:', ['A', 'B',])
st.write(label)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.write(datetime.datetime.now())

d = st.date_input(
     "Nowday",
     datetime.datetime.now())
st.write('Nowday is:', d)
