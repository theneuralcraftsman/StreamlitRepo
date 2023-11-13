import tensorflow as tf
import streamlit as st

model = tf.keras.models.load_model("D:/DeepLearningModels/Streamlit/basiclinearmodel")


st.title("Number predictor :one:")

input_num = st.number_input('Input number: ')


def predict():
    output = model.predict([input_num])
    st.success(f"The predicted number is: {output[0][0]:.2f}")
    

st.button('Predict', on_click=predict)



