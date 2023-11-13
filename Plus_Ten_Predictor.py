import tensorflow as tf
import streamlit as st
import pickle

# model = tf.keras.models.load_model("D:/DeepLearningModels/Streamlit/linearModel.h5")
# pickle.dump(model, open('D:/DeepLearningModels/Streamlit/model2','wb'))

model = pickle.load(open('model2','rb'))

st.title("Number predictor :one:")

input_num = st.number_input('Input number: ')


def predict():
    output = model.predict([input_num])
    st.success(f"The predicted number is: {output[0][0]:.2f}")
    

st.button('Predict', on_click=predict)



