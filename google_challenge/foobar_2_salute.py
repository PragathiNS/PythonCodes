def sal_count(s):
    count = 0
    right_count, left_count = 0, 0

    for i in s:
        if i not in ['<', '>', '-']:
            return (0)

    for i in range(len(s)):
        if s[i] == '>':
            right_count += 1
            for j in s[i:]:
                if j == '<':
                    count += 1
        elif s[i] == '<':
            left_count += 1
            count += right_count
        else:
            continue

    return (count)

print (sal_count("<<>><"))
