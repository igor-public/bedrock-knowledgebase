import streamlit as st 
import rag_kb_backend as backEnd_RagBedRock

st.set_page_config(page_title="Italian Office Doc") 

new_title = '<p style="font-family:sans-serif; color:white; font-size: 30px;">Italian Office PDF Q&A </p>'
st.markdown(new_title, unsafe_allow_html=True)

input_text = st.text_area("Input text", label_visibility="collapsed") 
go_button = st.button("start", type="primary")


if go_button:  
     with st.spinner("Running"):
         response_content = backEnd_RagBedRock.getBedrockReponseThroughAPI(input_text) 
         st.write(response_content) 