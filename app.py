import streamlit as st
from openai import OpenAI
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Aadhitya's ChatGPT",
    page_icon="💬",
    layout="wide"
)

# Initialize session state
def init_session_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'api_key' not in st.session_state:
        st.session_state.api_key = ""

# Initialize session state
init_session_state()

# Sidebar for API key input
with st.sidebar:
    st.title("Settings")
    st.session_state.api_key = st.text_input("OpenAI API Key", type="password")
    if st.button("Clear Chat"):
        st.session_state.messages = []

# Main chat interface
st.title("Aadhitya's ChatGPT")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def handle_chat(prompt):
    """Handle chat interaction with OpenAI API"""
    if not st.session_state.api_key:
        st.error("Please enter your OpenAI API key in the settings sidebar")
        return

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat
    with st.chat_message("user"):
        st.write(prompt)

    try:
        # Initialize OpenAI client with the new SDK (>=1.0.0)
        client = OpenAI(api_key=st.session_state.api_key)

        # Get AI response
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                *st.session_state.messages
            ]
        )

        # Extract and display assistant message
        message = response.choices[0].message
        st.session_state.messages.append({"role": "assistant", "content": message.content})

        with st.chat_message("assistant"):
            st.write(message.content)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Handle user input
if prompt := st.chat_input("What would you like to know?"):
    handle_chat(prompt)
