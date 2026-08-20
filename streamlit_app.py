import streamlit as st

st.title("")

if not st.session.state_pontos:
  st.session.state_pontos = 67

st.write("pontos")
