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

# 单选框
st.sidebar.selectbox("Which would you like", [1, 2, 3], key="1")

# 单选按钮
st.sidebar.radio("Which would you like", [1, 2, 3], key="1")

# 多选框
selector = st.sidebar.multiselect("Which would you like", [1, 2, 3], key="3")
st.write(selector)


# 添加占位符
placeholder = st.empty()
# 创建进度条
bar = st.progress(0)

for i in range(100):
    time.sleep(0.05)
    # 不断更新占位符的内容
    placeholder.text(f"Iteration {i+1}")
    # 不断更新进度条
    bar.progress(i + 1)

# 状态
st.success("Finished")
