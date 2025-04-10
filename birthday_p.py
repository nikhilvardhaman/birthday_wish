import streamlit as st
from openai import OpenAI
import os

# Set your OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="🎂 Birthday Wishes for Pinku", page_icon="💖")

st.title("💌 Birthday Wishes for Pinku")
st.markdown("Let AI craft a unique birthday message just for you baby 💝")

# Fixed values
name = "Pinku"
relationship = "girlfriend"

# Let user pick the mood/tone
tone = st.selectbox("Pick a mood for the birthday wish", [
    "Heartfelt ❤️", "Funny 😂", "Romantic 💕", "Poetic 🎭", "Casual 😎", "Spiritual 🙏"
])

tone_styles = {
    "Heartfelt ❤️": "heartfelt",
    "Funny 😂": "funny",
    "Romantic 💕": "romantic",
    "Poetic 🎭": "poetic",
    "Casual 😎": "casual",
    "Spiritual 🙏": "spiritual"
}

# Button to generate
if st.button("Tadaa🎉"):
    with st.spinner("Stirring the love potion... 🧪💘"):
        
        prompt = (
            f"Write a unique and {tone_styles[tone]} birthday message for my {relationship}. "
            f"Her name is {name}. The message should be original, loving, and avoid clichés. "
            f"Make it feel personal and warm."
        )

        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.95,
                max_tokens=120
            )
            wish = response.choices[0].message.content.strip()
            #st.success("Here's your birthday message! 🎉")
            st.balloons() 
            st.success("Here's your birthday wish! 💕")
            st.markdown(f"> {wish}")

            st.download_button("📩 Download as text", wish, file_name="birthday_wish.txt")
        except Exception as e:
            st.error(f"Error: {e}")
