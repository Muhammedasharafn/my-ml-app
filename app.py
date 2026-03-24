import streamlit as st
import pickle
import numpy as np

# Load the saved model
model = pickle.load(open("model.pkl", "rb"))
class_names = ["Setosa", "Versicolor", "Virginica"]

# App Title
st.title("🌸 Iris Flower Predictor 🌸")
st.write("Move the sliders and click Predict!")

# Input sliders
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
sepal_width  = st.slider("Sepal Width (cm)",  2.0, 5.0, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width  = st.slider("Petal Width (cm)",  0.1, 2.5, 1.0)

# Predict button
if st.button("Predict 🔍"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)[0]
    st.success(f"✅ Predicted Flower: **{class_names[prediction]}**")