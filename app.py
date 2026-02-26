import streamlit as st
From PIL import Image

st.title("israel bomb site")

st.header("kill")
st.write("jews")
image = Image.open('The_Happy_Merchant.jpg')

st.image(image, caption="they look like this")

texto= st.text.input('escriba algo','este es el texto')
st.write("el ttexto escrito es", texto)
