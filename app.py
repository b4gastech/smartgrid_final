import streamlit as st
import pandas as pd
import joblib

model = joblib.load("decision_tree_model.pkl")

st.title("Smart Grid Stability Prediction")

tau1 = st.number_input("tau1")
tau2 = st.number_input("tau2")
tau3 = st.number_input("tau3")
tau4 = st.number_input("tau4")

p1 = st.number_input("p1")
p2 = st.number_input("p2")
p3 = st.number_input("p3")
p4 = st.number_input("p4")

g1 = st.number_input("g1")
g2 = st.number_input("g2")
g3 = st.number_input("g3")
g4 = st.number_input("g4")

if st.button("Prediksi"):

    data = pd.DataFrame([[tau1,tau2,tau3,tau4,
                          p1,p2,p3,p4,
                          g1,g2,g3,g4]],
                        columns=[
                            'tau1','tau2','tau3','tau4',
                            'p1','p2','p3','p4',
                            'g1','g2','g3','g4'
                        ])

    hasil = model.predict(data)

    if hasil[0] == 1:
        st.success("UNSTABLE")
    else:
        st.success("STABLE")