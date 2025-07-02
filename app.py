import streamlit as st

st.title("🤖 AI Freelancer Coach – Onboarding & Campaign Support (Demo Mode)")

# Hardcoded Q&A Dictionary
demo_responses = {
    "how do i set up my first ppc campaign?": """
1. Define your campaign objective (Traffic, Conversions, etc.).
2. Choose target geographies and audience segments.
3. Select high-RPC keywords aligned to top-performing verticals.
4. Set an appropriate daily budget and bids.
5. Create engaging ad creatives.
6. Launch and monitor your performance regularly via Babkee.
""",

    "what is a good daily budget to start with?": """
For beginners, start with a daily budget between $20–$50 per campaign.
This allows enough data to optimize performance without excessive risk.
As you gain insights, scale your budget based on RPC and ROI trends.
""",

    "what are best practices for targeting and keyword selection?": """
- Focus on high-RPC keywords relevant to your vertical.
- Use geo-targeting based on top-performing locations.
- Avoid overly broad keywords that waste spend.
- Regularly refine keyword lists based on campaign performance.
- Monitor negative keywords to prevent poor traffic quality.
""",

    "how does the ppc arbitrage model work?": """
You buy ad traffic from platforms like Google, Facebook, or TikTok,
then monetize it through search ads on Yahoo, Bing, and Google.
Profit comes from the margin between your traffic cost (CPC) and revenue generated per click (RPC).
The goal is to maximize this margin through smart campaign setup and optimization.
""",

    "where do i track my campaign performance?": """
Track your performance on the Babkee dashboard and internal reporting tools.
Monitor key metrics like RPC, CPC, Click Volume, Conversion Rate, and Scrub Rate daily.
""",

    "my rpc is low—what can i do?": """
- Review your CPC and Scrub Rate.
- Optimize keywords for higher RPC potential.
- Adjust geo-targeting to focus on high-performing regions.
- Refresh your ad creatives.
- Exclude low-converting placements.
""",

    "how to optimize cpc and reduce costs?": """
- Refine keyword targeting to eliminate non-performing terms.
- Use negative keywords to filter poor traffic.
- Focus on high-conversion geos and time slots.
- Test lower bids while monitoring traffic quality.
- Continuously review placement performance.
""",

    "what should i check if my ad isn’t getting impressions?": """
- Confirm your campaign is active and approved.
- Check that your daily budget and bids are sufficient.
- Ensure your targeting settings aren’t overly restrictive.
- Review keyword match types.
- Look for any disapprovals or account issues in Google Ads.
""",

    "how do i troubleshoot a sudden drop in conversion rate?": """
- Review recent campaign changes (budget, targeting, creatives).
- Check for landing page issues or site downtime.
- Analyze traffic quality and source breakdown.
- Monitor click-to-conversion funnel stages.
- Pause underperforming campaigns and optimize creatives.
""",

    "what verticals are trending this week?": """
This week, top-performing verticals showing high RPC trends include:
1. Software
2. Health & Wellness
3. Financial Services
Regularly check internal market insights and platform trend dashboards for updates.
"""
}


user_input = st.text_input("Ask your onboarding or campaign question:")

if user_input:
    lower_question = user_input.lower()
    if lower_question in demo_responses:
        st.markdown(f"**AI Coach Response:**\n\n{demo_responses[lower_question]}")
    else:
        st.warning("Sorry, this demo only supports limited sample questions. Please try one of these:\n- How do I set up my first PPC campaign?\n- My RPC is low. What should I do?\n- What is scrub rate?")
