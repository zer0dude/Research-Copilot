import streamlit as st

def get_text_input():
    with st.form(key='my_form'):
        st.session_state['text_input'] = st.text_area('Describe your research interests and I will find the relevant literature for you!')
        st.session_state['submit_button'] = st.form_submit_button(label='Generate')
    