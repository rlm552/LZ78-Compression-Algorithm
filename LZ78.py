f = open("book.txt", "r")
if f.mode == "r":
    text = f.read()

###### initialized variables #######
phraseDic = dict()
pos = 0
buffer = text[pos]
lastChar = len(text) - 1
s = b''
end = False
###############################

def inDic(phraseDic, buffer):
    """ returns True is string in dictionary, False if not"""
    global closestIdx
    idx = 0
    for phrase in phraseDic:
        idx += 1
        if phrase == buffer:
            closestIdx = idx
            return True
    return False

while not end:
    lastLetter = text[pos]
    closestIdx = 0
    while inDic(phraseDic, buffer):        
        if pos == lastChar:
            s += closestIdx.to_bytes(2, byteorder = 'big')
            end = True
            break
        else: 
            pos += 1
            lastLetter = text[pos]
            buffer += lastLetter
    else:             
        phraseDic[buffer] = str(closestIdx) + lastLetter
        s += closestIdx.to_bytes(2, byteorder = 'big') + lastLetter.encode()
        if pos != lastChar:
            pos += 1
            buffer = text[pos]
        else:
            end = True
            break
        

print(s)





        



    