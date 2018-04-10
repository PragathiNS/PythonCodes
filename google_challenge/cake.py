def answer(s):
    last_char = s[-1]
    patt = ""
    for i in s:
        if i == last_char:
            patt += i
            com_str = patt * s.count(patt)
            if (com_str == s):
                return (s.count(patt))
            else:
                continue
        patt += i
    print (patt)
    return (0)


s = "abccbaabccba"
print(answer(s))
