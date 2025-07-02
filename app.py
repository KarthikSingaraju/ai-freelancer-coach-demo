
import streamlit as st
import openai

# Read API key from Streamlit Cloud Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

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
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        ai_reply = response['choices'][0]['message']['content']
        st.markdown(f"**AI Coach Response:**\n\n{ai_reply}")
