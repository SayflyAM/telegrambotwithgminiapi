import streamlit as st
import telepot
from telepot.loop import MessageLoop
import google.generativeai as genai

# Streamlit app title
st.title("Telegram Chatbot with Streamlit")

# Function to handle incoming messages
def handle(msg):
    chat_id = msg['chat']['id']
    text = msg['text']
    response = model.generate_content(text)
    telepot.bot.sendMessage(chat_id, response.text)

# Configure generative AI
genai.configure(api_key="AIzaSyDOYIv0sDULoFLFDj88VklpODGlqH-UdMs")
model = genai.GenerativeModel('gemini-pro')

# Main Streamlit app
def main():
    # Set up the Telegram bot
    bot_token = st.text_input("Enter your Telegram bot token:")
    if bot_token:
        telepot.bot = telepot.Bot(bot_token)
        st.write('Telegram bot configured.')

        # Start message loop
        MessageLoop(telepot.bot, handle).run_as_thread()
        st.write('Listening for incoming messages...')
    else:
        st.warning('Please enter your Telegram bot token.')

if __name__ == "__main__":
    main()
