import requests
import PyPDF2
import io
import cohere
import os
import streamlit as st
from PyPDF2 import PdfReader

def get_pdf(url):
    # Initialize an empty string to hold all the text
    all_text = ""

    # Fetch the PDF content from the URL
    response = requests.get(url)

    # Ensure the request was successful
    if response.status_code == 200:
        # Create a BytesIO object from the binary content of the PDF
        pdf_bytes = io.BytesIO(response.content)
        
        # Use PyPDF2 to read the PDF from bytes
        pdf = PyPDF2.PdfReader(pdf_bytes)
        
        # Iterate through each page of the PDF
        for page_num in range(len(pdf.pages)):
            # Get a page
            page = pdf.pages[page_num]
            
            # Extract text from the page
            text = page.extract_text()
            
            # Append the text of each page to the all_text string
            if text:  # Check if text extraction was successful
                all_text += text + "\n"  # Add a newline character to separate pages
            else:
                all_text += "Could not extract text from page.\n"
    else:
        print("Failed to fetch the PDF.")
        return None

    # Return the text
    return all_text




try:
    path="COHERE_KEY.txt"
    os.environ["COHERE_KEY"] = open(path, 'r').read()
except:
    print("Please set the GITHUB_KEY environment variable.")

co = cohere.Client(api_key=os.environ["COHERE_KEY"])
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

def rag_chat(message, documents=None):
    try:
        results_rerank = co.rerank(query=message, documents=documents, top_n=10, model='rerank-english-v3.0')
        results_docs = [documents[result.index] for result in results_rerank.results]
    except:
        results_docs = None
        print('No documents')
    #print(results_rerank)
    
    #print(results_docs)
    answer=co.chat(
        model="command-r",
        message=message,
        documents=results_docs,
        chat_history=st.session_state['chat_history'],
        prompt_truncation='AUTO_PRESERVE_ORDER',
        #connectors=[{"id": "web-search"}],
        citation_quality='accurate'
    )
    
    st.session_state['chat_history'] = answer.chat_history
    #print(answer)
    return answer



def read_pdfs_from_urls(pdf_urls):
    """
    Reads PDF files from the specified URLs and returns their content in a list of dictionaries.
    Splits the text into chunks at sentence boundaries, aiming for chunks of up to 300 words without breaking sentences.

    Parameters:
    - pdf_urls: A list of dictionaries, each containing a 'url' key that links to a PDF file.

    Returns:
    A list of dictionaries, each containing 'title', 'text', and 'url' keys. 'text' may contain multiple chunks.
    """
    pdf_contents = []  # List to store the content of each PDF

    print(len(pdf_urls))
    for pdf_dict in pdf_urls:
        print('paper')
        print(pdf_dict.keys())
        print(pdf_dict['openAccessPdf'])
        
        try:
            url = pdf_dict['openAccessPdf']['url']
            response = requests.get(url)
            response.raise_for_status()  # Raises HTTPError for bad responses

            with io.BytesIO(response.content) as pdf_file:
                pdf_reader = PdfReader(pdf_file)
                full_text = ""
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if text:  # Ensure there's text to add
                        full_text += text + "\n"
                

                # Split the full text into sentences
                sentences = full_text.split('. ')
                word_count = 0
                chunk = ""
                for sentence in sentences:
                    sentence_word_count = len(sentence.split())
                    # Check if adding this sentence would exceed the 300-word limit
                    if word_count + sentence_word_count > 300:
                        # Append the current chunk to the list and start a new one
                        pdf_contents.append({"title": pdf_dict['title'], "text": chunk.strip(), "url": url})
                        chunk = sentence + ". "
                        word_count = sentence_word_count
                    else:
                        chunk += sentence + ". "
                        word_count += sentence_word_count

                # Don't forget to add the last chunk if it's not empty
                if chunk:
                    pdf_contents.append({"title": pdf_dict['title'], "text": chunk.strip(), "url": url})
        except:

            print(f"Failed to read PDF")
    print(pdf_contents)
    print('Text found')
    return pdf_contents