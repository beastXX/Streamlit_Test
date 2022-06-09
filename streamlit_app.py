import streamlit as st
import os

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
