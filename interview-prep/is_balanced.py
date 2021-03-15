def isBalanced(s):
    stack = []
    top = -1
    imbalance = False

    for c in s:
        if c == "(" or c == "{" or c == "[":
            stack.append(c)
            top += 1
        elif top >= 0 and (
            (c == ")" and stack[top] == "(")
            or (c == "}" and stack[top] == "{")
            or (c == "]" and stack[top] == "[")
        ):
            stack.pop()
            top -= 1
        else:
            imbalance = True
            break

    if not imbalance:
        return "YES" if top < 0 else "NO"
    else:
        return "NO"


print(isBalanced("{{}}]"))

