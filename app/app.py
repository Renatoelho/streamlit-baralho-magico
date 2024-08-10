
import streamlit as st

from utils.pagina1 import pagina1
from utils.pagina2 import pagina2
from utils.pagina3 import pagina3
from utils.pagina4 import pagina4
from utils.pagina5 import pagina5
from utils.configura_pagina import configura_pagina
from utils.conteudo import esconde_css_streamlit


configura_pagina()
esconde_css_streamlit()

if "pagina1" not in st.session_state:
      st.session_state["pagina1"] = True

if st.session_state["pagina1"]:
    pagina1()
elif st.session_state["pagina2"]:
    pagina2()
elif st.session_state["pagina3"]:
    pagina3()
elif st.session_state["pagina4"]:
    pagina4()
elif st.session_state["pagina5"]:
    pagina5()
