if __name__ == "__main__":    
    from id_translation import mid2id
else:
    from util.id_translation import mid2id
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