import streamlit as st
from blocks.calculations.research_papers.get_papers import get_papers_topics, bibtex_to_apa
import json
import os
import time


def save_papers_to_json(papers, filename='papers.json'):
    with open(filename, 'w') as f:
        json.dump(papers, f, indent=4)

def load_papers_from_json(filename='papers.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return None

def get_papers_list():
    if 'relevant_topics' in st.session_state:
        topics_relevant = st.session_state['relevant_topics'].split('\n')[:-1]

        if 'papers' not in st.session_state:
            papers = load_papers_from_json()
            if not papers:
                papers = get_papers_topics(topics_relevant)
                st.session_state['papers'] = papers
                # Save papers to JSON file
                save_papers_to_json(papers)
            else:
                st.session_state['papers'] = papers
        else:
            papers = st.session_state['papers']

        # Add a delay to mimic processing time
        time.sleep(1)
        
        with st.container(border=True):
            st.subheader('Bibliography')
            for paper in papers:
                st.markdown(bibtex_to_apa(paper['citationStyles']['bibtex'], url=paper['url']))