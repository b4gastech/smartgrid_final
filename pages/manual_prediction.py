import streamlit as st

import numpy as np

from utils.style import load_css

from utils.model_loader import load_models


load_css()

dt,knn,svm=load_models()


st.sidebar.title(

"⚙ Model"

)

model_name=st.sidebar.radio(

"Choose",

[

"Decision Tree",

"KNN",

"SVM"

]

)


if model_name=="Decision Tree":

    model=dt


elif model_name=="KNN":

    st.sidebar.warning(

    "Coming Soon"

    )

    model=dt


else:

    st.sidebar.warning(

    "Coming Soon"

    )

    model=dt



features=[

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


st.title(

"🧠 Manual Prediction"

)


c1,c2,c3=st.columns(3)


inputs=[]


for i,f in enumerate(features):

    with [c1,c2,c3][i%3]:

        x=st.number_input(

        f,

        value=0.0

        )

        inputs.append(x)


if st.button(

"⚡ Predict"

):

    data=np.array([inputs])

    pred=model.predict(data)


    if pred[0]==1:

        st.success(

        "🟢 STABLE"

        )


    else:

        st.error(

        "🔴 UNSTABLE"

        )