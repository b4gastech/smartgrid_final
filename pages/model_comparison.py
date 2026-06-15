import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.style import load_css

# Load CSS Custom
load_css()

st.title("🏆 Model Performance Comparison")

# Data perbandingan model dengan nilai akurasi terbaru
data = {
    "Model": ["Decision Tree", "KNN", "SVM"],
    "Accuracy": [0.74, 0.79, 0.98],
    "Precision": [0.72, 0.77, 0.97],
    "Recall": [0.70, 0.75, 0.99]
}

df = pd.DataFrame(data)

# Tampilan Tabel Metrik
st.subheader("Performance Metrics")
st.table(df.style.highlight_max(axis=0, subset=['Accuracy', 'Precision', 'Recall']))

# Visualisasi Grafik
st.subheader("Accuracy Comparison")
fig, ax = plt.subplots(figsize=(8, 4))
sns.set_style("whitegrid")

# Bar plot dengan warna yang menonjolkan model terbaik (SVM)
colors = ['#C44E52', '#55A868', '#4C72B0'] # Warna untuk DT, KNN, SVM
sns.barplot(x="Model", y="Accuracy", data=df, palette=colors, ax=ax)

# Memberi label angka di atas bar
for i, v in enumerate(df["Accuracy"]):
    ax.text(i, v + 0.01, f"{v*100:.1f}%", ha='center', fontweight='bold')

ax.set_ylim(0, 1.1)
ax.set_ylabel("Accuracy Score")
st.pyplot(fig)

# Analisis Kesimpulan
st.markdown("---")
st.subheader("📊 Conclusion")
best_model = df.loc[df['Accuracy'].idxmax(), 'Model']

st.success(f"**Best Performing Model:** {best_model}")
st.write(f"""
Berdasarkan hasil pengujian, **{best_model}** menunjukkan performa yang paling unggul dengan tingkat akurasi mencapai **{df['Accuracy'].max()*100:.1f}%**.
SVM menjadi pilihan terbaik dalam kasus ini karena kemampuannya dalam memisahkan kelas data secara lebih efektif dibandingkan model lainnya.
""")