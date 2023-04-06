def sundayAlg(text, pat):
    t = len(text)
    p = len(pat)
    i = 0
    while i <= t - p:
        j = 0
        while j < p and text[i+j] == pat[j]:
            j += 1
        if j == p:
            last_index = i
        if i + p < t:
            i += p - pat.rfind(text[i + p])
        else:
            break
    return last_index if 'last_index' in locals() else -1
print(sundayAlg('mY5#E3g!F*6tI9Fg6tW*6t', 'W*6t'))
print(sundayAlg('abcadabadccdbabd', 'cadab'))
