"""
# My first app
Here's our first attempt at using data to create a table:
"""
import streamlit as st
from streamlit_extras.app_logo import add_logo 



st.title("XIPE")
st.subheader("The cross impact performance emissions model")

#logos
#st.sidebar.image('images\cnl-logo.png',use_column_width=True)
#st.sidebar.image('images\gemini_logo.png', use_column_width=True)

#input
col1, col2 = st.columns(2)

with col1:
   st.header("Inputs")
   z = st.selectbox('Select Cenex', options=["Cenex", "Cenex NL"])  # 👈 this is a widget


with col2:
   st.header("Outputs")
   if z == "Cenex":
      st.map(latitude="52.38424488638437", longitude="4.902959069675009", zoom=11, size=40)
   elif z == "Cenex NL":
      st.map(latitude="52.75835018938319", longitude="-1.2466710996992605", zoom=11, size=8)