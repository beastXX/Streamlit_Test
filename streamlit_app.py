import streamlit as st

st.write("""
# My First App
Hello *world*
""")

x = st.slider("x")
st.write(x, 'squared is', x * x)

label = st.selectbox('Filter to:', ['A', 'B',])
st.write(label)
