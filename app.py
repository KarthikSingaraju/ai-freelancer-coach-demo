import streamlit as st

st.title("🤖 AI Freelancer Coach – Onboarding & Campaign Support (Demo Mode)")

# Hardcoded Q&A Dictionary
demo_responses = {
    "how do i set up my first ppc campaign?": """
1. Select your campaign objective (traffic, conversions, etc.)
2. Choose target audience and geo locations.
3. Select high-RPC keywords.
4. Set your daily budget and bids.
5. Create engaging ad creatives.
6. Launch and monitor performance in Babkee.
""",
    "my rpc is low. what should i do?": """
- Review your CPC and scrub rate.
- Optimize for better-performing keywords.
- Refresh ad creatives.
- Check for low-quality publisher placements.
- Monitor performance in daily reports.
""",
    "what is scrub rate?": """
Scrub Rate measures the percentage of ad clicks that get filtered out due to poor quality traffic or invalid clicks. High scrub rate often signals poor traffic sources.
"""
}

user_input = st.text_input("Ask your onboarding or campaign question:")

if user_input:
    lower_question = user_input.lower()
    if lower_question in demo_responses:
        st.markdown(f"**AI Coach Response:**\n\n{demo_responses[lower_question]}")
    else:
        st.warning("Sorry, this demo only supports limited sample questions. Please try one of these:\n- How do I set up my first PPC campaign?\n- My RPC is low. What should I do?\n- What is scrub rate?")
