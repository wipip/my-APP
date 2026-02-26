import streamlit as st
from PIL import Image

st.title("israel bomb site")

st.header("kill")
st.write("jews")
image = Image.open('The_Happy_Merchant.jpg')

st.image(image, caption="they look like this")

texto= st.text_input('escriba algo','este es el texto')
st.write("el ttexto escrito es", texto)

col1, col2 = st.columns(2)

with col1:
  st.subheader("hola, q mas")
  st.write("hablelo")
  resp=st.checkbox("sizas")
  if resp:
    st.write("así es!")

with col2:
  st.subheader("esta es la otra columna")
  modo = st.radio("seleccione un modo",('visual','auditivo','tactil'))
  if modo =='visual':
    st.write("vealo")
  if modo =='auditivo':
    st.write("escuchelo")
  if modo =='tactil':
    st.write("sobelo")

st.subheader("selectbox")
in_mod = st.selectbox(
  "selecciona un modo",
  ("pequeño","mediano","grande"),
)
if in_mod =="pequeño":
  set_mod ="Talla S"
if in_mod =="mediano":
  set_mod ="Talla M"
if in_mod =="pgrande":
  set_mod ="Talla L"
st.subheader("usar botones")
if st.button("presionelo"):
  st.write("AAAAYYYYY")
else:
  st.write(":","(")
