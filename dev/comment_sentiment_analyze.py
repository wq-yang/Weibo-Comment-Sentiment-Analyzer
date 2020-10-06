import googleNLP
import weiboAPI
from config.weiboAPIConfig import *

comment = weiboAPI.getComment(API_KEY, API_SECRET, REDIRECT_URI)

