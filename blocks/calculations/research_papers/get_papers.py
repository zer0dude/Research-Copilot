from papers_api.scholar_api import get_papers
import time

def get_papers_topics(topics):
    papers = []

    for i, topic in enumerate(topics):
        papers_found = get_papers(topic)
        print(topic)
        print(papers_found)
        papers.extend(papers_found)
        if i != len(topics) - 1:  # if it's not the last iteration
            time.sleep(1.01)
    papers=list(set(papers))
    return papers
