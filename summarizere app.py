import streamlit as st
import requests

# Set the page layout to wide
st.set_page_config(layout="wide")

# Sidebar for navigation
page = st.sidebar.selectbox("Navigation", ["Home", "About"])

# Main content
if page == "Home":
    # Use custom CSS to align text slightly left and top
    st.markdown(
        """
        <style>
        
        .slight-left-top {
            
            position:absolute;
            top:-58px;
            left:-50px
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create a container for the text
    st.markdown('<div class="slight-left-top">IBM Text Summarizer</div>', unsafe_allow_html=True)
    
    # Ask for user input
    user_input = st.text_input("How can I help You Today?")

    # Display the user input
    if user_input:
        st.write(f"You entered: {user_input}")

elif page == "About":
    st.title("About")
    st.write("""
    This Text Summarization App is designed to help users quickly understand the main points of newspaper articles. 
    It leverages state-of-the-art natural language processing (NLP) models to generate concise summaries.

    ### Features
    - **Text Summarization**: Get a brief summary of the article.
    - **Sentiment Analysis**: Understand the overall sentiment of the article.
    - **Keyword Extraction**: Identify key terms and phrases.
    - **Translation**: Translate summaries into multiple languages.
    - **Voice Summaries**: Listen to the summaries instead of reading.
    - **Personalized Recommendations**: Get article suggestions based on your reading history.

    ### How It Works
    1. **Upload an Article**: Upload a text file or paste the text of the article.
    2. **Get Summary**: The app processes the text and provides a summary.
    3. **Explore Features**: Use additional features like sentiment analysis and keyword extraction.

    ### About the Developer
    This app was developed by our Team, a passionate developers with a keen interest in NLP and AI technologies.

    ### Contact
    For any queries or feedback, please contact .
    """)
