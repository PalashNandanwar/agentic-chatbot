import streamlit as st
import wikipedia  # Wikipedia API
from textblob import TextBlob  # For spelling correction
from utils.web_search import search_web, identify_query_type, format_results
from utils.wikipedia_scraper import get_wikipedia_summary
from utils.cv_RUn import extract_text_from_pdf, generate_career_insights

# Initialize chat history if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar navigation
st.sidebar.title("Navigation")
st.markdown("")

option = st.sidebar.radio("Select Query Type", ("Wikipedia Search", "Web Scraper", "Resume Insights"))

# Main chat interface
st.title("Agentic-chatbot")

# Function for spelling correction using TextBlob
def correct_spelling(query):
    blob = TextBlob(query)
    return blob.correct()

if option == "Wikipedia Search":
    st.subheader("Wikipedia Summary Search")

    # Input with autocomplete functionality
    query = st.text_input("Enter a query for Wikipedia summary:")

    # Autocomplete function using Wikipedia search results
    def autocomplete(query):
        try:
            # Get Wikipedia suggestions based on the query
            suggestions = wikipedia.search(query, results=5)
            return suggestions
        except Exception as e:
            st.error(f"Error fetching suggestions: {str(e)}")
            return []

    # If query is entered, try to correct the spelling first
    if query:
        corrected_query = str(correct_spelling(query))
        st.write(f"Did you mean: **{corrected_query}**?")

        # Get autocomplete suggestions
        suggestions = autocomplete(corrected_query)

        if suggestions:
            st.write("Suggestions:")
            for suggestion in suggestions:
                if st.button(suggestion):  # User can click on suggestions
                    summary = get_wikipedia_summary(suggestion)
                    st.write(summary)
                    break
        else:
            st.write("No suggestions found for this query.")

        # Display the summary for the corrected query
        if not suggestions:
            try:
                summary = get_wikipedia_summary(corrected_query)
                st.write(summary)
            except wikipedia.exceptions.DisambiguationError as e:
                st.write(f"Multiple options found: {e.options}")
            except Exception as e:
                st.error(f"Error fetching summary: {str(e)}")

elif option == "Web Scraper":
    st.subheader("Web Search")
    query = st.text_input("Enter a search query:")

    if query:
        try:
            query_type = identify_query_type(query)
            search_results = search_web(query)
            formatted_results = format_results(search_results, query_type, query)
            st.write(formatted_results)
        except Exception as e:
            st.error(f"Error: {str(e)}")

elif option == "Resume Insights":
    st.subheader("Upload Your Resume")

    resume_file = st.file_uploader("Choose a PDF resume file:", type="pdf")

    if resume_file is not None:
        resume_text = extract_text_from_pdf(resume_file)
        insights = generate_career_insights(resume_text)

        st.markdown("### Career Insights")
        st.markdown(insights)

