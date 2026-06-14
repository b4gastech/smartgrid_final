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

st.sidebar.title("⚙ Model")

model_name = st.sidebar.radio(
    "Choose Model",
    [
        "Decision Tree",
        "KNN",
        "SVM"
    ]
)

st.sidebar.markdown("---")

st.sidebar.write("🟢 Decision Tree - READY")
st.sidebar.write(
    "🟢 KNN - READY"
    if knn else
    "🟡 KNN - COMING SOON"
)

st.sidebar.write(
    "🟢 SVM - READY"
    if svm else
    "🟡 SVM - COMING SOON"
)

# ======================
# MODEL SELECT
# ======================

if model_name == "Decision Tree":

    model = dt

elif model_name == "KNN":

    model = knn if knn else dt

else:

    model = svm if svm else dt


# ======================
# PAGE
# ======================

st.title("📁 CSV Batch Prediction")

st.caption(
    f"Running Model : **{model_name}**"
)

# ======================
# UPLOAD
# ======================

file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

# ======================
# FEATURES
# ======================

features = [

    "tau1","tau2",
    "tau3","tau4",

    "p1","p2",
    "p3","p4",

    "g1","g2",
    "g3","g4"

]

# ======================
# READ FILE
# ======================

if file:

    df = pd.read_csv(file)

    st.subheader("Preview Dataset")

    st.dataframe(df.head())

    st.write("Columns :")

    st.write(df.columns.tolist())

    # ======================
    # RUN PREDICTION
    # ======================

    if st.button("🚀 Run Prediction"):

        missing = [

            x for x in features

            if x not in df.columns

        ]

        if missing:

            st.error(

                f"Missing columns : {missing}"

            )

        else:

            X = df[features]

            pred = model.predict(X)

            # DEBUG

            st.subheader("Prediction Distribution")

            st.write(

                pd.Series(pred)

                .value_counts()

            )

            st.write(

                "20 first predictions"

            )

            st.write(

                pred[:20]

            )

            # SAVE

            df["prediction"] = pred

            df["Prediction Label"] = df[
                "prediction"
            ].map(

                lambda x:

                "STABLE"

                if x == 1

                else

                "UNSTABLE"

            )

            # ======================
            # METRICS
            # ======================

            stable = (

                pred == 1

            ).sum()

            unstable = (

                pred == 0

            ).sum()

            col1, col2, col3 = st.columns(3)

            col1.metric(

                "Total Data",

                len(df)

            )

            col2.metric(

                "Stable",

                stable

            )

            col3.metric(

                "Unstable",

                unstable

            )

            # ======================
            # CHART
            # ======================

            c1, c2 = st.columns(2)

            with c1:

                fig, ax = plt.subplots(
                    figsize=(4,4)
                )

                ax.pie(

                    [stable, unstable],

                    labels=[

                        "Stable",

                        "Unstable"

                    ],

                    autopct="%1.1f%%"

                )

                st.pyplot(fig)

            with c2:

                fig2, ax2 = plt.subplots(
                    figsize=(5,4)
                )

                ax2.bar(

                    [

                        "Stable",

                        "Unstable"

                    ],

                    [

                        stable,

                        unstable

                    ]

                )

                st.pyplot(fig2)

            # ======================
            # RESULT TABLE
            # ======================

            st.subheader(

                "Prediction Result"

            )

            st.dataframe(df)

            # ======================
            # REAL LABEL CHECK
            # ======================

            if "stabf" in df.columns:

                st.subheader(

                    "Actual Label Distribution"

                )

                st.write(

                    df["stabf"]

                    .value_counts()

                )

            # ======================
            # DOWNLOAD
            # ======================

            csv = df.to_csv(

                index=False

            ).encode("utf-8")

            st.download_button(

                "⬇ Download Result",

                csv,

                "prediction_result.csv",

                "text/csv"

            )