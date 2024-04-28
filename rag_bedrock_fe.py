import streamlit as st 
import rag_backend as B_E

st.set_page_config(page_title="National Office Doc") 

new_title = '<p style="font-family:sans-serif; color:white; font-size: 30px;">National Office PDF Q&A </p>'
st.markdown(new_title, unsafe_allow_html=True)

if 'vector_index' not in st.session_state: 
    with st.spinner("📀 loading ... "):
        st.session_state.vector_index = B_E.no_pdf_index()

input_text = st.text_area("Input text", label_visibility="collapsed") 
go_button = st.button("start", type="primary")

if go_button:  
    with st.spinner("Running"):
        response_content = B_E.no_pdf_rag_response(index=st.session_state.vector_index, question=input_text) 
        st.write(response_content) 