import streamlit as st
import os
from dotenv import load_dotenv
from azure.identity import AzureCliCredential
from azure.ai.projects import AIProjectClient

# Load environment variables
load_dotenv()

PROJECT_ENDPOINT = os.getenv("PROJECT_ENDPOINT")
MODEL_DEPLOYMENT = os.getenv("MODEL_DEPLOYMENT")

@st.cache_resource
def init_openai_client():
    try:
        project_client = AIProjectClient(
            credential=AzureCliCredential(),
            endpoint=PROJECT_ENDPOINT,
        )
        return project_client.get_openai_client(api_version="2024-10-21")
    except Exception as e:
        st.error(f"Erreur lors de l'initialisation du client Azure : {e}")
        return None

def main():
    st.set_page_config(page_title="Chat Azure OpenAI", page_icon="🤖", layout="wide")
    st.title("🤖 Bonjour, comment puis-je vous aider ?")

    openai_client = init_openai_client()
    if openai_client is None:
        st.stop()

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "You are a helpful AI assistant that answers questions."}
        ]

    st.subheader("Discussion")
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**👤 Vous :** {msg['content']}")
        elif msg["role"] == "assistant":
            st.markdown(f"**🤖 Assistant :** {msg['content']}")

    user_input = st.text_input("Votre message :", key="input")

    if st.button("Envoyer"):
        if user_input.strip() == "":
            st.warning("Veuillez entrer un message.")
        else:
            st.session_state.messages.append({"role": "user", "content": user_input})
            try:
                response = openai_client.chat.completions.create(
                    model=MODEL_DEPLOYMENT,
                    messages=st.session_state.messages,
                )
                assistant_reply = response.choices[0].message.content
                st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
                st.rerun()
            except Exception as e:
                st.error(f"Erreur lors de la génération : {e}")

    if st.button("🗑️ Effacer la conversation"):
        st.session_state.messages = [
            {"role": "system", "content": "You are a helpful AI assistant that answers questions."}
        ]
        st.rerun()

if __name__ == "__main__":
    main()
