# author: wqyang@bu.edu
# reference: [doc of weibo package](http://weibo.lxyu.net/)

from weibo import Client
# from config.weiboAPIConfig import *
# from idTranslation import mid2id, id2mid

def getComment(API_KEY, API_SECRET, REDIRECT_URI):
    client = Client(API_KEY, API_SECRET, REDIRECT_URI)
    print("please paste the URL to your browser"+client.authorize_url+", and authorize")
    client.set_code(input("input your code:"))


    comments = client.get('comments/show', id=4545555559354630, count=5)["comments"]
    # print(type(comments), comments)

    # for comment in comments:
    #     print(comment["text"])
    return comments