def alternatingCharacters(s):
    stack = []
    tos = -1

    for c in s:
        if tos < 0:
            stack.append(c)
            tos += 1
        elif stack[tos] != c:
            stack.append(c)
            tos += 1

    print(len(s) - len(stack))
    # print(tos)


alternatingCharacters("aabaab")

