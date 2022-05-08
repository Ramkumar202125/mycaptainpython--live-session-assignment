def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    print(sorted(dict.items(),reverse=True))
    return "endof program"
print(char_frequency('Mississippi'))
print()
