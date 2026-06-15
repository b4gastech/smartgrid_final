import streamlit as st
import pandas as pd

from utils.model_loader import load_model


st.title("📁 Batch Prediction")


st.markdown("""

Upload a CSV file containing Smart Grid data

to predict whether the system is:

🟢 Stable

🔴 Unstable

""")


st.markdown("---")


# =========================
# CSV FORMAT INFO
# =========================

st.info("""

### 📄 Required CSV Columns

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


# =========================
# TEMPLATE CSV
# =========================

template = pd.DataFrame({

    "tau1":[2.0],

    "tau2":[3.1],

    "tau3":[5.5],

    "tau4":[8.7],

    "p1":[3.5],

    "p2":[-1.2],

    "p3":[-0.8],

    "p4":[-1.5],

    "g1":[0.05],

    "g2":[0.07],

    "g3":[0.09],

    "g4":[0.03]

})


csv_template = template.to_csv(index=False)


st.download_button(

    label="📥 Download CSV Template",

    data=csv_template,

    file_name="template_smart_grid.csv",

    mime="text/csv"

)


st.markdown("---")


# =========================
# FILE UPLOAD
# =========================

uploaded = st.file_uploader(

    "📤 Upload CSV File",

    type=["csv"]

)


if uploaded:


    try:


        df = pd.read_csv(uploaded)


        required_columns=[

            "tau1",

            "tau2",

            "tau3",

            "tau4",

            "p1",

            "p2",

            "p3",

            "p4",

            "g1",

            "g2",

            "g3",

            "g4"

        ]


        if list(df.columns)!=required_columns:


            st.error(

                "❌ Invalid CSV Format"

            )


            st.warning(

                "Please use the CSV Template."

            )


            st.stop()



        st.subheader("📄 Dataset Preview")


        st.dataframe(

            df.head(10),

            use_container_width=True,

            hide_index=True

        )


        st.success(

            f"Dataset loaded successfully with {len(df)} rows."

        )


        st.markdown("---")


        model=load_model()



        if st.button("🚀 Run Prediction"):


            pred=model.predict(df)


            df["Prediction"]=pred


            st.success(

                "Prediction Completed Successfully"

            )


            st.markdown("---")


            # =====================

            # STATISTICS

            # =====================


            stable=(

                df["Prediction"]

                =="stable"

            ).sum()



            unstable=(

                df["Prediction"]

                =="unstable"

            ).sum()



            total=len(df)



            col1,col2,col3=st.columns(3)



            with col1:


                st.metric(

                    "📊 Total Data",

                    total

                )



            with col2:


                st.metric(

                    "🟢 Stable",

                    stable

                )



            with col3:


                st.metric(

                    "🔴 Unstable",

                    unstable

                )


            st.markdown("---")


            st.subheader(

                "📑 Prediction Result"

            )


            st.dataframe(

                df,

                use_container_width=True,

                hide_index=True

            )


            st.markdown("---")


            csv=df.to_csv(

                index=False

            )


            st.download_button(

                label="📥 Download Prediction Result",

                data=csv,

                file_name="prediction_result.csv",

                mime="text/csv"

            )


    except Exception as e:


        st.error(

            "Failed to process CSV file."

        )


        st.exception(e)