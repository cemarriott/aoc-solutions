from functools import cmp_to_key

def packetChecker(left, right):
    if left == []:
        if right == []:
            return None
        else: 
            return True
    for idx, item in enumerate(left):
        try:
            # Both ints
            if type(item) == int and type(right[idx]) == int:
                if item == right[idx]:
                    continue
                elif item < right[idx]:
                    return True
                else:
                    return False
            # Both lists
            elif type(item) == list and type(right[idx]) == list:
                subCheck = packetChecker(item, right[idx])
                if subCheck != None:
                    return subCheck
                else: 
                    if len(item) == len(right[idx]):
                        continue
                    elif len(item) < len(right[idx]):
                        return True
            else:
                # Left int, right list
                if type(item) == int:
                    subCheck = packetChecker([item], right[idx])
                    if subCheck != None:
                        return subCheck
                    else: 
                        if len([item]) == len(right[idx]):
                            continue
                        elif len([item]) < len(right[idx]):
                            return True
                # Left list, right int
                else:
                    subCheck = packetChecker(item, [right[idx]])
                    if subCheck != None:
                        return subCheck
                    else: 
                        continue
        # Right list ran out of items first
        except:
            return False
    # Couldn't make a determination
    return None

def sortPackets(left, right):
    val = packetChecker(left, right)
    if val == None: return 0
    return 1 if val == True else -1

with open('input.txt', 'r') as inputFile:
    packetList = inputFile.read().splitlines()

    # Don't do this without checking your input... 
    # You've been warned.
    packetList = [eval(l) for l in packetList if l != '']

    correctPackets = []
    packetInd = 1
    for ind in range(0, len(packetList), 2):
        inOrder = packetChecker(packetList[ind], packetList[ind + 1])
        if inOrder or inOrder == None: correctPackets.append(packetInd)
        packetInd += 1
    print('Part 1 : The sum of indices is ' + str(sum(correctPackets)))

    sortList = packetList
    sortList.append([[2]])
    sortList.append([[6]])

    sortList = sorted(sortList, key=cmp_to_key(sortPackets), reverse=True)
    ind1 = sortList.index([[2]]) + 1
    ind2 = sortList.index([[6]]) + 1

    print('Part 2 : The decoder key is ' + str(ind1 * ind2))