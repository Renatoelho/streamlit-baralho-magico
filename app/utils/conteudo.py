
import os
from pathlib import Path

import streamlit as st

local_css = f"{Path(os.path.abspath(__file__)).parent.parent}/css"

with open(f"{local_css}/styles_css.css", "r+") as file:
    esconde_css = file.read()

def esconde_css_streamlit() -> st:
    st.markdown(esconde_css, unsafe_allow_html=True)