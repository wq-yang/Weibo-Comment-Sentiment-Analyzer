import sys
sys.path.append('.')

from comment_sentiment_analyze import *

weibo_client = weibo_api.init()

def test_normal_weibo():
    id = '4565837518474023'
    count = 20
    comments = []
    comments = weibo_api.get_comments(weibo_client, id, count)
    res = {}
    res = analyze_comments(comments)
    assert res != {}

def test_invalid_id():
    id = '0000000000000'
    count = 20
    comments = []
    comments = weibo_api.get_comments(weibo_client, id, count)
    res = {}
    res = analyze_comments(comments)
    assert res == {}

def test_invalid_count():
    id = '4565837518474023'
    count = 20
    comments = []
    comments = weibo_api.get_comments(weibo_client, id, count)
    res = {}
    res = analyze_comments(comments)
    assert res == {}
