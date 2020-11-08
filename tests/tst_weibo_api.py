import sys
sys.path.append('.')

from apis import weibo_api
from config.Weibo_API_Config import *  # local test

weibo_client = weibo_api.init()

def test_valid_id_and_count():
    id = '4565837518474023'
    count = 50
    comment = []
    comment = weibo_api.get_comments(weibo_client, id, count)
    assert len(comment) == 50

def test_invalid_id():
    id = '0000000000000000'
    count = 50
    comment = []
    comment = weibo_api.get_comments(weibo_client, id, count)
    assert len(comment) == 0

def test_invalid_count_1():
    # count test case 2: fetch 0 comments
    id = '4565837518474023'
    count = 0
    comment = []
    comment = weibo_api.get_comments(weibo_client, id, count)
    assert len(comment) == 0
def test_invalid_count_2():
    # count test case 3: fetch `n` comments, `n` > total count of comments
    id = '4565837518474023'
    count = 100000
    comment = []
    comment = weibo_api.get_comments(weibo_client, id, count)
    assert len(comment) < count

if __name__ == '__main__':
    pytest.main("test_weibo_api.py")