import streamlit as st
from openai import OpenAI

# Load API Key from Streamlit Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

system_prompt = """
You are an AI-powered Freelance Media Buyer Coach for a PPC Arbitrage business.

You help freelancers with:
- Onboarding questions
- Campaign optimization tips
- PPC concepts like RPC, CPC, CTR
- Real-time tactical campaign advice

Be clear, concise, and actionable. Focus on steps freelancers can take next.
"""

st.title("🤖 AI Freelancer Coach – Onboarding & Campaign Support")

user_input = st.text_input("Ask your question:")

if user_input:
    with st.spinner("Thinking..."):
        chat_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        ai_reply = chat_response.choices[0].message.content
        st.markdown(f"**AI Coach Response:**\n\n{ai_reply}")
