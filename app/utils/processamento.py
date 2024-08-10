import time
import streamlit as st


def processamento(texto1, texto2):
    with st.spinner(texto1):
        time.sleep(5)
    st.success(texto2)
