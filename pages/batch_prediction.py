import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.style import load_css
from utils.model_loader import load_models

# ======================
# LOAD CSS & MODEL
# ======================
load_css()
dt, knn, svm = load_models()

# ======================
# SIDEBAR
# ======================
st.sidebar.title("⚙ Model Configuration")
model_name = st.sidebar.radio("Choose Model", ["Decision Tree", "KNN", "SVM"])
st.sidebar.markdown("---")
st.sidebar.write(f"Model Status:")
st.sidebar.write("🟢 Decision Tree - READY")
st.sidebar.write("🟢 KNN - READY" if knn else "🟡 KNN - COMING SOON")
st.sidebar.write("🟢 SVM - READY" if svm else "🟡 SVM - COMING SOON")

# Select Model Logic
if model_name == "Decision Tree": model = dt
elif model_name == "KNN": model = knn if knn else dt
else: model = svm if svm else dt

# ======================
# PAGE
# ======================
st.title("📁 CSV Batch Prediction")
st.info(f"Running Model: **{model_name}**")

# ======================
# TEMPLATE DOWNLOAD
# ======================
with st.expander("ℹ️ Need help with file format?"):
    st.write("Ensure your CSV has these columns: `tau1, tau2, tau3, tau4, p1, p2, p3, p4, g1, g2, g3, g4`")
    # Membuat template CSV
    template_data = pd.DataFrame(columns=['tau1','tau2','tau3','tau4','p1','p2','p3','p4','g1','g2','g3','g4'])
    st.download_button(
        label="📥 Download Template CSV",
        data=template_data.to_csv(index=False).encode('utf-8'),
        file_name='template_smartgrid.csv',
        mime='text/csv'
    )

# ======================
# UPLOAD
# ======================
file = st.file_uploader("Upload your dataset CSV", type=["csv"])
features = ["tau1","tau2","tau3","tau4","p1","p2","p3","p4","g1","g2","g3","g4"]

if file:
    df = pd.read_csv(file)
    st.subheader("Preview Dataset")
    st.dataframe(df.head())

    if st.button("🚀 Run Prediction"):
        missing = [x for x in features if x not in df.columns]
        if missing:
            st.error(f"Missing columns: {missing}")
        else:
            X = df[features]
            pred = model.predict(X)
            
            # Add Prediction to DF
            df["prediction"] = pred
            df["Prediction Label"] = df["prediction"].map(lambda x: "STABLE" if x == 1 else "UNSTABLE")

            # Metrics
            stable = (pred == 1).sum()
            unstable = (pred == 0).sum()
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Data", len(df))
            col2.metric("Stable", stable)
            col3.metric("Unstable", unstable)

            # Charts
            c1, c2 = st.columns(2)
            with c1:
                st.subheader("Distribution (Pie)")
                fig, ax = plt.subplots(figsize=(4,4))
                ax.pie([stable, unstable], labels=["Stable", "Unstable"], autopct="%1.1f%%", colors=['#66b3ff','#ff9999'])
                st.pyplot(fig)
            
            with c2:
                st.subheader("Distribution (Bar)")
                fig2, ax2 = plt.subplots(figsize=(5,4))
                ax2.bar(["Stable", "Unstable"], [stable, unstable], color=['#66b3ff','#ff9999'])
                st.pyplot(fig2)

            # Results
            st.subheader("Prediction Result")
            st.dataframe(df)

            # Download Result
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("⬇ Download Result", csv, "prediction_result.csv", "text/csv")