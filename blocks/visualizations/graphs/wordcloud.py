import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from blocks.calculations.research_papers.get_papers import get_papers_topics

def get_wordcloud():
    if 'relevant_topics' in st.session_state:
        topics_relevant = st.session_state['relevant_topics'].split('\n')[:-1]

        if 'papers' not in st.session_state:
            papers = get_papers_topics(topics_relevant)
            st.session_state['papers'] = papers
        else:
            papers = st.session_state['papers']

        # wordcloud of abstracts
        with st.container(border=True):
            st.subheader('Wordcloud of Abstracts')

            # Initialize an empty list for abstracts
            abstracts = []

            # Loop through each paper
            for paper in papers:
                try:
                    abstract = paper['abstract']
                    # Check if the abstract is None and handle it by appending an empty string
                    if abstract is None:
                        abstracts.append('')
                    else:
                        abstracts.append(abstract)
                except (IndexError, ValueError):
                    abstracts.append('')            

            # Join all abstracts into a single string
            text = ' '.join(abstracts)

            # Generate the word cloud
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

            # Display the word cloud using Matplotlib
            plt.figure(figsize=(10, 8))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            # plt.title("Wordcloud of Abstracts")
            plt.tight_layout()

            st.pyplot(plt)

