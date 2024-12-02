import streamlit as st
from pyvis.network import Network
from blocks.calculations.research_papers.get_papers import get_papers_topics
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

            # Add manual edges
            paper_ids = [paper['paperId'] for paper in papers]
            
            # Paper 0 has a node connecting it to papers 1-25
            for target_id in paper_ids[1:25]:
                net.add_edge(paper_ids[0], target_id, color='lightblue')
            
            # Paper 1 has a connection to papers 18-30
            for target_id in paper_ids[18:33]:
                net.add_edge(paper_ids[1], target_id, color='lightblue')

            # Edges betwween cluster 0 and 1
            net.add_edge(paper_ids[18], paper_ids[19], color='lightblue')
            net.add_edge(paper_ids[18], paper_ids[20], color='lightblue')   
            net.add_edge(paper_ids[21], paper_ids[22], color='lightblue')

            # Papers 36, 37, 38 each have a connection to each other
            net.add_edge(paper_ids[36], paper_ids[37], color='lightblue')
            net.add_edge(paper_ids[36], paper_ids[38], color='lightblue')
            net.add_edge(paper_ids[37], paper_ids[38], color='lightblue')

            # Adjust physics settings to decrease edge pull strength
            net.barnes_hut(gravity=-2500)

            # Generate the network HTML directly
            network_html = net.generate_html()

            # Display the network in Streamlit using the HTML content
            st.components.v1.html(network_html, height=700, width=750)