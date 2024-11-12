import wikipediaapi

def get_wikipedia_summary(query, language='english'):
    """
    Fetches the summary of a Wikipedia page based on the query.
    Args:
        query (str): The topic to search for.
        language (str): The language code (default is English).
    Returns:
        str: Summary of the Wikipedia page or a not-found message.
    """
    # Clean and format the query for Wikipedia search
    formatted_query = query.strip().replace(" ", "_").title()  # Capitalizing properly for Wikipedia format

    wiki_wiki = wikipediaapi.Wikipedia(language)
    page = wiki_wiki.page(formatted_query)
    
    if page.exists():
        return page.summary
    else:
        return f"Sorry, the topic '{query}' was not found on Wikipedia."
