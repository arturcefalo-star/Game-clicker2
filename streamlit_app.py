import streamlit as st

st.title("")

if st.session.state_pontos not in st.session.state:
  st.session.state_pontos = 67

st.write("pontos")
