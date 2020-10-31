# author: wqyang@bu.edu

import google_nlp
import weibo_api
from id_translation import mid2id

def choose_weibo():
    """
    Choose a piece of weibo you want to analyze interactively
    You can input either URL, mid, or id of that piece of weibo
    return id
    """
    choice = input("Choose a way to get weibo you would like to analyze: 0. URL(default);"\
        " 1. mid; 2. id...\n")
    if choice == "2":  # input a id
        while True:  # check if id is valid, if not, re-input it
            id = input("Input id of the weibo you would like to analyze...\n")
            if id.isnumeric():
                break
            else:
                print("That was not a valid id. A valid id should look like '4565659885767682'."\
                    " Please try again...")
    elif choice == "1":  # input mid
        while True:  # check if mid is valid, if not, re-input it
            mid = input("Input mid of the weibo you would like to analyze...\n")
            if mid.isalnum():
                break
            else:
                print("That was not a valid mid. A valid mid should look like 'Jry72ocr8'."\
                    " Please try again...")
        id = mid2id(mid)
    else :  # input URL
        while True:  # check if URL is valid, if not, re-input it
            url = input("Input the url of the weibo you would like to analyze...\n")
            # get mid from url (a url example: 
            # "https://weibo.com/2803301701/Jry72ocr8?filter=hot&root_comment_id=0")
            mid = url.lstrip(':/.htpsweibocm')\
                .partition('?')[0]\
                .partition('/')[2]
            if mid.isalnum():
                break
            else:
                print("That was not a valid url. A valid url should look like "\
                    "'https://weibo.com/2803301701/Jry72ocr8?filter=hot&root_comment_id=0'."\
                    " Please try again...")
        id = mid2id(mid)
    return id

def get_num():
    while True:  # count of pieces of weibo, input should be a positive integer
        num = input("Input how many comments you want to fetch...\n")
        if num.isdigit() and int(num) > 0:
            num = int(num)
            break
        else:
            print("Please input a positive integer. Try again...")
    return num
    
def analyze_comments(comments):
    """
    analyze sentiment of comments using Google NLP
    return 
    """
    # initiate results
    most_positive_comment = { "score":0, "text":"" }
    most_negative_comment = { "score":0, "text":"" }
    strongest_comment = { "magnitude":0, "text":"" }
    average = { "score":0, "magnitude":0 }
    res = { 
        "positive": most_positive_comment,
        "negative": most_negative_comment,
        "strong": strongest_comment,
        "average": average
    }

    # analyze the sentiment: 
    # iterate comments, find the most positive, negative, and strongest one,
    # and also calculate the average
    nlp_client = google_nlp.init()
    for comment in comments:
        sentiment = google_nlp.analyze_sentiment(nlp_client, comment)
        if sentiment.score > most_positive_comment["score"]:
            most_positive_comment["score"] = sentiment.score
            most_positive_comment["text"] = comment
        if sentiment.score < most_negative_comment["score"]:
            most_negative_comment["score"] = sentiment.score
            most_negative_comment["text"] = comment
        if sentiment.magnitude > strongest_comment["magnitude"]:
            strongest_comment["magnitude"] = sentiment.magnitude
            strongest_comment["text"] = comment
        average["score"] += sentiment.score/len(comments)
        average["magnitude"] += sentiment.magnitude/len(comments)
    return res

if __name__ == "__main__":
    id = choose_weibo()
    count = get_num()

    # weibo init
    weibo_client = weibo_api.init()
    comments = weibo_api.get_comments(weibo_client, id, count)

    res = analyze_comments(comments)
    print("Finished! Analyzed {} pieces of weibo!".format(len(comments)), res)