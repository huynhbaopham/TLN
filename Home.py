import streamlit as st
from streamlit_navigation_bar import st_navbar
from streamlit_lottie import st_lottie


# ---------------Settings -----------------

page_title = "TL Networks Inc. | Home"
page_icon = "./avicon.png"
layout = "wide"


# -----------------------------------------

st.set_page_config(
    page_title=page_title,
    page_icon=page_icon,
    layout=layout,
    initial_sidebar_state="collapsed",
)

# ------ NavBav ----------------------------
pages = ["About Us", "Services", "Careers", "Partners", "Contact Us"]

styles = {
    "nav": {
        "background-color": "#526D82",
        "justify-content": "center",
    },
    "div": {
        "max-width": "40rem",
    },
    "img": {
        "padding-left": "14px",
    },
    "span": {
        "color": "#DDE6ED",
        "border-radius": "0.5rem",
        "padding": "0.4375rem 0.625rem",
        "margin": "0 0.125rem",
    },
    "active": {
        "background-color": "#526D82",
        "font-weight": "bold",
    },
    "hover": {
        "background-color": "#526D82",
    },
}
options = {
    "show_menu": True,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    logo_path="./logo.svg",
    styles=styles,
    options=options,
)

# ----- HIDE Streamlit Style --------------

# hide_st_style = """
#     <style>
#         #MainMenu {visibility: hidden;}
#         footer {visibility:hidden;}
#         header {visibility:hidden;}
#         h1 {text-align:center;}
#         body {width: 80%;}
#     </style>
#     """
# st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Welcome to TL Networks")
with st.container(height=520, border=False):
    st.warning("Sorry! Our backend is under maintenance.", icon="🛠️")
    st_lottie(
        "https://lottie.host/9f9d63b5-63b0-4ac6-9ed7-3ca2f68c07a5/utWYeF1RLY.json",
        height=400,
        loop=True,
    )

st.divider()
with st.container():
    c1, c2 = st.columns([0.4, 0.6])
    c1.subheader("TL Networks Inc.")
    c1.write("9301 E Shea Blvd")
    c1.write("Scottsdale, AZ 85260")
    c1.write("accounting@tlnetworksinc.com")
    c3, c4 = c2.columns(2)
    c3.text_input("", placeholder="Your Firstname", label_visibility="collapsed")
    c4.text_input("", placeholder="Your Lastname", label_visibility="collapsed")
    c2.text_input("", placeholder="Your Email Here", label_visibility="collapsed")
    c2.text_area("", placeholder="Your Inquiry Here", label_visibility="collapsed")
    c2.button("Send", type="primary")
    st.divider()
    st.write("Copyright © TL Networks Inc. 2024")
