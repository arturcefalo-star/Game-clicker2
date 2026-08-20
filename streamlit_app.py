import streamlit as st

st.title("")

if "pontos" not in st.session.state:
  st.session.state_pontos = 67

st.write("pontos")
