
import streamlit as st


def botao_pagina1():
    st.session_state["pagina1"] = False
    st.session_state["pagina2"] = True

def botoes_pagina2(numero_coluna):
    st.session_state["pagina1"] = False
    st.session_state["pagina2"] = False
    st.session_state["pagina3"] = True
    st.session_state["coluna_selecionada"] = numero_coluna

def botoes_pagina3(numero_coluna):
    st.session_state["pagina1"] = False
    st.session_state["pagina2"] = False
    st.session_state["pagina3"] = False
    st.session_state["pagina4"] = True
    st.session_state["coluna_selecionada"] = numero_coluna

def botoes_pagina4(numero_coluna):
    st.session_state["pagina1"] = False
    st.session_state["pagina2"] = False
    st.session_state["pagina3"] = False
    st.session_state["pagina4"] = False
    st.session_state["pagina5"] = True
    st.session_state["coluna_selecionada"] = numero_coluna

def botoes_pagina5():
    st.session_state["pagina1"] = False
    st.session_state["pagina2"] = True
    st.session_state["pagina3"] = False
    st.session_state["pagina4"] = False
    st.session_state["pagina5"] = False
    st.session_state["coluna_selecionada"] = None