import re
from math import prod

monkeys = []
commonDenom = 0

class Monkey:
    items = []
    operation = ()
    test = 0
    trueTarget = 0
    falseTarget = 0
    inspectionCount = 0

    def __init__(self, items, op, test, trueTarget, falseTarget):
        self.items = items
        self.operation = op
        self.test = test
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget

    def removeItems(self, delList):
        for item in delList:
            self.items.remove(item)
    
    def inspectItems(self):
        global commonDenom
        deleteList = []
        for idx, item in enumerate(self.items):
            self.inspectionCount += 1
            #print('Inspection of item with level ' + str(item))
            if self.operation[0] == '+':
                item += item if self.operation[1] == None else int(self.operation[1])
            elif self.operation[0] == '*':
                if self.operation[1] == None:
                    item = item ** 2
                else: 
                    item *= int(self.operation[1])
                #item *= item if self.operation[1] == None else int(self.operation[1])
            #print('Level increases to ' + str(item))
            #item = floor(item / 3)
            #print('Level reduced to ' + str(item))
            item %= commonDenom
            self.items[idx] = item
            if item % self.test == 0:
                monkeys[self.trueTarget].items.append(item)
                deleteList.append(item)
                print('Item passed test, sent to monkey ' + str(self.trueTarget))
            else:
                monkeys[self.falseTarget].items.append(item)
                deleteList.append(item)
                print('Item failed test, sent to monkey ' + str(self.falseTarget))
        self.removeItems(deleteList)

with open('input.txt', 'r') as inputFile:
    reg = re.compile(r"Monkey\s([\d]+):[\\n\s]*[A-Za-z\s:]+([\d,\s]*)[\\n\s]*[A-Za-z:\s=]*([\*\+]+)[\s]+([\d|\w]*)[\\n\s]*[A-Za-z:\s]*([\d]*)[\\n\s]*[A-Za-z:\s]*([\d]*)[\\n\s]*[A-Za-z:\s]*([\d]*)[\\n\s]*", re.M)
    monkeyRecords = inputFile.readlines()
    monkeyRecords = ''.join(monkeyRecords)

    matches = reg.findall(monkeyRecords)

    for match in matches:
        startItems = [int(i) for i in match[1].strip().split(', ')]
        if match[3] == 'old':
            opNum = None
        else:
            opNum = int(match[3])
        thisMonkey = Monkey(startItems, (match[2], opNum), int(match[4]), int(match[5]), int(match[6]))
        monkeys.append(thisMonkey)

    commonDenom = prod([monk.test for monk in monkeys])

    for round in range(10000):
        print('Round ' + str(round) + ': ')
        for idx, monkey in enumerate(monkeys):
            print('Monkey ' + str(idx) + ': ')
            monkey.inspectItems()
        #print('Worry levels:')
        #for idx, monkey in enumerate(monkeys):
        #    print('Monkey ' + str(idx) + ': ' + str(monkey.items))    

    inspectionList = []
    for idx, monkey in enumerate(monkeys):
        inspectionList.append(monkey.inspectionCount)
        print('Monkey {0} inspected items {1} times.'.format(str(idx), str(monkey.inspectionCount)))
    inspectionList = sorted(inspectionList, reverse=True)
    print('Monkey business = {0}'.format(str(inspectionList[0] * inspectionList[1])))

    