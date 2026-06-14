import streamlit as st


def load_css():

    st.markdown("""
    <style>

    .stApp{
        background:
        radial-gradient(circle at top,
        #0f172a,
        #020617);

        color:white;
    }

    #MainMenu{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    header{
        visibility:hidden;
    }

    section[data-testid="stSidebar"]{

        background:#0f172a;

        border-right:

        1px solid rgba(
        255,255,255,0.1);

    }

    </style>
    """,
    unsafe_allow_html=True)