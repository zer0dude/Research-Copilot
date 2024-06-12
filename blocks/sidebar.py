import streamlit as st

def get_sidebar():
    with st.sidebar:
        st.subheader('Model Selection')
        col1, col2 = st.columns(2)
        with col1:
            st.button('Model 1')
        with col2:
            st.button('Model 2')
        
        source = st.radio('Sources', ['Source 1', 'Source 2', 'Source 3', 'Source 4'])
        
    
