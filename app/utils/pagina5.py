
import streamlit as st

from utils.textos import PAG5_TEXTO1
from utils.textos import PAG5_TEXTO2
from utils.imagens import abre_imagem
from utils.botoes import botoes_pagina5


def pagina5():
    st.balloons()
    with st.container():
        if st.session_state["coluna_selecionada"] == 1:
            cartas = st.session_state["coluna2"] + st.session_state["coluna1"] + st.session_state["coluna3"]
        elif st.session_state["coluna_selecionada"] == 2:
            cartas = st.session_state["coluna1"] + st.session_state["coluna2"] + st.session_state["coluna3"]
        elif st.session_state["coluna_selecionada"] == 3:
            cartas = st.session_state["coluna2"] + st.session_state["coluna3"] + st.session_state["coluna1"]
        carta_selecionada = cartas[7][2]
        st.markdown(PAG5_TEXTO1, unsafe_allow_html=True)
        _, centro, __ = st.columns((1, 2.5, 0.1), vertical_alignment="center")
        with centro:
            abre_imagem(carta_selecionada)
        st.markdown(PAG5_TEXTO2, unsafe_allow_html=True)
        _, botao, _ = st.columns((1.3, 2.5, 0.1))
        with botao:
            st.button("Vamos começar novamente?", type="primary", on_click=botoes_pagina5)
    st.balloons()

    