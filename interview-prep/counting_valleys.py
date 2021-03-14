def countingValleys(steps, path):
    sealvl = 0
    valley = 0
    for i in range(steps):
        if path[i] == "D" and sealvl == 0:s
            valley += 1
        if path[i] == "D":
            sealvl -= 1
        else:
            sealvl += 1

    return valley


countingValleys(8, "UDDDUDUU")

