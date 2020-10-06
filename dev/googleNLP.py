# author: wqyang@bu.edu
# reference: [Google Natural Language Client Libraries Documentation](https://cloud.google.com/natural-language/docs/reference/libraries)

# set GOOGLE_APPLICATION_CREDENTIALS
import os
os.environ["http_proxy"] = "http://127.0.0.1:9910"
os.environ["https_proxy"] = "http://127.0.0.1:9910"
os.environ["HTTP_PROXY"] = "http://127.0.0.1:9910"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:9910"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./practice/config/GoogleAPIKey.json"

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = u'Hello, world!'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))