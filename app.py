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
    # # Version with Logo
    # # Display brand name or logo
    # col1, col2 = st.columns([0.1, 0.9])
    # with col1:
    #     st.image("media/logo.png", width=50)  # Replace with the path to your logo image
    # with col2:
    #     st.markdown("<h1 style='text-align: left;'>OctoMind</h1>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: left;'>OctoMind</h1>", unsafe_allow_html=True)

    st.markdown("<h2>Hi! I am Octo 🐙 your personal research assistant!</h2>", unsafe_allow_html=True)
    st.write("I can help you understand any research topic and find relevant papers that may interest you! I'll also provide you with summaries of those papers and allow you to communicate with your papers. Just type in a few keywords and I'll do the rest!")
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
    pg = st.navigation([st.Page(page_research, title='Find your relevant Sources!'), st.Page(chatbot_page, title='Chat with your Sources!')])
    pg.run()

if __name__ == "__main__":
    main()