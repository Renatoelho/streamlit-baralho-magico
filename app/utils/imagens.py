
from PIL import Image
import streamlit as st


def abre_imagem(caminho_imagem):
    st.image(Image.open(caminho_imagem))
