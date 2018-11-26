import re
def string_checker(string):

    chars = re.compile(r'[^a-zA-Z0-9.]')
    res = chars.search(string)

    check = not(bool(res))
    if check == True:
	    return("Your string was accepted.")
    else:
	    return("Your string contains characters other than the ones allowed.")
