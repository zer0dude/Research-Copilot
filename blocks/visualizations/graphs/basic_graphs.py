import streamlit as st
from collections import Counter
import matplotlib.pyplot as plt
from blocks.calculations.research_papers.get_papers import get_papers_topics

def get_basic_graphs():
    if 'relevant_topics' in st.session_state:
        topics_relevant = st.session_state['relevant_topics'].split('\n')[:-1]

        if 'papers' not in st.session_state:
            papers = get_papers_topics(topics_relevant)
            st.session_state['papers'] = papers
        else:
            papers = st.session_state['papers']
        
        # histogram of papers by year
        with st.container(border=True):
            st.subheader('Histogram of Papers by Publishing Year')

            # Initialize an empty list for years and a counter for invalid papers
            years = []
            invalid_papers_count = 0
            
            # Loop through each paper
            for paper in papers:
                try:
                    # Attempt to extract the year from the BibTeX citation style
                    year_str = paper['citationStyles']['bibtex'].split('year = {')[1].split('}')[0]
                    # Convert the extracted year to an integer and append to the list
                    years.append(year_str)
                except (IndexError, ValueError):
                    # Increment the counter for invalid papers if an error occurs
                    invalid_papers_count += 1
            
            # Convert years to integers and sort
            years_int = [int(year) for year in years if year.isdigit()]
            min_year, max_year = min(years_int), max(years_int)
            
            # Create a list of all years in the range, to ensure gaps are filled
            all_years = list(range(min_year, max_year + 1))
            
            # Count the papers per year, including years with 0 papers
            paper_counts_per_year = Counter(years_int)
            counts = [paper_counts_per_year.get(year, 0) for year in all_years]
            
            # Create a horizontal histogram using Matplotlib for valid years, ensuring years are in descending order
            plt.figure(figsize=(10, 8))  # Set the figure size
            plt.barh(all_years, counts, color='skyblue', edgecolor='black')
            plt.title("Histogram of Papers by Publishing Year")
            plt.xlabel("Number of Papers")
            plt.ylabel("Year")
            plt.tight_layout()  # Adjust the layout to make room for the labels
            
            # Display the histogram in Streamlit
            st.pyplot(plt)
            
            # Display the count of invalid papers using st.write
            if invalid_papers_count > 0:
                st.write(f"Number of papers without a clearly identified year: {invalid_papers_count}")
            

        # histogram of authors
        with st.container(border=True):
            st.subheader('Histogram of Authors')
            
            # Initialize an empty list for author names
            author_names = []
            
            # Loop through each paper
            for paper in papers:
                # Loop through each author in the current paper
                for author in paper['authors']:
                    # Append the author's name to the list
                    author_names.append(author['name'])
            
            # Count the occurrences of each author's name to determine the number of papers per author
            author_counts = Counter(author_names)
            authors, counts = zip(*author_counts.items())  # Unzip the items into two lists
            
            # Calculate dynamic figure height: 0.5 inches per author
            figure_height = max(10, len(authors) * 0.1)  # Ensure a minimum height of 10 inches

            plt.figure(figsize=(10, figure_height))  # Dynamically set the figure size
            plt.barh(authors, counts, color='skyblue', edgecolor='black')
            plt.title("Histogram of Papers by Authors")
            plt.xlabel("Number of Papers")
            plt.ylabel("Author")
            plt.xticks(rotation=90)  # Rotate the x-axis labels to prevent overlap
            plt.tight_layout()  # Adjust the layout to make room for the labels

            # Display the histogram in Streamlit
            st.pyplot(plt)


        # histogram of number of authors
        with st.container(border=True):
            st.subheader('Histogram of Number of Authors')
            
            # Initialize an empty list for the number of authors per paper
            num_authors = []
            
            # Loop through each paper
            for paper in papers:
                # Append the number of authors in the current paper to the list
                num_authors.append(len(paper['authors']))
            
            # Count the occurrences of each number of authors to determine the number of papers per author count
            author_counts = Counter(num_authors)
            author_counts = dict(sorted(author_counts.items()))

            # Create a vertical histogram using Matplotlib for the number of authors
            plt.figure(figsize=(10, 8))
            plt.bar(author_counts.keys(), author_counts.values(), color='skyblue', edgecolor='black')
            plt.title("Histogram of Number of Authors per Paper")
            plt.xlabel("Number of Authors")
            plt.ylabel("Number of Papers")
            plt.tight_layout()

            # Display the histogram in Streamlit
            st.pyplot(plt)

            