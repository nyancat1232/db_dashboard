import streamlit as st
import time
import pyplus.streamlit as stp
from displayer import Displayer

st.set_page_config(layout="wide")

hide_streamlit_style='''
            <style>
                /* Hide the Streamlit header and menu */
                header {visibility: hidden;}
                /* Hide your specific div class, replace class name with the one you identified */
                .st-emotion-cache-1jicfl2 {
                    padding: 0rem 0rem 0rem;
                }
                .st-emotion-cache-1eup5c7 {
                    gap: 0rem;
                }
            </style>
        '''

st.session_state['height_max']=200

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with st.container(height=st.session_state.height_max):
    function_list = [func for func in dir(Displayer) if not func.startswith('_')]
    tp = stp.TabsPlus(titles=function_list,layout='column')
    for key in function_list:
        with tp[key]:
            getattr(Displayer, key)()

time.sleep(1.0)
st.rerun()