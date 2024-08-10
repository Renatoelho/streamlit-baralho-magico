
import os
from pathlib import Path

import streamlit as st

from utils.textos import PAG1_TEXTO0
from utils.textos import PAG1_TEXTO1
from utils.textos import PAG1_TEXTO2
from utils.botoes import botao_pagina1
from utils.imagens import abre_imagem


caminho_carta = f"{Path(os.path.abspath(__file__)).parent.parent}/imagens/"

def pagina1():
    _, centro, __ = st.columns((0.1,5.8,0.1), vertical_alignment="center")
    with centro:
        st.markdown(PAG1_TEXTO1, unsafe_allow_html=True)
        st.markdown(PAG1_TEXTO2, unsafe_allow_html=True)
        abre_imagem(f"{caminho_carta}background_cards.jpg")
    _, botao, __ = st.columns((1.4, 2.5, 0.1), vertical_alignment="center")
    with botao:
        st.button("Vamos começar o Jogo?", type="primary", on_click=botao_pagina1)
    st.warning(PAG1_TEXTO0, icon="⚠️")

