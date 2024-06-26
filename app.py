import streamlit as st
from blocks.sidebar import get_sidebar
from blocks.text_input import get_text_input
from blocks.visualizations.relevant_topics.topics import get_relevant_topics
from blocks.visualizations.final_papers_list.papers_list import get_papers_list
from blocks.visualizations.final_papers_list.summary_papers import get_summary_all_papers
from blocks.visualizations.graphs.basic_graphs import get_basic_graphs
from blocks.visualizations.graphs.wordcloud import get_wordcloud
from blocks.visualizations.graphs.network_graphs import get_network_graphs
from blocks.visualizations.chatbot.chat_cohere import chatbot_page

st.set_page_config(layout="wide")


def page_research():
    st.title('Hi!')
    st.write("I'm your personal research assistant. I can help you find relevant papers on a topic of your choice. I'll also provide you with summaries of those papers and allow you to communicate with your papers. Just type in a few keywords and I'll do the rest!")
    get_text_input()
    
    
    col1, col2 = st.columns([0.4, 0.6])
    with col1:
        get_relevant_topics()
    with col2:
        get_papers_list()
    
    get_summary_all_papers()
    get_basic_graphs()
    get_wordcloud()
    get_network_graphs()




def main():
    

    get_sidebar()

    pg = st.navigation([st.Page(page_research, title='Find Papers'), st.Page(chatbot_page, title='ChatBot')])
    pg.run()


if __name__ == "__main__":
    main()