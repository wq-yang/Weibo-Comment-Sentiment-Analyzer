# Social Media Analyzer

Project 2 for EC601

*p.s. Because my application of Twitter Developer Account was rejected (for twice...), I made a comment analyzer for [Weibo](https://www.weibo.com), a Chinese social media platform similar to Twitter.*

## Description

- **Name:** weibo comment sentiment analyzer
- **Category:** command line tool, written in python
- **API used:** 
  - [Google Natural Language](https://cloud.google.com/natural-language/)
  - [weibo](lxyu.github.io/weibo/) (a concise third-party weibo python sdk which support python3)
- **Language:** python (>=3.6)

## MVP

Input the `id` or `mid` of a piece of weibo, return the overall sentiment of comments (average of the first `count` comments), and also return the most negative, the most positive, and the strongest comments.

## User Story

For influencers or business accounts, they can use this tool to know their follower's attitude towards a weibo, to evaluate this weibo's popularity, or maybe they can make some adjustment in their later weibos.

For sociologists, they can use this tool to know the public opinion of a weibo or a topic, and analyze the social impact.

For public relations officer, they can use this tool to know users' opinion to some weibos, to evaluate their work, or take further actions if, for example, users are offended by that weibo.

## Usage

- follow instructions on Google Cloud tutorial, create Google Natural Language project, and download configuration file, name it as `Google_API_Key.json`, and store it in the `config/` directory.
- follow instructions on Weibo Open Platform, apply for weibo developer permission, and create a micro-service, get API_KEY and API_SECRET, and store them in `config/Weibo_API_Config.py`. 

- add configuration files to `config`.
- install dependencies using `pip install -r requirements.txt`.

- run `python comment_sentiment_analyze.py`, and follow its instructions.

## Example

<div align="center">
	<img src="example.gif" alt="example" style="zoom:90%;" />
</div>
Analyzed comments of a weibo about Eddie Van Halen's death.



## File Structure

```
├─.github:                            for GitHub
│ ├─encrypted_config:                 store encrypted credentials
│ │ ├─Google_API_Key.json.gpg:        encrypted Google API credential
│ │ └─decrypt_secret.sh:              bash script to decrypt
│ └─workflows:                        GitHub Actions test
│   └─python_test.yml:                YAML script
├─config:                             add your own configurations
│ ├─Weibo_API_Config.py:              add your own Weibo API config
│ └─Google_API_Key.json:              add your own Google API config
├─apis:                               
│ ├─__init__.py:                      some settings about path
│ ├─weibo_api_.py:                    Weibo API
│ └─google_nlp.py:                    Google Cloud Natural Language API
├─util:                               some functional components
│ ├─id_translation:                   helper function for getting the id of a piece of weibo
│ ├─choose_weibo.py:                  receive input, URL/id/mid of weibo, return id
│ └─get_num.py:                       receive input num of counts, check its validity
├─comment_sentiment_analyze.py        the main python script
├─tests:                              tests
│ ├─test_google_nlp.py
│ ├─tst_weibo_api.py
│ └─tst_comment_sentiment_analyze.py
├─requirements.txt:                   dependencies
└─README.md:                          README
```

## Testing

- Auto-testing with GitHub Actions and Pytest

  Test Google Natural Language API with GitHub Actions and Pytest with different Python versions, see: [test1](https://github.com/wq-yang/EC601-Project2-Project4-Social-Media-Analyzer/actions/runs/352544403), [test2](https://github.com/wq-yang/EC601-Project2-Project4-Social-Media-Analyzer/actions/runs/352547020)

- Manual Test

  Because Weibo API's initialization always needs authorization (user login and authorize to my app, to prevent abusing), it seems to be unable to test it automatically. I tested several cases manually:

  - Normal test: get results.
  - Invalid Weibo API credentials: Error code 21324 in authorization page, prompt `Authorization failed... Input Y to try again...` after some input.
  - Invalid URL: prompt `That was not a valid url.`, give an example of valid URL and ask for another try
  - Invalid amount of comments: 
    - zero, negative integer or non-numeric input: ask for positive integer
    - amount that exceeds the available amout of comments: analyzed all available comments
  - Invalid mid: fetch 0 piece of comments, and return the result
  - Invalid id: 
    - Invalid but numeric id: fetch 0 piece of comments, and return the result
    - non-numeric id: ask for numeric id

## Reference

[1] [Google Natural Language Client Libraries Documentation](https://cloud.google.com/natural-language/docs/reference/libraries)

[2] [Weibo Python SDK (third party)](http://weibo.lxyu.net)

[3] [other-way-to-collect-sina-data](https://bindog.github.io/blog/2015/04/20/other-way-to-collect-sina-data)

[4] [Weibo Official API Document](https://open.weibo.com/wiki/API%E6%96%87%E6%A1%A3_V2/en)