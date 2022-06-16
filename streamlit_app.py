import streamlit as st, datetime, time
import os, random, pandas as pd, numpy as np

cp = os.path.dirname(os.path.abspath(__file__))

st.write("""
# My First App
Hello *world*
""")

st.write(cp)
x = st.slider("x", 0.00, 5.00)
st.write("当前电压：{:.2f}V".format(x))

data_1 = {'Pin1': x}
st.table(data_1)

label = st.selectbox('Filter to:', ['A', 'B',])
st.write(label)

chart_data = pd.DataFrame(
     np.random.randn(5, 3),
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


# # 添加占位符
# placeholder = st.empty()
# # 创建进度条
# bar = st.progress(0)

# for i in range(100):
#     time.sleep(0.01)
#     # 不断更新占位符的内容
#     placeholder.text(f"Iteration {i+1}")
#     # 不断更新进度条
#     bar.progress(i + 1)

# # 状态
# st.success("Finished")


# pb = st.progress(0)
# status_txt = st.empty()
# chart = st.line_chart(np.random.randn(10, 2))

# for i in range(100):
#     pb.progress(i + 1)
#     new_rows = np.random.randn(10, 2)
#     status_txt.text(
#         "The latest number is: %s" % new_rows[-1, 1]
#     )
#     chart.add_rows(new_rows)
#     time.sleep(0.01)

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")
