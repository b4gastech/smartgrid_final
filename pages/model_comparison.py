import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

from utils.style import load_css


load_css()


st.title(

"🏆 Model Comparison"

)


data={

"Model":[

"Decision Tree",

"KNN",

"SVM"

],

"Status":[

"READY",

"COMING SOON",

"COMING SOON"

]

}


df=pd.DataFrame(data)


st.dataframe(df)


fig,ax=plt.subplots(

figsize=(5,4)

)


ax.bar(

df["Model"],

[92,0,0]

)


ax.set_title(

"Accuracy"

)


st.pyplot(fig)


st.success(

"🏆 Best Model : Decision Tree"

)