from agents.gemini_agent import gemini_agent

def get_keywords(text):
    prompt= '''
        From the provided text extract, generate detailed keyword phrases for researching related academic papers. Create up to five different keyword phrases in markdown format, each separated by a newline. Return the list only.
    '''
    keywords = gemini_agent(prompt+text)
    return keywords