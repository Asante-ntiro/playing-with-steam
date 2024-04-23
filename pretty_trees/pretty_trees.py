import streamlit as st
st.title("Bro, we doin it BIG")
st.write(
    """
    Im finn get streamLIT tonight!
    """
)
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")
with col3:
    st.write("Column 3")

