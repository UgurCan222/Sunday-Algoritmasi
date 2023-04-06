def check(char, pat, lenpat, textindex):
    j = lenpat - 1
    while j >= 0:
        if pat[j] == char:
            return textindex - j
        j -= 1
    return -1
     
def sundayAlg(text, pat):
    t, p = len(text), len(pat)
    i = 0
    while i < t - p:
        z = p - 1
        while z >= 0 and pat[z] == text[i+z]:
            z -= 1
        if z == -1:
            return i
        i += check(text[i+p], pat, p, i+p)
    return -1

print(sundayAlg('mY5#E3g!F*6tI9Fg6tW*6t', 'W*6t'))
print(sundayAlg('abcadabadccdbabd', 'cadab'))
