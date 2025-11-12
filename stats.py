def get_num_words(filePath):
    res = ""
    with open(filePath) as f:
        res += f.read()
    return len(res.split())

def charFrequency(fullText):
    dict = {}
    for ch in fullText:
        ch = ch.lower()
        if ch not in dict: dict[ch] = 0
        dict[ch] += 1
    return dict

def sortKey(dict):
    return dict["num"]

def getSortedDict(charFreq):
    res = []
    for ch in charFreq:
        if not ch.isalpha(): continue
        curr = {}
        curr["char"] = ch
        curr["num"] = charFreq[ch]
        res.append(curr)
    
    res.sort(reverse=True, key=sortKey)
    return res
