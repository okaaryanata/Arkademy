def ganti_kata(string,char1,char2):
    newString = ''
    for x in string:
        if x == char1:
            newString += char2
        else:
            newString += x
    return newString
print(ganti_kata("purwakarta",'a','o'))