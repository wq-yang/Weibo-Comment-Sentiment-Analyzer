# author: wqyang@bu.edu
# reference: [Google Natural Language Client Libraries Documentation](https://cloud.google.com/natural-language/docs/reference/libraries)

# set GOOGLE_APPLICATION_CREDENTIALS
import os
os.environ["http_proxy"] = "http://127.0.0.1:9910"
os.environ["https_proxy"] = "http://127.0.0.1:9910"
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:9910"
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:9910"

# suppose you are currently in the dev directory
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./config/GoogleAPIKey.json"

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def init():
    # Instantiates a client
    client = language.LanguageServiceClient()
    return client

def analyzeSentiment(client, text, language="zh"):
    document = types.Document(
        content=text,
        language = language,
        type=enums.Document.Type.PLAIN_TEXT
    )

    sentiment = client.analyze_sentiment(document=document).document_sentiment
    
    return sentiment