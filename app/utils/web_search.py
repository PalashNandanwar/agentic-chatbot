import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import re

# Load environment variables from the .env file
load_dotenv()

def search_web(query):
    api_key = os.getenv('API_KEY')
    cx = os.getenv('CX')

    if not api_key or not cx:
        raise ValueError("API key or Custom Search Engine ID is not set. Ensure they are stored in the .env file.")

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": api_key,
        "cx": cx,
        "num": 6,  
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        results = response.json().get('items', [])
        if not results:
            raise Exception("No relevant search results found. Try refining your search.")
        return results
    else:
        raise Exception(f"Error fetching search results: {response.status_code}, {response.text}")

def identify_query_type(query):
    if re.search(r'\b(compare|versus)\b', query, re.IGNORECASE):
        return "comparative_analysis"
    elif re.search(r'\b(how to|guide|tutorial)\b', query, re.IGNORECASE):
        return "guides_and_how_tos"
    elif re.search(r'\b(reviews|opinions|ratings)\b', query, re.IGNORECASE):
        return "reviews_and_opinions"
    elif re.search(r'\b(live|weather|score|stock)\b', query, re.IGNORECASE):
        return "real_time_data"
    elif re.search(r'\b(who is|biography|born|death|died)\b', query, re.IGNORECASE):
        return "person_query"
    elif re.search(r'\b(list|data|statistics)\b', query, re.IGNORECASE):
        return "specific_data"
    elif re.search(r'\b(event|concert|schedule|entertainment)\b', query, re.IGNORECASE):
        return "event_or_entertainment"
    elif re.search(r'\b(financial|business|revenue|reports)\b', query, re.IGNORECASE):
        return "financial_or_business_data"
    else:
        return "general_info"

def format_results(results, query_type, query):
    formatted = ""

    if query_type == "person_query":
        main_info = next((item for item in results if 'wikipedia' in item.get('link', '').lower()), results[0])
        formatted += f"**Detailed Information about '{query}':**\n"
        formatted += f"{main_info.get('snippet', 'Snippet unavailable')}\n"
        formatted += f"[Read more on Wikipedia]({main_info.get('link')})\n"

        social_media_sites = ["instagram.com", "twitter.com", "facebook.com"]
        social_links = [item.get('link') for item in results if any(site in item.get('link', '') for site in social_media_sites)]

        if social_links:
            formatted += "\n**Social Media Links:**\n"
            for link in social_links:
                formatted += f"- [Visit here]({link})\n"

    elif query_type == "guides_and_how_tos":
        formatted += f"**Guides and Tutorials on '{query}':**\n"
        for result in results:
            formatted += f"- **{result.get('title')}**: {result.get('snippet')}\n  [Read more]({result.get('link')})\n"

    elif query_type == "comparative_analysis":
        formatted += f"**Comparative Analysis for '{query}':**\n"
        for idx, result in enumerate(results):
            formatted += f"{idx + 1}. **{result.get('title')}**: {result.get('snippet')}\n  [Link]({result.get('link')})\n"

    elif query_type == "reviews_and_opinions":
        formatted += f"**Reviews and Opinions on '{query}':**\n"
        for result in results:
            formatted += f"- **{result.get('title')}**: {result.get('snippet')}\n  [Read more]({result.get('link')})\n"

    elif query_type == "real_time_data":
        formatted += f"**Real-Time Data for '{query}':**\n"
        for result in results:
            formatted += f"- **{result.get('title')}**: {result.get('snippet')}\n  [Read more]({result.get('link')})\n"

    elif query_type == "specific_data":
        formatted += f"**Specific Data for '{query}':**\n"
        for result in results:
            formatted += f"- **{result.get('title')}**: {result.get('snippet')}\n  [Read more]({result.get('link')})\n"

    elif query_type == "financial_or_business_data":
        formatted += f"**Financial and Business Data for '{query}':**\n"
        for result in results:
            formatted += f"- **{result.get('title')}**: {result.get('snippet')}\n  [Read more]({result.get('link')})\n"

    else:  # For general info or other queries
        formatted += f"**General Information on '{query}':**\n"
        for result in results:
            formatted += f"- **{result.get('title')}**: {result.get('snippet')}\n  [Read more]({result.get('link')})\n"

    return formatted

