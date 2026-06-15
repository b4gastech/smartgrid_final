import streamlit as st
import pandas as pd
import joblib
import os

# ======================================
# PAGE CONFIG
# ======================================
st.set_page_config(page_title="Smart Grid Multi-Model", page_icon="⚡", layout="wide")

# ======================================
# PATH SETUP & LOAD MODELS
# ======================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

@st.cache_resource
def load_all_models():
    models = {
        "Decision Tree": joblib.load(os.path.join(MODEL_DIR, "decision_tree_model.pkl")),
        "SVM": joblib.load(os.path.join(MODEL_DIR, "svm_model.pkl")),
        "KNN": joblib.load(os.path.join(MODEL_DIR, "knn_model.pkl"))
    }
    scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
    return models, scaler

try:
    models, scaler = load_all_models()
except Exception as e:
    st.error(f"Gagal memuat model. Pastikan semua file .pkl ada di folder 'models'. Error: {e}")
    st.stop()

fitur = ['tau1', 'tau2', 'tau3', 'tau4', 'p1', 'p2', 'p3', 'p4', 'g1', 'g2', 'g3', 'g4']

# ======================================
# SIDEBAR
# ======================================
with st.sidebar:
    st.title("⚡ Smart Grid Control")
    menu = st.radio("Navigasi", ["🏠 Home", "🔍 Prediksi Manual", "📁 Analisis CSV"])
    st.markdown("---")
    selected_model_name = st.selectbox("Pilih Algoritma", list(models.keys()))
    
    # Identitas Kelompok di Sidebar
    st.markdown("---")
    st.subheader("👥 Tim Pengembang")
    st.write("• Dista")
    st.write("• Piqi")
    st.write("• Tora")

# ======================================
# LOGIKA PREDIKSI
# ======================================
def get_prediction(data, model_name):
    if model_name != "Decision Tree":
        data = scaler.transform(data)
    
    hasil = models[model_name].predict(data)[0]
    return hasil

# ======================================
# MAIN CONTENT
# ======================================
if menu == "🏠 Home":
    st.title("⚡ Smart Grid Stability Analysis")
    st.markdown("""
    Selamat datang di aplikasi prediksi stabilitas jaringan listrik. 
    Aplikasi ini menggunakan algoritma Machine Learning untuk memprediksi apakah jaringan listrik dalam kondisi **STABLE** atau **UNSTABLE** berdasarkan parameter input yang diberikan.
    """)
    
    # Dashboard Cards
    col1, col2, col3 = st.columns(3)
    col1.metric("Model Tersedia", "3", "DT, KNN, SVM")
    col2.metric("Fitur Input", "12", "Parameter Jaringan")
    col3.metric("Status", "Online", "Ready to Use")
    
    st.success("Silakan pilih menu di sidebar untuk memulai prediksi.")

elif menu == "🔍 Prediksi Manual":
    st.subheader(f"Input Data Parameter ({selected_model_name})")
    
    inputs = {}
    cols = st.columns(4) # Menggunakan 4 kolom agar lebih rapi
    for i, f in enumerate(fitur):
        inputs[f] = cols[i % 4].number_input(f.upper(), value=0.0, format="%.4f")

    if st.button("🚀 Proses Prediksi"):
        input_df = pd.DataFrame([inputs])
        hasil = get_prediction(input_df, selected_model_name)
        st.divider()
        st.success(f"### Hasil Prediksi: {hasil.upper()}")

elif menu == "📁 Analisis CSV":
    st.subheader(f"Analisis Batch dengan {selected_model_name}")
    
    # Template Download
    with st.expander("ℹ️ Panduan Format Data"):
        st.write("Pastikan file CSV memiliki kolom: " + ", ".join(fitur))
        template_df = pd.DataFrame(columns=fitur)
        st.download_button("📥 Download Template CSV", template_df.to_csv(index=False).encode('utf-8'), "template_smartgrid.csv")

    uploaded_file = st.file_uploader("Upload file dataset CSV", type=["csv"])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        df.columns = df.columns.str.strip() 
        
        if not all(col in df.columns for col in fitur):
            st.error(f"Format CSV tidak sesuai! Pastikan kolom Anda adalah: {fitur}")
        else:
            st.dataframe(df.head())
            if st.button("Jalankan Prediksi"):
                with st.spinner('Sedang memproses data...'):
                    df["Prediksi"] = [get_prediction(df[fitur].iloc[[i]], selected_model_name) for i in range(len(df))]
                    st.success("Prediksi Selesai!")
                    st.dataframe(df)
                    st.download_button("📥 Download Hasil", df.to_csv(index=False).encode('utf-8'), "hasil_prediksi.csv")

st.markdown("---")
st.caption("Developed by Tubes Dasildat Kelompok 5 | Dista - Piqi - Tora")