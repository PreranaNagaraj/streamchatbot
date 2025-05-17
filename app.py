
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os
os.environ["GOOGLE_API_KEY"]=st.secrets["GOOGLE_API_KEY"]
import streamlit as st
# Initialize the chat model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful assistant.")
    ]

# Set up the Streamlit UI
st.title("LangChain Chat with Gemini Flash")

# Display previous messages
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# Get user input
user_input = st.chat_input("Your message:")

# Process user input
if user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get response from the model
    result = llm.invoke(st.session_state.chat_history)
    ai_response = result.content
    
    st.session_state.chat_history.append(AIMessage(content=ai_response))
    
    # Display the response
    with st.chat_message("assistant"):
        st.write(ai_response)
    
    # Clear input (optional -  clears the input box after sending)
    #st.session_input(value="") # Removed st.session_input, use st.chat_input without value.

# Add a quit mechanism (optional -  for stopping the chat via a button)
if st.button("End Chat"):
    st.stop()
    
# Run the app:
# streamlit run your_script_name.py  (replace your_script_name.py)
