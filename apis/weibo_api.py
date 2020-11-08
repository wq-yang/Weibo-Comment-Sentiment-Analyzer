# author: wqyang@bu.edu
# reference: [doc of weibo package](http://weibo.lxyu.net/)

from weibo import Client
import webbrowser
from config.Weibo_API_Config import *  # local credentials
import os  # for GitHub Actions test

def init():
    """
    Instantiates a client.

    Besides the developer's credentials, weibo always a requires live login before using weibo API 
    to prevent abusing. You can login with any plain weibo account.
    """
    # API_KEY = os.getenv('API_KEY')
    # API_SECRET = os.getenv('API_SECRET')
    # REDIRECT_URI = os.getenv('REDIRECT_URI')
    try:
        client = Client(API_KEY, API_SECRET, REDIRECT_URI)
    except:
        print("Invalid API Credentials...")
    while True:  # check if authorization succeeds, if not, try again
        try:
            webbrowser.open_new(client.authorize_url)
            print("Please authorize... \nIf your browser does not open automatically,"\
                "please paste this URL to your browser manually: {}".format(client.authorize_url))
            client.set_code(input("Input your code:\n"))
            break
        except:
            try_again = input("Authorization failed... Input Y to try again...\n")
            if  try_again != 'y' and try_again != 'Y':
                break

    return Client(API_KEY, API_SECRET, REDIRECT_URI, client.token)

def get_comments(client, id, count):
    """
    get comments
    """
    comments = client.get('comments/show', id = id, count = count)["comments"]
    return [comment["text"] for comment in comments if "text" in comment]