## Introduction to Streamlit

### Description

- `streamlit` is a Python module that allows an end user to make web applications solely with Python.

- It uses a backend web server known as `uvicorn` in order to host components that are rendered as a single page. In software engineering, this is referred to as a `SPA` or a single page application.

- The actual components (e.g. HTML, CSS, JavaScript) is all handled using a templating mechanism in Python known as `jinja2`. They use a front-end framework to dynamically render the content (e.g. React, Vue, Angular).

### Apps

- Social Profile Page
- Graphing Calculator

### Installation

- Install `streamlit` via `pip`

```bash
pip install streamlit
```

### Basic Usage

```python
import streamlit as st

# Create a title of the page
st.title("Hello World!")
```

### Run the Streamlit Server

- As soon as `streamlit` has been installed, you can literally create a server from the command line.

- Replace `app.py` with the name of your file that you want to show on the browser.

```bash
streamlit run app.py
```
