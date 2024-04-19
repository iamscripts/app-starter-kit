import streamlit as st
from langchain.llms import OpenAI

st.title('Quickstart Test Automation App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

# Initialize OpenAI instance outside the function, after key validation
if openai_api_key.startswith('sk-'):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
else:
    llm = None

def generate_response(input_text):
    if llm is not None:
        try:
            # Call the LLM and display the result
            response = llm(input_text)
            st.info(response)
        except Exception as e:
            # Handle other exceptions that may occur
            st.error(f"An error occurred: {str(e)}")
    else:
        st.error("Invalid API key. Please enter a valid OpenAI API key.")

with st.form('my_form'):
    text = st.text_area('Enter text:', 'Give me a use case and ask for test cases')
    submitted = st.form_submit_button('Submit')

    if submitted:
        if not openai_api_key:
            st.warning('Please enter your OpenAI API key!', icon='⚠️')
        else:
            generate_response(text)