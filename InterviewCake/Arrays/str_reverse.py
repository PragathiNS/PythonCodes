def strrev(chars):
    l = len(chars)
    for ind, val in enumerate(chars):
        if (l <= len(chars) / 2):
            break
        chars[ind] = chars[l - 1]
        chars[l - 1] = val
        l -= 1
    return chars


print (strrev([]))
print (strrev([1, 2, 4, 6]))
print (strrev(['P', 'r', 'a', 'g', 's']))

