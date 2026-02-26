import streamlit as st
from PIL import Image

st.title("israel bomb site")

st.header("kill")
st.write("jews")
image = Image.open('The_Happy_Merchant.jpg')

st.image(image, caption="they look like this")

texto= st.text.input('escriba algo','este es el texto')
st.write("el ttexto escrito es", texto)

col1, col2 = st.colums(2)

with col1:
  st.subheader("hola, q mas")
  st.write("hablelo")
  resp=st.checkbox("sizas")
  if resp:
    st.write("así es!")
