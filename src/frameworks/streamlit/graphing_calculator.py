import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Supresses the matplotlib warning
st.set_option('deprecation.showPyplotGlobalUse', False)

# Title for Web Page
st.markdown("<h1 style='text-align:center'> Graphing Calculator </h1>", unsafe_allow_html=True)

# Create a text area that has an equation
equation = st.text_area("Write in an equation with respect to x: ", placeholder='x**2')

# Graph function
def graph(equation: str):
    # Vector called x
    x = np.linspace(-10, 10, num=200)

    # Create the y vector
    y = eval(equation)

    # Matplotlib visual
    plt.figure(figsize=(10,10))

    plt.plot(x, y)

    st.pyplot()

if st.button("Graph"):
    graph(equation)