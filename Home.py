import streamlit as st

# ---------------Settings -----------------

page_title = "TL Networks Inc. | Home"
page_icon = "./avicon.png"
layout = "centered"


# -----------------------------------------

st.set_page_config(
    page_title=page_title,
    page_icon=page_icon,
    layout=layout,
    initial_sidebar_state="collapsed",
)
st.title("Welcome to TL Networks")

# ----- HIDE Streamlit Style --------------

hide_st_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility:hidden;}
        header {visibility:hidden;}
        h1 {text-align:center;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)

with st.container(border=True):
    st.warning("Sorry! Our backend is under maintenance.", icon="🛠️")
