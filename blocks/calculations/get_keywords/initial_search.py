from agents.gemini_agent import gemini_agent

def get_keywords(text):
    prompt= '''
        From the following text extract keywords for a query research of papers linked to the topic, up to 5 different keywords in mardown format. Return only the keywords separated by a new line:
    '''
    keywords = gemini_agent(prompt+text)
    return keywords