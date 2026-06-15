import streamlit as st
from utils.style import load_css

st.set_page_config(
    page_title="Smart Grid Stability",
    page_icon="🌳",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

st.title("🌳 SMART GRID STABILITY DASHBOARD")

st.markdown("""
<div class="hero">

<h1>Decision Tree Classification</h1>

<p>

Predict Smart Grid Stability using Machine Learning.

Classify whether the system is Stable or Unstable.

</p>

</div>

""", unsafe_allow_html=True)


col1,col2,col3,col4=st.columns(4)

with col1:

    st.metric(

        "📂 Dataset",

        "60000"

    )

with col2:

    st.metric(

        "⚡ Features",

        "12"

    )


with col3:

    st.metric(

        "🌳 Algorithm",

        "Decision Tree"

    )


with col4:

    st.metric(

        "🎯 Target",

        "stabf"

    )


st.markdown("---")


st.subheader("⚡ Machine Learning Workflow")

st.code("""

Dataset

↓

Preprocessing

↓

Train Test Split

↓

Decision Tree Training

↓

Model Evaluation

↓

Deployment Streamlit

""")


st.markdown("---")


col1,col2,col3=st.columns(3)

with col1:

    st.info("""

### 📝 Manual Prediction


Predict Smart Grid

manually.

""")


with col2:

    st.success("""

### 📁 Batch Prediction


Upload CSV

and predict

multiple data.

""")


with col3:

    st.warning("""

### 📈 Model Information


View parameters

and evaluation.

""")



st.markdown("---")

st.caption(

"🌳 Smart Grid Stability Dashboard | Decision Tree | 2026"

)