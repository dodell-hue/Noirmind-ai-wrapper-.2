import streamlit as st
import google.generativeai as genai

# ------------------------------------------------------------
# 🧠 CONFIGURATION
# ------------------------------------------------------------
# Load your Gemini API key securely from Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# ------------------------------------------------------------
# 🎭 DEFINE SPECIALIZED PERSONA
# ------------------------------------------------------------
# A Film Noir Detective persona who writes short mysterious reports.
persona_prompt = """
You are a Film Noir Detective trapped in a smoky city where every idea is a case.
You must write your response in exactly 150 words.
You must always include a list of **three clues** in Markdown format.
You must always start with a question and end with a definitive statement.
Stay in character as the detective — gritty, observant, mysterious.
"""

# ------------------------------------------------------------
# 🎨 STREAMLIT UI
# ------------------------------------------------------------
st.set_page_config(page_title="NoirMind: The Detective AI", layout="centered")
st.title("🕵️ NoirMind: The Detective AI")
st.caption("Where every idea is a mystery waiting to be solved...")

user_input = st.text_area("💭 Enter your idea or mystery for the detective to solve:", height=150)
submit = st.button("🔍 Investigate")

# ------------------------------------------------------------
# ⚡ RUN AI CALL
# ------------------------------------------------------------
if submit and user_input.strip():
    with st.spinner("Detective is piecing together the clues..."):
        try:
            # Use Gemini 1.5 Flash (fast and generative)
            model = genai.GenerativeModel("gemini-pro")

            full_prompt = f"{persona_prompt}\n\nUser's Case: {user_input}\n\nDetective's Report:"
            response = model.generate_content(full_prompt)

            output_text = response.text.strip()
            st.markdown("### 🕯️ Detective's Final Report")
            st.markdown(output_text)

        except Exception as e:
            st.error("🚨 Something went wrong while generating the detective's report.")
            st.exception(e)
else:
    st.info("Enter an idea above, then press 'Investigate' to get started.")
