import streamlit as st
#from agents.gemini_agent import gemini_agent
from blocks.calculations.get_keywords.initial_search import get_keywords

def get_relevant_topics():
    if 'submit_button' in st.session_state:
        if st.session_state['submit_button']:
            with st.container(border=True):
                st.subheader('Relevant Topics')
                st.session_state['relevant_topics'] = get_keywords(st.session_state['text_input'])
                st.write('Here are some relevant topics for your paper:')
                st.write(st.session_state['relevant_topics'])