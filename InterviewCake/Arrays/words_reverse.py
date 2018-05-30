def reverse_words(message):
    st = ""
    ret = []
    for i in message:
        if i != ' ':
            st += i
        else:
            ret.append(st)
            st = ""






print (reverse_words([ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]))
