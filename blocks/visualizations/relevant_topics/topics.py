import streamlit as st
from blocks.calculations.get_keywords.initial_search import get_keywords
import time

def update_session_state(topics):
    st.session_state['relevant_topics'] = '\n'.join(topics) + '\n'

def get_relevant_topics():
    if 'submit_button' in st.session_state or 'relevant_topics' in st.session_state:
        if st.session_state['submit_button'] or 'relevant_topics' in st.session_state:
            if st.session_state['submit_button']:
                # drop relevant topics
                st.session_state.pop('relevant_topics', None)
                st.session_state.pop('papers', None)

            with st.form(key='form_topics'):
                st.subheader('Relevant Search Terms')

                # waiting time to mimic llm working to find topics
                time.sleep(2)
                
                # Hardcoded topics
                topics_relevant = [
                    "Remote work productivity",
                    "Remote work, short-term vs. long-term effects",
                    "Remote work: demographic, industry, and geographical variations in productivity",
                    "Work-life balance under remote work",
                    "Organizational strategies for remote work"
                ]
                
                st.write('Here are some relevant search terms for your research:')
                topics = []
                for i, topic in enumerate(topics_relevant):
                    # Adjust the height of the text area based on the length of the topic
                    height = max(1, len(topic) // 50)  # Adjust the divisor to control the height
                    topics.append(st.text_area('Input for topic', topic, height=height, label_visibility='hidden'))

                st.form_submit_button(label='Submit Search Terms', on_click=lambda: update_session_state(topics))