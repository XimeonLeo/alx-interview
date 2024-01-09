#!/usr/bin/python3

def canUnlockAll(boxes):
    if type(boxes) != list or len(boxes) == 0:
        return False

    boxLen = len(boxes)

    keysAvailable = [0]
    keysUsed = set()

    while keysAvailable:
        openedBoxIndex = keysAvailable.pop()
        keysUsed.add(openedBoxIndex)

        openedBoxes = boxes[openedBoxIndex]

        if type(openedBoxes) != list:
            return False
        for key in openedBoxes:
            if key < boxLen and key not in keysUsed:
                if key not in keysAvailable:
                    keysAvailable.append(key)

    return len(keysUsed) == boxLen
