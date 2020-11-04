def get_num():
    while True:  # count of pieces of weibo, input should be a positive integer
        num = input("Input how many comments you want to fetch...\n")
        if num.isdigit() and int(num) > 0:
            num = int(num)
            break
        else:
            print("Please input a positive integer. Try again...")
    return num