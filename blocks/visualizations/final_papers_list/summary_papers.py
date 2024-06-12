import streamlit as st
from agents.gemini_agent import gemini_agent

def get_summary_all_papers():
    if 'papers' in st.session_state:
        prompt = '''
            Provide a summary of all the papers in the list. In Markdown style:
        '''
        list_abstracts = ' Next Paper:'.join([str(paper['abstract']) for paper in st.session_state['papers']])
        summary = gemini_agent(prompt+list_abstracts)
        st.session_state['summary'] = summary
        if 'summary' in st.session_state:
            with st.container(border=True):
                st.subheader('Summary of All Papers')
                st.markdown(summary)