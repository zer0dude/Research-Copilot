import streamlit as st
from blocks.calculations.rag_papers.get_pdf import rag_chat, read_pdfs_from_urls

def chatbot_page():
    st.title("Chat with the Papers")
    
    #print(st.session_state['folder'])
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    if 'citations' not in st.session_state:
        st.session_state['citations'] = []

    if 'text_papers' not in st.session_state:
        try:
            print('finding papers')
            st.session_state['text_papers'] = read_pdfs_from_urls(st.session_state['papers'])
        except:
            st.session_state['text_papers']=None
            st.write("Papers not found")
    
    if st.session_state['text_papers'] is None:
        try:
            print('finding papers')
            st.session_state['text_papers'] = read_pdfs_from_urls(st.session_state['papers'])
        except:
            st.session_state['text_papers']=None
            st.write("Papers not found")

    #print(st.session_state[st.session_state['folder']])
    # Display chat messages from history on app rerun
    for i, message in enumerate(st.session_state.chat_history):
        with st.chat_message(message.role.replace('CHATBOT', 'assistant')):
            #print(i)
            #print(len(st.session_state['citations']))
            st.markdown(message.message)
            if message.role == 'CHATBOT':
                with st.popover("Citations"):
                    st.write(st.session_state['citations'][i])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        st.session_state['citations'].append([])
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        answer = rag_chat(prompt, st.session_state['text_papers'])
        response = f"{answer.text}"
        #print(answer.citations)
        st.session_state['citations'].append(answer.citations)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
            with st.popover("Citations"):
                st.write(answer.citations)
    
