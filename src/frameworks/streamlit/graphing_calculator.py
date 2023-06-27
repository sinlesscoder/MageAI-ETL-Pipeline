import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Supresses the matplotlib warning
st.set_option('deprecation.showPyplotGlobalUse', False)

# Title for Web Page
st.markdown("<h1 style='text-align:center'> Graphing Calculator </h1>", unsafe_allow_html=True)

# Create a text area that has an equation
equation = st.text_area("Write in an equation with respect to x: ", placeholder='x**2')

# Numerical input
start = st.number_input("Number to start the domain with: ", min_value=-1000000000, max_value=1000000000, value=-10)
end = st.number_input("Number to end the domain with: ", min_value=-1000000000, max_value=1000000000, value=10)

# Create a color picker
graph_color = st.color_picker(label="Choose a color for the graph: ")

# Graph function
def graph(equation: str, start, end, color):
    # Vector called x
    x = np.linspace(start, end, num=200)

    # Create the y vector
    y = eval(equation)

    # Matplotlib visual
    plt.figure(figsize=(10,10))
    plt.text(0, 2.0, f"y={equation}", size=16)
    plt.plot(x, y, color=color)

    st.pyplot()

if st.button("Graph"):
    graph(equation, start, end, graph_color)