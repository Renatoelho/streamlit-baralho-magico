
import streamlit as st

from utils.textos import PAG4_TEXTO1
from utils.textos import PAG4_TEXTO2
from utils.imagens import abre_imagem
from utils.botoes import botoes_pagina4
from utils.processamento import processamento


def pagina4():
    processamento("Embaralhando mais uma vez...", "Agora vai!!!")
    if st.session_state["coluna_selecionada"] == 1:
        cartas = st.session_state["coluna2"] + st.session_state["coluna1"] + st.session_state["coluna3"]
    elif st.session_state["coluna_selecionada"] == 2:
        cartas = st.session_state["coluna1"] + st.session_state["coluna2"] + st.session_state["coluna3"]
    elif st.session_state["coluna_selecionada"] == 3:
        cartas = st.session_state["coluna2"] + st.session_state["coluna3"] + st.session_state["coluna1"]
    coluna1 = [cartas[0], cartas[3], cartas[6], cartas[9], cartas[12]]
    coluna2 = [cartas[1], cartas[4], cartas[7], cartas[10], cartas[13]]
    coluna3 = [cartas[2], cartas[5], cartas[8], cartas[11], cartas[14]]
    st.session_state["coluna1"] = coluna1
    st.session_state["coluna2"] = coluna2
    st.session_state["coluna3"] = coluna3
    posicoes = [0, 1, 2, 3, 4]
    st.markdown(PAG4_TEXTO1, unsafe_allow_html=True)
    st.markdown(PAG4_TEXTO2, unsafe_allow_html=True)
    st.divider()
    col1, col2, col3 = st.columns(3, gap="small", vertical_alignment="center")
    with st.container():
        for posicao, item1, item2, item3 in zip(posicoes, coluna1, coluna2, coluna3):
            with col1:
                if posicao != 4:
                    abre_imagem(item1[1])
                else:
                    abre_imagem(item1[0])
                    st.divider()
                    st.button("Coluna 1", type="primary", on_click=lambda: botoes_pagina4(1))
            with col2:
                if posicao != 4:
                    abre_imagem(item2[1])
                else:
                    abre_imagem(item2[0])
                    st.divider()
                    st.button("Coluna 2", type="primary", on_click=lambda: botoes_pagina4(2))
            with col3:
                if posicao != 4:
                    abre_imagem(item3[1])
                else:
                    abre_imagem(item3[0])
                    st.divider()
                    st.button("Coluna 3", type="primary", on_click=lambda: botoes_pagina4(3))
