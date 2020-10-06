# author: bindog
# ref: https://bindog.github.io/blog/2015/04/20/other-way-to-collect-sina-data/
# WHY WE NEED THIS: weibo use both "mid" and "id" to refer to a certain piece of weibo. 
#                   we only get "mid" from the url (e.g. https://weibo.com/2146965345/Jj76HDfz8,
#                   "2146965345" is the UserID, "Jj76HDfz8" is "mid" of this piece of weibo)
#                   when using weibo API, we must use "id" to refer to this piece of weibo. 
#                   for the example above, its id is "4545555559354630". 
#                   mid <-> id can be done with base 62 hash function.

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rsplit(s, count):
    f = lambda x: x > 0 and x or 0
    return [s[f(i - count):i] for i in range(len(s), 0, -count)]

def id2mid(id):
    result = ''
    for i in rsplit(id, 7):
        str62 = base62_encode(int(i))
        result = str62.zfill(4) + result
    return result.lstrip('0')

def mid2id(mid):
    result = ''
    for i in rsplit(mid, 4):
        str10 = str(base62_decode(i)).zfill(7)
        result = str10 + result
    return result.lstrip('0')

def base62_encode(num, alphabet=ALPHABET):
    """Encode a number in Base X
    `num`: The number to encode
    `alphabet`: The alphabet to use for encoding
    """
    if (num == 0):
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)

def base62_decode(string, alphabet=ALPHABET):
    """Decode a Base X encoded string into the number
    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1
    return num

if __name__ == '__main__':
    print (mid2id('CeaOU15IT'))
    print (id2mid('3833781880260331'))