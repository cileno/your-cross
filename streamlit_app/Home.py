import streamlit as st
import pandas as pd

st.title("YOUR CROSS")
st.write("Bem-vindo ao sistema da academia!")

df = pd.DataFrame({"Nome": ["João", "Ana"], "Idade": [30, 25]})
st.dataframe(df)