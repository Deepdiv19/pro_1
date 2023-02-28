import streamlit as st
import streamlit as st
code = '''hello datascience 2023'''
st.code(code, language = 'python')
BUTTON_CLICK = st.button("click me")
st.write(BUTTON_CLICK)
st.balloons()

if BUTTON_CLICK == True:
    st.subheader("uyou ckikk : emojis")
    st.balloons()

