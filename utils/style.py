import streamlit as st

def load_css():

    st.markdown("""

<style>

.stApp{

background:

linear-gradient(

135deg,

#020617,

#0f172a,

#1e293b

);

color:white;

}


/* Hero */

.hero{

padding:50px;

text-align:center;

border-radius:30px;

background:

rgba(

255,

255,

255,

0.08

);

backdrop-filter:

blur(20px);

box-shadow:

0 8px 32px

rgba(

0,

0,

0,

0.4

);

margin-bottom:30px;

}


.hero h1{

font-size:48px;

font-weight:700;

}


.hero p{

font-size:18px;

opacity:0.9;

}



/* Metric */

[data-testid="metric-container"]{

background:

rgba(

255,

255,

255,

0.08

);

padding:20px;

border-radius:20px;

box-shadow:

0 5px 20px

rgba(

0,

0,

0,

0.3

);

transition:0.3s;

}



[data-testid="metric-container"]:hover{

transform:

translateY(-5px);

}



/* Button */

.stButton>button{

width:100%;

height:55px;

border-radius:15px;

font-size:18px;

font-weight:bold;

background:

linear-gradient(

90deg,

#3b82f6,

#06b6d4

);

color:white;

border:none;

}



.stButton>button:hover{

transform:scale(1.02);

transition:0.3s;

}


/* Sidebar */

section[data-testid="stSidebar"]{

background:#0b1120;

}

</style>

""",

unsafe_allow_html=True

)