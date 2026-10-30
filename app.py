import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
if api_key:
    client = genai.Client(api_key=api_key)
else:
    client = None

# Website settings
st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide"
)
st.markdown("""
<style>
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }

    h1 {
        color: #60A5FA;
        font-weight: 800;
    }

    h2, h3 {
        color: #93C5FD;
    }

    .stButton > button {
        background-color: #2563EB;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        width: 100%;
    }

    .stButton > button:hover {
        background-color: #1D4ED8;
        color: white;
    }

    .stTextArea textarea, .stTextInput input {
        background-color: #1F2937;
        color: white;
        border-radius: 10px;
    }

    hr {
        border-color: #374151;
    }
</style>
""", unsafe_allow_html=True)
st.title("📚 StudyMate AI")
with st.sidebar:
    st.title("📚 StudyMate AI")
    st.caption("Your Personal AI Study Assistant")

    st.divider()

    st.markdown("### ✨ Available Tools")
    st.markdown("""
    - 📝 Notes Summarizer
    - 🧠 Quiz Generator
    - 💡 Concept Explainer
    - 📖 Flashcard Generator
    """)

    st.divider()

    st.success("AI Assistant is Ready!")

    st.caption("Empowering Students to Learn Smarter — Created by Swarup")
st.subheader("Your Personal AI Study Assistant")

st.write("Study smarter, revise faster!")

st.divider()

tool = st.selectbox(
    "Choose your study tool:",
    [
        "Notes Summarizer",
        "Quiz Generator",
        "Concept Explainer",
        "Flashcard Generator"
    ]
)

if tool == "Notes Summarizer":

    st.header("📝 AI Notes Summarizer")

    notes = st.text_area(
        "Paste your study notes here:",
        height=250
    )

    if st.button("Generate Summary"):

        if not notes.strip():
            st.warning("Please enter your notes.")

        elif client is None:
            st.error("API key not found. Check your .env file.")

        else:
            with st.spinner("AI is summarizing your notes..."):

                try:
                    response = client.models.generate_content(
                        model="gemini-3.5-flash-lite",
                        contents=f"Summarize these study notes in simple English with important points:\n\n{notes}"
                    )

                    st.subheader("Your AI Generated Summary")
                    st.write(response.text)

                except Exception as e:
                    st.error(f"Something went wrong: {e}")

elif tool == "Quiz Generator":
    st.header("🧠 AI Quiz Generator")
    st.write("Generate MCQ questions from your study notes using AI.")

    quiz_notes = st.text_area(
        "Paste your study notes here:",
        height=200,
        key="quiz_notes"
    )

    number = st.selectbox(
        "Number of Questions:",
        [5, 10, 15, 20]
    )

    difficulty = st.selectbox(
        "Select Difficulty:",
        ["Easy", "Medium", "Hard"]
    )

    if st.button("Generate Quiz"):
        if not quiz_notes.strip():
            st.warning("Please enter your study notes.")

        elif client is None:
            st.error("API key not found. Check your .env file.")

        else:
            with st.spinner("AI is generating your quiz..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-3.5-flash-lite",
                        contents=f"""
                        Create {number} multiple choice questions
                        from the following study notes.

                        Difficulty: {difficulty}

                        Each question must have:
                        1. Four options (A, B, C, D).
                        2. One correct answer.
                        3. A short explanation.

                        Clearly show the correct answer.

                        Study Notes:
                        {quiz_notes}
                        """
                    )

                    st.subheader("Your AI Generated Quiz")
                    st.write(response.text)

                except Exception as e:
                    st.error(f"Something went wrong: {e}")
elif tool == "Concept Explainer":
    st.header("💡 AI Concept Explainer")
    st.write("Understand difficult topics in simple language with AI.")

    topic = st.text_input(
        "Enter the topic you want to understand:"
    )

    level = st.selectbox(
        "Choose explanation level:",
        ["Beginner", "Intermediate", "Advanced"]
    )

    if st.button("Explain Concept"):
        if not topic.strip():
            st.warning("Please enter a topic.")

        elif client is None:
            st.error("API key not found. Check your .env file.")

        else:
            with st.spinner("AI is explaining the concept..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-3.5-flash-lite",
                        contents=f"""
                        Explain the following topic at {level} level.

                        Topic: {topic}

                        Instructions:
                        1. Use simple and clear English.
                        2. Explain step by step.
                        3. Give real-life examples.
                        4. Include important points.
                        5. Give a short summary at the end.
                        """
                    )

                    st.subheader("Your AI Explanation")
                    st.write(response.text)

                except Exception as e:
                    st.error(f"Something went wrong: {e}")

elif tool == "Flashcard Generator":
    st.header("📖 AI Flashcard Generator")
    st.write("Create question-and-answer flashcards from your study notes.")

    flashcard_notes = st.text_area(
        "Paste your study notes here:",
        height=200,
        key="flashcard_notes"
    )

    number_of_cards = st.selectbox(
        "Number of Flashcards:",
        [5, 10, 15, 20]
    )

    if st.button("Generate Flashcards"):
        if not flashcard_notes.strip():
            st.warning("Please enter your study notes.")

        elif client is None:
            st.error("API key not found. Check your .env file.")

        else:
            with st.spinner("AI is creating your flashcards..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-3.5-flash-lite",
                        contents=f"""
                        Create {number_of_cards} flashcards from these study notes.

                        Each flashcard must contain:
                        1. One clear question.
                        2. One accurate and easy-to-understand answer.

                        Keep answers short and useful for exam revision.
                        Number every flashcard clearly.

                        Study Notes:
                        {flashcard_notes}
                        """
                    )

                    st.subheader("Your AI Generated Flashcards")
                    st.write(response.text)

                except Exception as e:
                    st.error(f"Something went wrong: {e}")
