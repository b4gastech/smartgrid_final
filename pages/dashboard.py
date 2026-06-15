import streamlit as st
import pandas as pd

st.title("📊 Dashboard")


st.markdown("""

Welcome to Smart Grid Stability Dashboard.


This application predicts

whether Smart Grid is

Stable or Unstable

using Decision Tree.

""")


st.markdown("---")


col1,col2=st.columns(2)


with col1:

    st.info("""

### Dataset Information


Dataset :

Smart Grid Stability


Records :

60000


Features :

12


Target :

stabf

""")


with col2:


    st.success("""

### Prediction Classes


🟢 Stable


System operates normally.



🔴 Unstable


System needs monitoring.

""")



st.markdown("---")


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