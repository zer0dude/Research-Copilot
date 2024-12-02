import streamlit as st
from agents.gemini_agent import gemini_agent
import os
import time

def save_summary_to_file(summary, filename='summary.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(summary)

def load_summary_from_file(filename='summary.txt'):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    return None

def get_summary_all_papers():
    if 'papers' in st.session_state:
        
        # Load summary from file if it exists
        summary = load_summary_from_file()
        if summary:
            st.session_state['summary'] = summary
        else:
            prompt = '''
                Provide a summary of all the papers in the list.  In Markdown style:
            '''
            list_abstracts = ' Next Paper:'.join([f"Title: {paper['title']} Abstract: {paper['abstract']}" for paper in st.session_state['papers']])
            summary = gemini_agent(prompt + list_abstracts)
            st.session_state['summary'] = summary
            
            # Save summary to file
            save_summary_to_file(summary)
            
            # Add a delay to mimic processing time
            time.sleep(5)

        if 'summary' in st.session_state:
            with st.container(border=True):
                st.subheader('Summary of All Papers')
                st.markdown(st.session_state['summary'])
