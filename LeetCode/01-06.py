        S = input()
        compress = str()
        length = len(S)
        char = S[0]
        times = 0
        for i in range(length):
            if char == S[i]:
                times += 1
            else:
                compress = compress + char + str(times)
                times = 1
                char = S[i]
        compress = compress + char + str(times)
        if length > len(compress):
            print(compress)
        else:
            print(S)
