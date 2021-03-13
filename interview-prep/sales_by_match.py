# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()

    # concept of stack
    stack = []
    top = -1

    for x in ar:
        if len(stack) < 0:
            stack.append(x)
            top = top + 1
        elif len(stack) > 0 and stack[top] == x:
            stack.pop()
            top = top - 1
        else:
            stack.append(x)
            top = top + 1

    return int((len(ar) - len(stack)) / 2)


a = sockMerchant(7, [10, 10, 10, 20, 30, 40, 20])
print(a)
