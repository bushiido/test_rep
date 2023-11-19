

text = "GATCCAGATCCCCATAC"
sablon = "CC"

def PatternCount(Text, Pattern):
    duzina = len(Text) - len(Pattern)
    count = 0
    for i in range(duzina):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count 


kurs = PatternCount(text,sablon)

print(kurs)