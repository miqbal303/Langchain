import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI  # Ensure the correct import
from langchain.prompts import ChatPromptTemplate  # Correct import for ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser  # Correct import for StrOutputParser


# load the environment
load_dotenv()

# Ensure your environment variables are correctly loaded
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')

# Langsmith Tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY

# Creating chatbot with the system message converted to human message
prompt = ChatPromptTemplate.from_messages(
    [
        ("user", "You are a helpfull assistant. Please provide response to the user query. Question: {question}")
    ]
)

# Streamlit
st.title("Langchain Demo with Gemini")
input_text = st.text_input("Search topic")

llm = ChatGoogleGenerativeAI(google_api_key=GOOGLE_API_KEY, model="gemini-pro")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    #Process user input
    user_result = chain.invoke({"question": input_text})
    st.write(" Response to user query")
    st.write(user_result)
