import streamlit as st 
import rag_backend as FE

st.set_page_config(page_title="National Office Doc") 

new_title = '<p style="font-family:sans-serif; color:white; font-size: 30px;">Nantional Office PDF test-chats </p>'
st.markdown(new_title, unsafe_allow_html=True)

if 'vector_index' not in st.session_state: 
    with st.spinner("📀 loading ... "):
        st.session_state.vector_index = FE.no_pdf_index()

input_text = st.text_area("Input text", label_visibility="collapsed") 
go_button = st.button("start", type="primary")

if go_button: 
    
    with st.spinner("Running"):
        response_content = FE.no_pdf_rag_response(index=st.session_state.vector_index, question=input_text) ### replace with RAG Function from backend file
        st.write(response_content) 