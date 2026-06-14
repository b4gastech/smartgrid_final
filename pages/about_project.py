import streamlit as st

from utils.style import load_css


# ======================
# LOAD STYLE
# ======================

load_css()


# ======================
# HEADER
# ======================

st.title("📖 About Project")

st.caption(
    "SmartGrid AI Platform • Machine Learning Classification Project"
)

st.markdown("---")


# ======================
# OVERVIEW
# ======================

st.subheader("🎯 Project Overview")

st.write("""

SmartGrid AI Platform adalah aplikasi Machine Learning berbasis Streamlit
yang digunakan untuk memprediksi stabilitas sistem Smart Grid.

Aplikasi ini dibuat untuk membantu pengguna melakukan prediksi
stabilitas jaringan listrik menggunakan algoritma Machine Learning.

Fitur utama:

✅ Manual Prediction

✅ CSV Batch Prediction

✅ Model Comparison

✅ Interactive Dashboard

✅ Download Prediction Result

""")


# ======================
# DATASET
# ======================

st.markdown("---")

st.subheader("📊 Dataset Information")

col1,col2,col3,col4=st.columns(4)

with col1:

    st.metric(
        "Total Data",
        "60,000"
    )

with col2:

    st.metric(
        "Features",
        "12"
    )

with col3:

    st.metric(
        "Target",
        "stabf"
    )

with col4:

    st.metric(
        "Classes",
        "2"
    )


st.write("""

Dataset yang digunakan adalah:

### Smart Grid Stability Dataset

Dataset ini digunakan untuk memprediksi apakah sistem Smart Grid berada pada kondisi:

- Stable
- Unstable

Dataset memiliki 12 feature utama:

""")

st.code("""

tau1
tau2
tau3
tau4

p1
p2
p3
p4

g1
g2
g3
g4

""")

st.write("""

Target yang digunakan:

- stab  → nilai numerik stabilitas

- stabf → label stable / unstable

""")


# ======================
# MACHINE LEARNING MODEL
# ======================

st.markdown("---")

st.subheader("🧠 Machine Learning Model")


st.info("""

Primary Model

🌳 Decision Tree Classifier

Accuracy

📈 88.46%

""")


st.write("""

Alasan memilih Decision Tree:

✅ Mudah diinterpretasikan

✅ Cepat dalam proses training

✅ Cocok untuk klasifikasi

✅ Memiliki performa yang baik
pada Smart Grid Stability Dataset

""")


# ======================
# WORKFLOW
# ======================

st.markdown("---")

st.subheader("⚙ Workflow")


st.info("""

📁 Dataset CSV

⬇

🧹 Preprocessing

⬇

✂ Train Test Split

⬇

🌳 Decision Tree Training

⬇

📈 Model Evaluation

⬇

💾 Save Model (.pkl)

⬇

⚡ Deploy Streamlit

""")


# ======================
# TECHNOLOGY
# ======================

st.markdown("---")

st.subheader("🛠 Technology Stack")


c1,c2,c3=st.columns(3)


with c1:

    st.success("""

🐍 Python

📊 Pandas

🔢 NumPy

""")


with c2:

    st.success("""

🌳 Scikit Learn

💾 Joblib

📈 Matplotlib

""")


with c3:

    st.success("""

⚡ Streamlit

🎨 Custom CSS

📂 Multi Page App

""")


# ======================
# CONTRIBUTION
# ======================

st.markdown("---")

st.subheader("🎓 My Contribution")


st.success("""

• Dataset preprocessing

• Decision Tree model training

• Streamlit UI development

• CSV Batch Prediction

• Data visualization

""")


# ======================
# TEAM
# ======================

st.markdown("---")

st.subheader("👥 Team")


st.write("""

Project ini dibuat sebagai tugas kelompok
mata kuliah Data Mining / Dasar Ilmu Data.

SmartGrid AI Platform © 2026

""")


# ======================
# FOOTER
# ======================

st.markdown("---")

st.caption(
    "Built with ❤️ using Streamlit & Scikit-Learn"
)