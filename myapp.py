import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Cats")

col1, col2 = st.columns(2)
with col1:
  st.subheader("agent")
  st.image("./image.jpg", caption="Persian Cat", width=300,use_column_width=True)
  st.write("Persian cats are cute")
with col2:
  st.subheader("mango")
  st.image("./8.jpg", caption="Ragdoll Cat", width=300,use_column_width=True)
  st.write("Ragdoll cats are proud")
