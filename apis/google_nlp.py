# author: wqyang@bu.edu
# reference: [Google Natural Language Client Libraries Documentation](https://cloud.google.com/natural-language/docs/reference/libraries)

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def init():
    """ 
    Instantiates a client
    """
    client = language.LanguageServiceClient()
    return client

def analyze_sentiment(client, text):
    """
    params: client, text to analyze
    return: sentiment{score, magnitude}
    """
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT
    )

    sentiment = client.analyze_sentiment(document=document).document_sentiment
    
    return sentiment