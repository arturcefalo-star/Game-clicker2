import streamlit as st

st.title("")

if "pontos" not in st.session_state:
  st.session_state.pontos = 1
  
st.write(pontos)
