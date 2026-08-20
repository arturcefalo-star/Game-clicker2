import streamlit as st

st.title("")

if "pontos" not in st.session_state:
  st.session_state.pontos = 1
if "poder_c" not in st.session_state:
  st.session_state.poder_c = 1
  
st.write(f"**Pontos:** {st.session_state.pontos:,}")

if st.button("test"):
   st.session_state_pontos += st.session_state_poder_c
  

