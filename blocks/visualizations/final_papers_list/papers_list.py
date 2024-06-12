import streamlit as st
from blocks.calculations.research_papers.get_papers import get_papers_topics

def get_papers_list():
    if 'relevant_topics' in st.session_state:
        topics_relevant = st.session_state['relevant_topics'].split('\n')[:-1]
        papers = get_papers_topics(topics_relevant)
        st.session_state['papers'] = papers
        
        with st.container(border=True):
            st.subheader('Bibliography')
            for paper in papers:
                st.write(paper['title'])