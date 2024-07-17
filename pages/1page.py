
import streamlit as st
import pandas as pd
import numpy as np
import os

cwd = os.getcwd()
"""
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write("Here's our first attempt at using data to create a table:")

df
st.write(df)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

y = st.button('+1')  # 👈 this is a widget
if y:
    a = x + 1
    st.write(a)
else:
    a = x
    st.write(a)

z = st.selectbox('z', options=["Squared", "Times 10"])  # 👈 this is a widget
if z == "Squared":
    st.write(a * a)
else:
    st.write(a * 10)
"""