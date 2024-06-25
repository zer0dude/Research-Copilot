import streamlit as st

def get_sidebar():
    with st.sidebar:
        st.subheader('Model Selection')
        col1, col2 = st.columns(2)
        with col1:
            st.button('Gemini 1.5 Flash')
        with col2:
            st.button('GPT-4o')
        
        source = st.radio('Sources', ['Semantic Scholar', 'arXiv', 'Elsevier', 'IEEE Xplore'])
        
    
