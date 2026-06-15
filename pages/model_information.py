import streamlit as st
import pandas as pd


st.title("📈 Model Information")


st.markdown("""

This page provides information

about the dataset,

features,

and the Decision Tree model

used in this project.

""")


st.markdown("---")


# =========================
# DATASET INFORMATION
# =========================

st.subheader("📂 Dataset Information")


col1,col2,col3=st.columns(3)


with col1:

    st.metric(

        "Dataset",

        "Smart Grid"

    )


with col2:

    st.metric(

        "Records",

        "60000"

    )


with col3:

    st.metric(

        "Features",

        "12"

    )



st.info("""

### About Dataset


The Smart Grid Stability Dataset

contains electrical parameters

used to determine whether

a Smart Grid system

is Stable or Unstable.


The dataset consists of:


• 60,000 records


• 12 input features


• Binary classification target


• Two prediction classes:

stable and unstable

""")


st.markdown("---")


# =========================
# FEATURES
# =========================

st.subheader("⚡ Features Used")


features=pd.DataFrame({

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

    features,

    use_container_width=True,

    hide_index=True

)


st.markdown("---")


# =========================
# FEATURE CATEGORY
# =========================


col1,col2,col3=st.columns(3)


with col1:


    st.warning("""

### Tau Features


tau1

tau2

tau3

tau4


Represent the response time

of generators.

""")


with col2:


    st.info("""

### Power Features


p1

p2

p3

p4


Represent power produced

by generators.

""")


with col3:


    st.success("""

### Elasticity Features


g1

g2

g3

g4


Represent price elasticity

coefficients.

""")


st.markdown("---")


# =========================
# DECISION TREE
# =========================


st.subheader("🌳 Decision Tree Model")


col1,col2,col3=st.columns(3)


with col1:

    st.metric(

        "Criterion",

        "gini"

    )


with col2:

    st.metric(

        "Max Depth",

        "5"

    )


with col3:

    st.metric(

        "Random State",

        "42"

    )



st.success("""

### About Decision Tree


Decision Tree is a supervised

Machine Learning algorithm

used for classification tasks.


The algorithm creates

a tree-like structure

where:


• Nodes represent decisions


• Branches represent rules


• Leaf nodes represent

the prediction result


This model is:


✅ Easy to Understand


✅ Fast for Prediction


✅ Suitable for Classification


✅ Easy to Visualize


✅ Highly Interpretable

""")


st.markdown("---")


st.caption(

"🌳 Smart Grid Stability Dashboard | Decision Tree Classification | 2026"

)