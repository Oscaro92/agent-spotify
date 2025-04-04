import time
import pandas as pd
import streamlit as st
from agent import AgentSpotify

st.title("🎶 Agent Spotify 🎶")
agent = AgentSpotify()

def stream_data(response):
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.05)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Add input file
st.header("Importer votre playlist")
uploaded_file = st.file_uploader("Choisissez un fichier CSV ou Markdown", type=["csv", "md"])

# Traitement du fichier importé
if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1].lower()
    st.success(f"Fichier importé avec succès!")

    if file_extension == "csv":
        df = pd.read_csv(uploaded_file)
        csv_string = df.to_csv(index=False)
        st.session_state.uploaded_data = csv_string


    elif file_extension == "md":
        content = uploaded_file.read().decode("utf-8")
        st.session_state.uploaded_data = content


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if uploaded_file is not None:
    # React to user input
    if prompt := st.chat_input("Que puis-je faire pour toi ? "):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            with st.spinner("Loading response..."):
                response = agent.chat(st.session_state.messages, st.session_state.uploaded_data)

            st.write_stream(stream_data(response))

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})