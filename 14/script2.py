with open('input.txt', 'r') as inputFile:
    coordLines = inputFile.read().splitlines()
    rockCoordinates = set()
    sandCoordinates = set()

    # Load the rocks
    for line in coordLines:
        coordinates = [(int(x), int(y)) for x, y in [a.split(',') for a in line.split(' -> ')]]
        for idx, item in enumerate(coordinates):
            rockCoordinates.add((item[0], item[1]))

            # Generate rocks between the pairs
            if idx < len(coordinates) - 1:
                start = item
                end = coordinates[idx + 1]
                
                if start[0] == end[0]:
                    if start[1] < end[1]:
                        for num in range(start[1], end[1] + 1):
                            rockCoordinates.add((start[0], num))
                    elif start[1] > end[1]:
                        for num in range(start[1], end[1] - 1, -1):
                            rockCoordinates.add((start[0], num))
                elif start[1] == end[1]:
                    if start[0] < end[0]:
                        for num in range(start[0], end[0] + 1):
                            rockCoordinates.add((num, start[1]))
                    elif start[0] > end[0]:
                        for num in range(start[0], end[0] - 1, -1):
                            rockCoordinates.add((num, start[1]))
    
    # Generate the floor layer of rocks
    rockFloor = sorted([y for x, y in rockCoordinates], reverse=True)[0] + 2
    #rockWall = sorted([x for x, y in rockCoordinates], reverse=True)
    #rightMost = rockWall[0] + 10
    #leftMost = rockWall[-1] - 10
    #for h in range(leftMost, rightMost + 1):
    #    rockCoordinates.add((h, rockFloor))

                    
    # Load the sand
    stillRunning = True
    while stillRunning == True:
        sandResting = False
        sandGrain = (500, 0)
        blockers = rockCoordinates | sandCoordinates

        # Check if source is blocked
        if sandGrain in blockers:
            sandResting = True
            stillRunning = False

        while sandResting == False:
            # Check below
            if (sandGrain[0], sandGrain[1] + 1) not in blockers and sandGrain[1] + 1 != rockFloor:
                sandGrain = (sandGrain[0], sandGrain[1] + 1)
            
            # Check down-left
            elif (sandGrain[0] - 1, sandGrain[1] + 1) not in blockers and sandGrain[1] + 1 != rockFloor:
                sandGrain = (sandGrain[0] - 1, sandGrain[1] + 1)
                continue

            # Check down-right
            elif (sandGrain[0] + 1, sandGrain[1] + 1) not in blockers and sandGrain[1] + 1 != rockFloor:
                sandGrain = (sandGrain[0] + 1, sandGrain[1] + 1)
                continue

            # Sand is at rest
            else:
                sandCoordinates.add(sandGrain)
                sandResting = True

    print('Total resting sand is: ' + str(len(sandCoordinates)))