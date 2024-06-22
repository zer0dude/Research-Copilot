from papers_api.scholar_api import get_papers
import time

def get_papers_topics(topics):
    papers = []

    for i, topic in enumerate(topics):
        topics = [topic for topic in topics if topic is not None]
        papers_found = get_papers(topic)
        if papers_found:
            papers.extend(papers_found)
        if i != len(topics) - 1:  # if it's not the last iteration
            time.sleep(1.01)
    # Remove duplicates based on a unique key, e.g., 'paper_id'
    unique_papers = []
    seen_ids = set()
    for paper in papers:
        if paper['paperId'] not in seen_ids:
            unique_papers.append(paper)
            seen_ids.add(paper['paperId'])

    return unique_papers
