import streamlit as st

st.title("")

if "pontos" not in st.session_state:
  st.session_state.pontos = 9999999
if "poder_c" not in st.session_state:
  st.session_state.poder_c = 1
if "poder_b" not in st.session_state:
  st.session_state.poder_b = 1
  
st.write(f"**Pontos:** {st.session_state.pontos:,}")

if st.button("          CLIQUE AQUI         "):
   st.session_state.pontos += st.session_state.poder_c

if st.button("Melhoria = 100 Pts"):
  if st.session_state.pontos >= 100:
     st.session_state.poder_c += st.session_state.poder_b
  
  

