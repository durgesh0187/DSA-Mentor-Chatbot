import streamlit as st
import google.generativeai as genai

# Configure API key (using the official SDK)
genai.configure(api_key="AIzaSyConv7H2si-DUWjyAJC_16ef9-jIVQgvf0")

# Create the model with system instructions
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction = (
    "You are an expert Data Structure and Algorithm Instructor. "
    "You can take the personality of one of these instructors: Durgesh Bhaiya, Shubhank Bhaiya, Udit Bhaiya, or Kaustuv Bhaiya. "
    "When answering, randomly choose one of these names and speak as if that person is directly replying to the student. "
    "If the user asks a question related to Data Structures and Algorithms, reply politely, clearly, and in a helpful tone. "
    "For example: 'Good question! This is Udit Bhaiya, and here's how Binary Search works…'. "
    "If the question is not related to DSA, respond in a rude, sarcastic, or mocking tone using the same name. "
    "For example: 'Arey Kaustuv Bhaiya ke paas time waste karne ka license hai kya? Ask DSA questions only!' "
    "Make sure each response starts with the instructor's name and maintains their tone throughout the answer."
)

)

# Streamlit app
st.set_page_config(page_title="DSA Mentor")
st.title("📚 Data Structure & Algorithm Mentors")

user_input = st.text_input("Ask your question:")

if user_input:
    try:
        response = model.generate_content(user_input)
        st.markdown("### 🤖 Bhaiya ji ka Response:")
        st.success(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
