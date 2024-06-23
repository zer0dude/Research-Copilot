import streamlit as st
from blocks.sidebar import get_sidebar
from blocks.text_input import get_text_input
from blocks.visualizations.relevant_topics.topics import get_relevant_topics
from blocks.visualizations.final_papers_list.papers_list import get_papers_list
from blocks.visualizations.final_papers_list.summary_papers import get_summary_all_papers
from blocks.visualizations.chatbot.chat_cohere import chatbot_page

st.set_page_config(layout="wide")

def page_research():
    st.title('Research Assistant!')
    get_text_input()
    
    
    col1, col2 = st.columns([0.4, 0.6])
    with col1:
        get_relevant_topics()
    with col2:
        get_papers_list()
    
    get_summary_all_papers()



def main():
    

    get_sidebar()

    pg = st.navigation([st.Page(page_research, title='Find Papers'), st.Page(chatbot_page, title='ChatBot')])
    pg.run()
    

if __name__ == "__main__":
    main()