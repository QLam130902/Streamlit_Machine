import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
st.title("Streamlit Menu")
st.write("Lê Quốc Việt - 20110600")
st.write("Đỗ Quang Lâm - 20110512")
st.sidebar.success("Select a demo above.")

st.markdown(
"""
    Select a demo about !
"""
)
