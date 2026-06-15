import streamlit as st
import pandas as pd

from utils.model_loader import load_model


st.title("📝 Manual Prediction")


st.markdown("""

Predict Smart Grid Stability manually

by entering all required features below.


The model will classify the system into:

🟢 Stable

🔴 Unstable

""")


st.markdown("---")


# =========================
# FEATURE DESCRIPTION
# =========================

st.subheader("📚 Feature Description")


desc = pd.DataFrame({

"Feature":[

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

],


"Description":[

"Response Time 1",

"Response Time 2",

"Response Time 3",

"Response Time 4",

"Power Produced 1",

"Power Produced 2",

"Power Produced 3",

"Power Produced 4",

"Price Elasticity 1",

"Price Elasticity 2",

"Price Elasticity 3",

"Price Elasticity 4"

]

})


st.dataframe(

    desc,

    use_container_width=True,

    hide_index=True

)


st.markdown("---")


# =========================
# LOAD MODEL
# =========================

model = load_model()


# =========================
# INPUT FEATURES
# =========================

st.subheader("⚙️ Input Features")


col1,col2,col3,col4=st.columns(4)


with col1:

    tau1=st.number_input(

        "tau1",

        value=2.0

    )


    p1=st.number_input(

        "p1",

        value=3.5

    )


    g1=st.number_input(

        "g1",

        value=0.05

    )



with col2:

    tau2=st.number_input(

        "tau2",

        value=3.1

    )


    p2=st.number_input(

        "p2",

        value=-1.2

    )


    g2=st.number_input(

        "g2",

        value=0.07

    )



with col3:

    tau3=st.number_input(

        "tau3",

        value=5.5

    )


    p3=st.number_input(

        "p3",

        value=-0.8

    )


    g3=st.number_input(

        "g3",

        value=0.09

    )



with col4:

    tau4=st.number_input(

        "tau4",

        value=8.7

    )


    p4=st.number_input(

        "p4",

        value=-1.5

    )


    g4=st.number_input(

        "g4",

        value=0.03

    )


st.markdown("---")


# =========================
# PREDICTION
# =========================

if st.button("🚀 Predict Stability"):


    data = pd.DataFrame({

        "tau1":[tau1],

        "tau2":[tau2],

        "tau3":[tau3],

        "tau4":[tau4],

        "p1":[p1],

        "p2":[p2],

        "p3":[p3],

        "p4":[p4],

        "g1":[g1],

        "g2":[g2],

        "g3":[g3],

        "g4":[g4]

    })


    pred = model.predict(data)[0]


    st.markdown("---")


    st.subheader("📊 Prediction Result")


    if pred=="stable":


        st.success("""

# 🟢 STABLE


The Smart Grid system

is predicted to be stable.


The electrical parameters

indicate that the system

can operate safely.

""")


    else:


        st.error("""

# 🔴 UNSTABLE


The Smart Grid system

is predicted to be unstable.


Further monitoring

and optimization

may be required.

""")


    st.markdown("---")


    # =========================
    # CONFIDENCE SCORE
    # =========================


    st.subheader("🎯 Confidence Score")


    try:


        proba = model.predict_proba(data)


        confidence = round(

            max(proba[0]) * 100,

            2

        )


        col1,col2,col3=st.columns([1,2,1])


        with col2:


            st.metric(

                "Model Confidence",

                f"{confidence}%"

            )


            st.progress(

                confidence / 100

            )


            if confidence>=90:


                st.success(

                    "Very High Confidence"

                )


            elif confidence>=70:


                st.info(

                    "High Confidence"

                )


            else:


                st.warning(

                    "Low Confidence"

                )



    except:


        st.info(

            "Confidence Score is not available."

        )



    st.markdown("---")


    # =========================
    # INPUT SUMMARY
    # =========================


    st.subheader("📄 Input Summary")


    st.dataframe(

        data,

        use_container_width=True,

        hide_index=True

    )