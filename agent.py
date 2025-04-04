# * import libraries
import os, openai
from decouple import config

class AgentSpotify:
    def __init__(self):
        os.environ["OPENAI_API_KEY"] = config('OPENAI_API_KEY')

    def chat(self, conversation:list, file:str) -> str:
        """
        Manage & response to user

        :param conversation: list of message between assistant & user
        :param file: user's playlist
        :return: agent's response
        """

        messages = [
            {
                "role": "system",
                "content": f"Tu es spécialisé dans l'analyse playlist Spotify. Tu dois répondre aux questions qu'on te pose a propos de la playlist suivante : {file}"
            }
        ]

        for conv in conversation:
            messages.append({"role": conv["role"], "content": conv["content"]})

        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        return response.choices[0].message.content