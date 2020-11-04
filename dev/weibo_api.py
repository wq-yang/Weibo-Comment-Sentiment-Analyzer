# author: wqyang@bu.edu
# reference: [doc of weibo package](http://weibo.lxyu.net/)

from weibo import Client
import webbrowser
from config.Weibo_API_Config import *

def init():
    """
    Instantiates a client.

    Besides the developer's credentials, weibo always a requires live login before using weibo API 
    to prevent abusing. You can login with a plain weibo account.
    """
    client = Client(API_KEY, API_SECRET, REDIRECT_URI)
    while True:  # check if authorization succeeds, if not, try again
        try:
            webbrowser.open_new(client.authorize_url)
            print("Please authorize... \nIf your browser does not open automatically,"\
                "please paste this URL to your browser manually: {}".format(client.authorize_url))
            client.set_code(input("Input your code:\n"))
            break
        except:
            print("Authorization failed. Please try again...")
    return Client(API_KEY, API_SECRET, REDIRECT_URI, client.token)

def get_comments(client, id, count):
    """
    get comments
    """
    comments = client.get('comments/show', id = id, count = count)["comments"]
    return [comment["text"] for comment in comments if "text" in comment]