import streamlit as st
from pyvis.network import Network
from blocks.calculations.research_papers.get_papers import get_papers_topics

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

            # Add nodes and edges
            for paper in papers:
                paper_id = paper['paperId']
                paper_title = paper.get('title', 'No Title')
                net.add_node(paper_id, label=paper_title, title=paper_title)
                # Iterate through citations if they exist
                for citation in paper.get('citations', []):
                    cited_paper_id = citation.get('paperId')
                    # Ensure both the citing and cited papers are in the dataset and have been added as nodes
                    if cited_paper_id in [p['paperId'] for p in papers]:
                        # Check if both nodes exist in the network before adding an edge
                        if paper_id in net.get_nodes() and cited_paper_id in net.get_nodes():
                            net.add_edge(paper_id, cited_paper_id, color='lightblue')

            # Generate the network HTML directly
            network_html = net.generate_html()

            # Display the network in Streamlit using the HTML content
            st.components.v1.html(network_html, height=800, width=800)