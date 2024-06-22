import streamlit as st
#from agents.gemini_agent import gemini_agent
from blocks.calculations.get_keywords.initial_search import get_keywords
def update_session_state(topics):
    st.session_state['relevant_topics'] = '\n'.join(topics) + '\n'

def get_relevant_topics():
    
    if 'submit_button' in st.session_state or 'relevant_topics' in st.session_state:
        

        if st.session_state['submit_button'] or 'relevant_topics' in st.session_state:
            if st.session_state['submit_button']:
                # drop relevant topics
                st.session_state.pop('relevant_topics', None)
                st.session_state.pop('papers', None)
                
            
                
            
            #with st.container(border=True):
                
            with st.form(key='form_topics'):
                st.subheader('Relevant Topics')
                if 'relevant_topics' not in st.session_state:
                
                    topic_search = get_keywords(st.session_state['text_input']).replace('- ', '')
                else:
                    topic_search = st.session_state['relevant_topics']
                topics_relevant = topic_search.split('\n')[:-1]
                st.write('Here are some relevant topics for your paper:')
                topics=[]
                for i, topic in enumerate(topics_relevant):
                    topics.append(st.text_input('Input for topic',topic, label_visibility='hidden'))

                st.form_submit_button(label='Submit Topics', on_click=lambda: update_session_state(topics))
                
                    

                #st.write(st.session_state['relevant_topics'])