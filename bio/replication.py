genom = "CGATATATCCATAG"
sablon = "ATA"

def pattern(genom,sablon):
    count = 0
    index = 0
    while index < len(genom):
        start = genom.find(sablon,index)
        if start == -1:
            break
        count += 1
        index += 1
    return count


def PatternCount(text,pattern):
    duzina = len(text) - len(pattern)
    count = 0
    for i in range(duzina):
        if text[i:i+len(pattern)] == pattern:
            count = count+1
    return count 
