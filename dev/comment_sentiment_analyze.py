# author: wqyang@bu.edu
import googleNLP
import weiboAPI
from config.weiboAPIConfig import *
from id_translation import mid2id

weibo_client = weiboAPI.init()

def chooseWeibo():
    choice = input("choose a way to get weibo you would like to analyze: 0. id(default); 1. mid...")
    if choice == 1 or choice == "1":
        id = mid2id(input("input mid of the weibo you would like to analyze..."))
    else :
        id = input("input id of the weibo you would like to analyze...")
    # print("You are trying to analyze comments of the weibo: {}, if not, input \"choose again\"".format(
    #         weiboAPI.getWeibo(weibo_client, id)
    #         ))
    # if input() == "choose again":
    #     chooseWeibo()
    return id

id = chooseWeibo()
comments = weiboAPI.getComment(weibo_client, id, input("input how many comments you want to fetch..."))



nlp_client = googleNLP.init()

most_positive_comment = {"score":0, "text":""}
most_negative_comment = {"score":0, "text":""}
strongest_comment = {"magnitude":0, "text":""}
average = {"score":0, "magnitude":0}
for comment in comments:
    sentiment = googleNLP.analyzeSentiment(nlp_client, comment)
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

print("The most positive comment is:{}, whose sentiment score is {}.".format(
    most_positive_comment["text"], most_positive_comment["score"]
    ))
print("The most negative comment is:{}, whose sentiment score is {}.".format(
    most_negative_comment["text"], most_negative_comment["score"]
    ))
print("The strongest commment is:{}, whose sentiment magnitude is {}".format(
    strongest_comment["text"], strongest_comment["magnitude"]
    ))
print("The average sentiment score is {}, and the average sentiment magnitude is {}".format(
    average["score"], average["magnitude"]
    ))