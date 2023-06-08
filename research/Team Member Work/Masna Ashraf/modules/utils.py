import os
import streamlit as st

class Utilities:
    @staticmethod
    def load_api_key():
        """
        Loads the OpenAI API key from the user's input and returns it
        """
        user_api_key = st.text_input(
            label="Your OpenAI API key", placeholder="sk-...", type="password"
        )
        return user_api_key
