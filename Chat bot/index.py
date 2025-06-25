import streamlit as st
st.header("Abhinand Shaji")
with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload pdf file", type="pdf")