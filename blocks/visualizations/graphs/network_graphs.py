import streamlit as st
from pyvis.network import Network
from blocks.calculations.research_papers.get_papers import get_papers_topics
import random
import numpy as np

def get_network_graphs():
    if 'relevant_topics' in st.session_state:
        topics_relevant = st.session_state['relevant_topics'].split('\n')[:-1]

        if 'papers' not in st.session_state:
            papers = get_papers_topics(topics_relevant)
            st.session_state['papers'] = papers
        else:
            papers = st.session_state['papers']

        # Citation Network
        with st.container(border=True):
            st.subheader('Citation Network')

            # Initialize the network graph
            net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

            # Add nodes
            for paper in papers:
                paper_id = paper['paperId']
                paper_title = paper.get('title', 'No Title')
                net.add_node(paper_id, label=paper_title, title=paper_title)

            # Add random edges
            paper_ids = [paper['paperId'] for paper in papers]
            for paper in papers:
                paper_id = paper['paperId']
                num_connections = int(np.random.normal(loc=3, scale=3))  # Normal distribution with mean=10, std=5
                num_connections = max(1, min(num_connections, 10))  # Ensure the number of connections is between 1 and 20
                targets = random.sample(paper_ids, num_connections)
                for target_id in targets:
                    if paper_id != target_id:  # Avoid self-loops
                        net.add_edge(paper_id, target_id, color='lightblue')

            # Generate the network HTML directly
            network_html = net.generate_html()

            # Display the network in Streamlit using the HTML content
            st.components.v1.html(network_html, height=800, width=800)