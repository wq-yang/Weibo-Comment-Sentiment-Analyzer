# author: wqyang@bu.edu
# reference: [doc of weibo package](http://weibo.lxyu.net/)

from weibo import Client
from config.weiboAPIConfig import *
import webbrowser

def init():
    client = Client(API_KEY, API_SECRET, REDIRECT_URI)
    webbrowser.open_new(client.authorize_url)
    print("Please authorize... If your browser does not open automatically,"\
        "please paste this URL to your browser manually: {}...".format(client.authorize_url))
    client.set_code(input("input your code:"))
    return Client(API_KEY, API_SECRET, REDIRECT_URI, client.token)

def getWeibo(client, id):
    return client.get('statuses/show', id = id)["text"]

def getComment(client, id, count):
    comments = client.get('comments/show', id = id, count = count)["comments"]
    # print([comment["text"] for comment in comments if "text" in comment])
    return [comment["text"] for comment in comments if "text" in comment]