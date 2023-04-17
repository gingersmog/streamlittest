import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)


edited_df = st.experimental_data_editor(df, num_rows="dynamic")


st.dataframe(edited_df)

st.write('Hello, *World!* :sunglasses:')
st.write(1234)