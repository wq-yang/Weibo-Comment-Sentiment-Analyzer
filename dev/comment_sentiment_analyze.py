import google_nlp
import weibo_api
import os
from util.choose_weibo import choose_weibo
from util.get_num import get_num

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

    # Imports the Google Cloud client library.
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./config/Google_API_Key.json"

    nlp_client = google_nlp.init()
    for comment in comments:  
        # analyze each comment, find the most positive, negative, and strongest one, also calculate the average
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

def main():
    # weibo init
    weibo_client = weibo_api.init()
    while True:
        if input("Press ENTER to start! Press anything else to exit") != "":
            exit()
        id = choose_weibo()
        count = get_num()
        comments = weibo_api.get_comments(weibo_client, id, count)
        res = analyze_comments(comments)
        print("Finished! Analyzed {} pieces of weibo!".format(len(comments)), res)

if __name__ == "__main__":
    main()