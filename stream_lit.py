# https://medium.com/codex/streamlit-fastapi-%EF%B8%8F-the-ingredients-you-need-for-your-next-data-science-recipe-ffbeb5f76a92
import streamlit as st
import json
import requests

st.title("Basic Calculator App")

# taking user input
option = st.selectbox('What operation could you like to perform?',
                      ('add', 'sub', 'multiply', 'division'))
st.write("")
st.write("select the numbers from slider below")
x = st.slider("X", 0, 10000, 20)
y = st.slider("Y", 0, 13000, 10)

# converting the inputs into a json format
inputs = {"operation": option, "x": x, "y": y}

# when the user clicks on button it will fetch the API
if st.button("Calculate"):
    res = requests.post(
        url="http://127.0.0.1:8000/calculate",
        data = json.dumps(inputs)
    )

    st.subheader(f"Response form API = {res.text}")

"""
在命令行输入：
# 启动后端
uvicorn fast_api:app --reload
# 启动前端
streamlit run stream_lit.py
"""