from papers_api.scholar_api import get_papers
import time
from pybtex.database.input import bibtex
from pybtex.plugin import find_plugin
from pybtex.database import BibliographyData
from pybtex.database.output import bibtex as bibtex_output
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

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



def bibtex_to_apa(bibtex_str, url=None):
    def format_apa(entry, url=None):
        authors = entry.get('author', '').replace(' and ', ', ')
        title = entry.get('title', '')
        year = entry.get('year', '')
        journal = entry.get('journal', '')
        volume = entry.get('volume', '')
        number = entry.get('number', '')
        pages = entry.get('pages', '')
        publisher = entry.get('publisher', '')
        
        if entry['ENTRYTYPE'] == 'article':
            apa_entry = f"{authors} ({year}). {title}. *{journal}*, {volume}({number}), {pages}."
        elif entry['ENTRYTYPE'] == 'book':
            apa_entry = f"{authors} ({year}). *{title}*. {publisher}."
        else:
            apa_entry = f"{authors} ({year}). {title}."
        
        if url:
            apa_entry += f" [Available online](<{url}>)"
        
        return apa_entry

    parser = BibTexParser()
    parser.customization = convert_to_unicode
    bib_database = bibtexparser.loads(bibtex_str, parser=parser)
    
    apa_entries = [format_apa(entry, url) for entry in bib_database.entries]
    return '\n'.join(apa_entries)