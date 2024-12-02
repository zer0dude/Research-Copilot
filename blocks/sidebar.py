import streamlit as st

def get_sidebar():
    with st.sidebar:
        st.subheader('Model Selection')
        
        # 3rd Party Models
        st.markdown("### 3rd Party Models")
        third_party_models = []
        if st.checkbox('GPT-4o', value=True):
            third_party_models.append('GPT-4o')
        if st.checkbox('Gemini 1.5 Flash'):
            third_party_models.append('Gemini 1.5 Flash')
        if st.checkbox('Claude'):
            third_party_models.append('Claude')
        
        # OctoMind Models
        st.markdown("### OctoMind Models")
        octomind_models = []
        if st.checkbox('Octo 1'):
            octomind_models.append('Octo 1')
        
        # Local Models
        st.markdown("### Local Models")
        local_models = []
        if st.checkbox('Local Reef 1.2'):
            local_models.append('Local Reef 1.2')
        
        # Sources
        st.markdown("### Sources")
        sources = []
        if st.checkbox('Semantic Scholar', value=True):
            sources.append('Semantic Scholar')
        if st.checkbox('arXiv'):
            sources.append('arXiv')
        if st.checkbox('Elsevier'):
            sources.append('Elsevier')
        if st.checkbox('IEEE Xplore'):
            sources.append('IEEE Xplore')
        if st.checkbox('Local Data'):
            sources.append('Local Data: Internal Report and Data on Remote Work')
        if st.checkbox('Think Tank Internal Database'):
            sources.append('Think Tank Internal Database')
        
        # Button to connect further sources
        st.markdown("### Connect further Sources!")
        if st.button("Add Source"):
            pass  # Button does not need to do anything