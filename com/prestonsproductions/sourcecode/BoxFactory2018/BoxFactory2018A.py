# TEAM NAME:
# TEAM NUMBER:
# PARTICIPANT NAMES:

# SOURCE CODE
# 2018 - Box Factory - Box Production
# DIVISION B/C

''' INSTRUCTIONS

SCENARIO: Box Factory - Box Production
DESCRIPTION: There are many aspects of a road trip where software can be used to generate reports
or calculate statistics. One task is generating a travel Log. Each of the questions below will break
down this large task into smaller (more manageable) tasks. By completing the questions, you will be able
to generate a custom travel log. The main function will call your questions (using your logic) and
print out the travel log. Some of your questions may require you to call previous functions.

1. For each question, write your code to solve each objective. (return the answer programmatically. ie via variables)
2. Each objective is worth a designated number of points. 112 Points Total.
3. Highest number of points wins. Question 19 is a tie breaker. If there is still a tie, question 18, 17 and so on will break the tie.
4. The main function will call and run all of the questions and print the production data. Do not modify this function.
5. Programs that do not run/compile will not be eligible to receive full points as determined by the Source Code rules.
6. Run your program often to test and check for errors.

INFORMATION: Some questions will use a list of tuples. The tuples will represent the length, width, and height of a box)
The structure will be:
[ (length, width, height), (length, width, height), ... ] 

GOOD LUCK! '''

# QUESTION 0: FACTORY PRODUCTION TITLE
# OBJECTIVE A (2): A name, number, and date are passed into the function below. (All strings) 
# Return the name, number, and date concatenated, each separated by a space and colon. ex) "Log : 01 : 01/01/2018"
def getBoxProductionTitle(name, number, date):
    
    return name + ' : ' + number + ' :' + date

# QUESTION 1: CALCULATE VOLUME
# OBJECTIVE A (2): Boxes can be made in all shapes and sizes. Length, width, and height are passed into the function.
# Calculate and return the volume.
def getVolume(l, w, h):
    
    return l*w*h

# QUESTION 2: CALCULATE SURFACE AREA
# OBJECTIVE A (3): When building a box, we need to know how much material we need (square units). Length, width, and height
# are passed into the function below. Calculate and return the total surface area for a box.
def getSurfaceArea(l, w, h):
    
    return (2*l*w) + (2*l*h) + (2*w*h)

# QUESTION 3: WILL IS FIT?
# OBJECTIVE A (3): The function below has two parameters. The first parameter is the volume of a box and the second
# parameter is the volume of an object. Write code to return true if the volume is greater than or equal to that of
# the object, otherwise return false. 
# Calculate and return the volume.
def isBoxLargeEnough(vBox, vObject):
    if (vBox >= vObject): return True
    return False

# QUESTION 4: TOTAL SURFACE AREA
# OBJECTIVE A (4): A list of numbers representing the surface area of a box is passed in to the function below.
# Calculate and return the total surface area of all the boxes in the list.
def getTotalSurfaceArea(boxes):
    total = 0
    for s in boxes:
        total += s
    return total

# QUESTION 5: AVERAGE SURFACE AREA
# OBJECTIVE A (4): A list of numbers representing the surface area of a box is passed in to the function below.
# Calculate and return the average surface area of the boxes. Do not round your answer.
def getAverageSurfaceArea(boxes):
    total = 0
    for s in boxes:
        total += s
    return total / len(boxes)

# QUESTION 6: SUM OF FACTORS
# OBJECTIVE A (4): A list of numbers representing the surface area of a box is passed in to the function below.
# Calculate and return the sum of the surface area's where the number is a factor of 3 and 5, but not 8.
def getSumOfFactors(boxes):
    total = 0
    for s in boxes:
        if (s % 3 == 0 and s % 5 == 0 and s % 8 != 0): total += s
    return total

# QUESTION 7: SLICING PRACTICE
# OBJECTIVE A (4): A list of numbers representing the volume of objects is passed in to the function below.
# For each number, reverse the order of the numbers. ex 932 -> 239, 49932 -> 23994. If the value is less than
# 100, do not reverse the number. Return the reversed list.
def reverseList(objects):
    r = []
    for i in objects:
        if i >= 100: r.append(str(i)[::-1])
        else: r.append(i) 
    return r

# QUESTION 8: TIME TO BUILD A BOX
# OBJECTIVE A (4): The function below has parameters for the length, width and height of a box.
# One box making machine produces box material at 40 square units per second. Use the getSurfaceArea() function
# to calculate the surface are, then return the time (seconds) it will take to produce that box.
# OBJECTIVE B (2): If the length or width is greater than 40 units the box cannot be produced in the machine.
# Return -1 in this scenario.
def getBoxBuildTime(l, w, h):
    if (l > 40 or w > 40): return -1
    return getSurfaceArea(l, w, h) / 40

# QUESTION 9: BOX COST
# OBJECTIVE A (4): The function below takes in two parameters. sqUnits represents the surface area in
# square units of a box. price represents the cost per square unit. Calculate and return the cost of 
# a box. Use the round() function and round your answer to 2 decimal places. ex round(6.77893, 2)
# OBJECTIVE B (2): If the box is bigger than 99 square units, the price per square unit is reduced by 
# $0.05.
def getBoxCost(sqUnits, price):
    if (sqUnits > 99): return round((sqUnits * (price-0.05)),2)
    return round((sqUnits * price),2)

# QUESTION 10: ADD ON COSTS
# OBJECTIVE A (4): There are add on costs associated with boxes. Below, the cost, material of the boxes, and
# number of boxes are passed into the function. Multiply the cost by the number associated with a specific 
# type of material:
# 'CARDBOARD' : 1.00, 'PLASTIC' : 1.10, 'METAL' : 1.20
# OBJECTIVE B (4): If the number of boxes is more than 10, there is a 10% discount on the total cost.
# OBJECTIVE C (4): If the material is 'METAL' there is an additional 0.10 fee per box.
def getBoxAddOnCost(cost, material, nbrBoxes):
    total = 0
    if 'CARDBOARD' == material:
        total = cost * 1.00
    elif 'PLASTIC' == material:
        total = cost * 1.10
    elif 'METAL' == material:
        total = cost * 1.20
        total += .10 * nbrBoxes
    if (nbrBoxes > 10): total = total - (total * .10)    
        
    return total

# QUESTION 11: BOX MATERIAL COUNT
# OBJECTIVE A (4): A special order has requested that boxes with a surface area less than 400 be made or 'CARDBOARD',
# greater than or equal to 400 be made of 'PLASTIC' and greater than 899 be made of 'METAL'. A List of 
# surface area has been passed into the function below. Calculate and return in a tuple what percentage of the boxes
# are card board, plastic, and metal. ex. (60,10,30).
# OBJECTIVE B (2): Format the numbers as Integers
def getMaterialPercentage(boxes):
    c = 0
    p = 0
    m = 0
    for box in boxes:
        if box < 400: c += 1
        elif box >= 400 and box < 900: p += 1
        elif box >= 900: m += 1
        
    c = int(c / len(boxes) * 100)
    p = int(p / len(boxes) * 100)
    m = int(m / len(boxes) * 100)

    return (c,p,m)

# QUESTION 12: TOTAL BUILD TIME
# OBJECTIVE A (6): The function below has one parameter which is a list of tuples. Each tuple represents the 
# length, width, and height of a box in indices (0,1,2) respectively. Calculate how long it will take to build
# all boxes in the list. Use the getBoxBuildTime() function to calculate the size of each box. If -1 is returned,
# from getBoxBuildTime(), do not count that box. (Time in seconds)
def getTotalBuildTime(boxes):
    total = 0
    for box in boxes:
        time = getBoxBuildTime(box[0],box[1],box[2])
        if (time > -1): total += time
    return total

# QUESTION 13: BUILD BOXES TO FIT
# OBJECTIVE A (6): The function below has one parameter that is a list of volumes. These volumes represent objects
# and they need to be put in to the smallest box possible (Disregard objects shape). Calculate the dimensions of
# the smallest box for the object, put the dimensions in a tuple, and append the tuple to a list. Return the list
# of boxes.
def getBoxes(objects):
    import math
    boxes = []
    for obj in objects:
        nbr = math.pow(obj, 1/3)
        boxes.append((nbr,nbr,nbr))
    return boxes

# QUESTION 14: PERFECT SQAURES
# OBJECTIVE A (6): The Source Code box factory puts special stickers on boxes where the surface area is a perfect
# square (the number is the product of two equal integers). A number is passed into the function below. If the number
# is a perfect square return True, otherwise return false.
def needsPerfectSqaureSticker(number):
    for i in range(1, number):
        if (i*i == number): return True
        
    return False

# QUESTION 15: PYTHOGOREAN TRIPLES
# OBJECTIVE A (6): A pythagorean triple can be explained as three numbers (a,b,c) which fit the equation
# a**2 + b**2 = c**2. Loop through the list of tuples (boxes) and determine how many are pythagorean triples.
# Note, thre triple can be any combination of the numbers in the tuple. Return the count.
def getPythagoreanTriples(boxes):
    total = 0
    for box in boxes:
        if (box[0]**2 + box[1]**2 == box[2]**2
            or box[1]**2 + box[2]**2 == box[0]**2
            or box[2]**2 + box[0]**2 == box[1]**2):
            total += 1
    return total

# QUESTION 16: WILL IT FIT? PART 2
# OBJECTIVE A (6): Two lists (of numbers) with the same length are passed into the function below. The first list represents the 
# surface area of a box and the second list represents the volume of an object. Compare the each corresponding index 
# (saList[0] and vList[0], saList[1] and vList[1] and so on and determine if the object will fit in the box. Return
# a new list with True (if the object will fit) or False (if the object won't fit) in each corresponding index.
# HINT: Assume every box is a cube.
def isBoxesLargeEnough(saList, vList):
    import math
    fitList = []
    count = 0
    for box in saList:
        side = math.sqrt(box / 6)
        if side**3 >= vList[count]: fitList.append(True)
        else: fitList.append(False)
        count += 1

    return fitList

# QUESTION 17: MOST BOXES MADE
# OBJECTIVE A (8): The function below takes in a list of tuples (boxes) and an amount of box material 
# in square units, sqUnits. Calculate the maximum number of boxes in the list with the amount of box
# material given.
# HINT: Use getSurfaceArea() to find the surface area of each box. Make the smallest boxes first.
def getMostBoxesCount(boxes, sqUnits):
    total = 0
    unitcount = 0
    boxesSA = []
    for box in boxes:
        boxesSA.append(getSurfaceArea(box[0],box[1],box[2]))
    boxesSA.sort()
    for box in boxesSA:
        if ((unitcount+box) <= sqUnits):
            total += 1
            unitcount += box
    return total

# QUESTION 18: PRIME NUMBER BOXES
# OBJECTIVE A (8): The function below has one parameter, x, representing a number of boxes. Calculate the 
# VOLUME of x boxes and return the sum. The dimensions of each box must be a prime number. No two boxes
# can have the same dimensions. Start with (l,w,h) = 2, (l,w,h) = 3, (l,w,h) = 5 ...
def getPrimeNumberBoxesVolume(x):
    total = 0
    count = 0
    nbr = 2
    while (count < x):
        prime = True
        for i in range(1,nbr):
            if (nbr % i == 0 and i > 1):
                prime = False
        if (prime):
            total += (nbr**3)
            count += 1
        nbr += 1
    return total

# QUESTION 19: BOX FREESTYLE
# OBJECTIVE A (4): The function below has one parameter, boxes, which is a list of tuples. (as used earlier). Write 
# your own code to calculate a statistic or generate useful data. Return your results in any format.
# OBJECTIVE B (2): Write a two sentence comment explaining what your function does.
# OBJECTIVE C (2): Use at least one previous function from this test in your function.
# OBJECTIVE D (2): 
def getStatistics(boxes):

    return ''



###############################
# MAIN FUNCTION
# NOTE: It is in your best interest to not modify values in this function.
# Input for the programming questions is test data. The supervisor will use 
# different values to grade your program.
###############################
def main():
    
    # Boxes Surface Area
    boxesSF = [712,349,756,349,343,114,234,215,635,284,772,783,377,392,871,771,442,744,946,223,416,404,710,956,275,378,
               745,688,676,373,733,884,365,678,954,329,804,550,404,218,514,138,927,542,248,968,340,728,520,301,377,785,
               403,223,488,114,110,450,779,176,672,278,706,385,873,238,843,156,340,250,934,286,872,185,258,454,183,790,
               522,325,348,633,888,263,503,830,311,595,654,195,581,148,427,193,986,583,324,822,258,538]
    
    # Boxes
    boxes = [(1,16,27),(36,3,7),(9,15,31),(8,11,27),(17,15,6),(1,36,7),(12,41,42),(11,38,6),(27,38,3),(6,14,18),(19,37,10),
             (21,34,18),(5,14,3),(23,11,21),(41,35,38),(10,12,29),(37,12,19),(35,21,28),(19,5,28),(17,18,24),(42,16,20),
             (27,15,3),(38,1,9),(6,29,5),(10,29,20),(14,14,34),(9,1,1),(3,16,37),(38,41,29),(42,9,35),(2,20,28),(20,42,7),
             (2,36,28),(2,11,6),(11,24,26),(18,28,14),(5,5,23),(36,41,35),(12,4,19),(7,22,23),(15,22,3),(10,40,38),(25,30,18),
             (11,10,30),(35,33,20),(26,1,22),(5,32,38),(41,2,5),(40,37,17),(15,17,8),(19,30,25),(20,36,10),(22,17,35),(34,14,35),
             (20,8,9),(26,18,6),(38,8,39),(20,31,33),(33,39,20),(36,41,4),(3,38,13),(9,6,26),(5,15,24),(7,15,20),(25,2,6),(19,18,29),
             (26,21,19),(16,40,31),(38,19,12),(37,4,28),(26,5,22),(10,33,33),(34,42,29),(31,7,23),(24,42,6),(39,35,8),(21,27,15),
             (20,42,24),(34,39,13),(13,26,25),(7,13,13),(29,16,38),(14,38,19),(1,19,39),(9,9,15),(35,4,15),(10,41,23),(34,15,20),
             (38,37,38),(26,42,33),(24,19,5),(14,31,37),(27,30,21),(12,35,37),(7,19,7),(19,1,22),(34,14,7),(38,14,33),(36,16,9)]
    
    # Objects Volume
    objects = [362,35,374,696,417,129,486,456,584,935,273,314,778,220,299,156,552,226,683,217,827,482,635,200,855,273,
               745,750,387,793,707,337,974,147,130,586,312,585,635,949,217,315,843,420,209,279,156,527,357,249,681,505,
               972,920,812,320,809,654,702,563,652,599,587,740,680,673,702,263,702,932,562,421,453,23,898,485,968,620,
               792,205,179,92,362,2,89,600,18,514,75,110,976,872,458,44,642,411,437,539,233, 1000]
    
    # Print Question Answer 112 Points Total
    print('Source Code - Division B/C - Box Factory - Box Production')
    
    print('QUESTION 0 OBJECTIVE A (2): '+str(getBoxProductionTitle('The Source Code Box Production', '00022', '01/13/2019'))) # The Source Code Box Production : 00022 :01/13/2019
    print('Question 1 OBJECTIVE A (2): '+str(getVolume(10,20,5))) # 1000
    print('Question 2 OBJECTIVE A (3): '+str(getSurfaceArea(4,5,10))) # 220
    print('Question 3 OBJECTIVE A (3): '+str(isBoxLargeEnough(12, 11))) # True
    print('Question 4 OBJECTIVE A (4): '+str(getTotalSurfaceArea(boxesSF))) # 50613
    print('Question 5 OBJECTIVE A (4): '+str(getAverageSurfaceArea(boxesSF))) # 506.13
    print('Question 6 OBJECTIVE A (4): '+str(getSumOfFactors(boxesSF))) # 645
    print('Question 7 OBJECTIVE A (4): '+str(reverseList(objects))) # ['263', 35, '473', '696', '714', '921', '684', '654', '485', '539', '372', '413', '877', '022', '992', '651', '255', '622', '386', '712', '728', '284', '536', '002', '558', '372', '547', '057', '783', '397', '707', '733', '479', '741', '031', '685', '213', '585', '536', '949', '712', '513', '348', '024', '902', '972', '651', '725', '753', '942', '186', '505', '279', '029', '218', '023', '908', '456', '207', '365', '256', '995', '785', '047', '086', '376', '207', '362', '207', '239', '265', '124', '354', 23, '898', '584', '869', '026', '297', '502', '971', 92, '263', 2, 89, '006', 18, '415', 75, '011', '679', '278', '854', 44, '246', '114', '734', '935', '332', '0001']
    
    print('Question 8 OBJECTIVE A (4): '+str(getBoxBuildTime(10,20,30))) # 55.0
    print('Question 8 OBJECTIVE B (2): '+str(getBoxBuildTime(39,41,30))) # -1
    
    print('Question 9 OBJECTIVE A (4): '+str(getBoxCost(99, 0.24))) # 23.76
    print('Question 9 OBJECTIVE B (2): '+str(getBoxCost(100, 0.24))) # 19.0
    
    print('Question 10 OBJECTIVE A (4): '+str(getBoxAddOnCost(150, 'CARDBOARD', 8))) # 150.0
    print('Question 10 OBJECTIVE B (4): '+str(getBoxAddOnCost(150, 'PLASTIC', 11))) # 148.5
    print('Question 10 OBJECTIVE C (4): '+str(getBoxAddOnCost(150, 'METAL', 9))) # 180.9
    
    print('Question 11 OBJECTIVE A (4): '+str(getMaterialPercentage(boxesSF))) # (44.0, 49.0, 7.000000000000001) or (44, 49, 7)
    print('Question 11 OBJECTIVE B (2): '+str(getMaterialPercentage(boxesSF))) # (44, 49, 7)
    
    print('Question 12 OBJECTIVE A (6): '+str(getTotalBuildTime(boxes))) # 4926.35
    print('Question 13 OBJECTIVE A (6): '+str(getBoxes(objects))) # [(7.126935967201602, 7.126935967201602, 7.126935967201602), (3.2710663101885897, 3.2710663101885897, 3.2710663101885897), (7.20483214721452, 7.20483214721452, 7.20483214721452), (8.862095243387268, 8.862095243387268, 8.862095243387268), (7.470999115478001, 7.470999115478001, 7.470999115478001), (5.05277434720856, 5.05277434720856, 5.05277434720856), (7.862224182626689, 7.862224182626689, 7.862224182626689), (7.697002262553609, 7.697002262553609, 7.697002262553609), (8.358678392762462, 8.358678392762462, 8.358678392762462), (9.7784616525042, 9.7784616525042, 9.7784616525042), (6.48715411671635, 6.48715411671635, 6.48715411671635), (6.7968843858592365, 6.7968843858592365, 6.7968843858592365), (9.197289686814337, 9.197289686814337, 9.197289686814337), (6.036810736797685, 6.036810736797685, 6.036810736797685), (6.686883076988654, 6.686883076988654, 6.686883076988654), (5.383212612087283, 5.383212612087283, 5.383212612087283), (8.203131859404694, 8.203131859404694, 8.203131859404694), (6.091199348919784, 6.091199348919784, 6.091199348919784), (8.806572225338611, 8.806572225338611, 8.806572225338611), (6.009245006917366, 6.009245006917366, 6.009245006917366), (9.386460059516399, 9.386460059516399, 9.386460059516399), (7.840594845883629, 7.840594845883629, 7.840594845883629), (8.595238034338408, 8.595238034338408, 8.595238034338408), (5.848035476425731, 5.848035476425731, 5.848035476425731), (9.49121995802933, 9.49121995802933, 9.49121995802933), (6.48715411671635, 6.48715411671635, 6.48715411671635), (9.065367701259413, 9.065367701259413, 9.065367701259413), (9.085602964160698, 9.085602964160698, 9.085602964160698), (7.287361631121842, 7.287361631121842, 7.287361631121842), (9.25602237474319, 9.25602237474319, 9.25602237474319), (8.908538705945451, 8.908538705945451, 8.908538705945451), (6.958943337186094, 6.958943337186094, 6.958943337186094), (9.91257118112387, 9.91257118112387, 9.91257118112387), (5.277632087904077, 5.277632087904077, 5.277632087904077), (5.065797019100886, 5.065797019100886, 5.065797019100886), (8.368209391204644, 8.368209391204644, 8.368209391204644), (6.782422886028333, 6.782422886028333, 6.782422886028333), (8.363446607369195, 8.363446607369195, 8.363446607369195), (8.595238034338408, 8.595238034338408, 8.595238034338408), (9.827025224202185, 9.827025224202185, 9.827025224202185), (6.009245006917366, 6.009245006917366, 6.009245006917366), (6.804092115953367, 6.804092115953367, 6.804092115953367), (9.44660721966867, 9.44660721966867, 9.44660721966867), (7.488872387218507, 7.488872387218507, 7.488872387218507), (5.934472140399941, 5.934472140399941, 5.934472140399941), (6.534335077087572, 6.534335077087572, 6.534335077087572), (5.383212612087283, 5.383212612087283, 5.383212612087283), (8.077374240743945, 8.077374240743945, 8.077374240743945), (7.093970944750709, 7.093970944750709, 7.093970944750709), (6.291194551556287, 6.291194551556287, 6.291194551556287), (8.79796785031895, 8.79796785031895, 8.79796785031895), (7.963374241789242, 7.963374241789242, 7.963374241789242), (9.905781746683878, 9.905781746683878, 9.905781746683878), (9.725888262188558, 9.725888262188558, 9.725888262188558), (9.329363390985685, 9.329363390985685, 9.329363390985685), (6.839903786706787, 6.839903786706787, 6.839903786706787), (9.317859848626759, 9.317859848626759, 9.317859848626759), (8.68012373555622, 8.68012373555622, 8.68012373555622), (8.88748820522211, 8.88748820522211, 8.88748820522211), (8.257263269927625, 8.257263269927625, 8.257263269927625), (8.671266460286839, 8.671266460286839, 8.671266460286839), (8.429638310387759, 8.429638310387759, 8.429638310387759), (8.372966759705923, 8.372966759705923, 8.372966759705923), (9.045041696510273, 9.045041696510273, 9.045041696510273), (8.793659344316357, 8.793659344316357, 8.793659344316357), (8.763380887467774, 8.763380887467774, 8.763380887467774), (8.88748820522211, 8.88748820522211, 8.88748820522211), (6.4069585771855575, 6.4069585771855575, 6.4069585771855575), (8.88748820522211, 8.88748820522211, 8.88748820522211), (9.767992199474913, 9.767992199474913, 9.767992199474913), (8.252371525139433, 8.252371525139433, 8.252371525139433), (7.49481122585905, 7.49481122585905, 7.49481122585905), (7.680085719529357, 7.680085719529357, 7.680085719529357), (2.8438669798515654, 2.8438669798515654, 2.8438669798515654), (9.64773676867724, 9.64773676867724, 9.64773676867724), (7.856828007847996, 7.856828007847996, 7.856828007847996), (9.8921748864974, 9.8921748864974, 9.8921748864974), (8.527018983281597, 8.527018983281597, 8.527018983281597), (9.252130018365483, 9.252130018365483, 9.252130018365483), (5.896368539970366, 5.896368539970366, 5.896368539970366), (5.635740794544236, 5.635740794544236, 5.635740794544236), (4.514357435474001, 4.514357435474001, 4.514357435474001), (7.126935967201602, 7.126935967201602, 7.126935967201602), (1.2599210498948732, 1.2599210498948732, 1.2599210498948732), (4.464745095584537, 4.464745095584537, 4.464745095584537), (8.434326653017491, 8.434326653017491, 8.434326653017491), (2.6207413942088964, 2.6207413942088964, 2.6207413942088964), (8.01040313265657, 8.01040313265657, 8.01040313265657), (4.217163326508746, 4.217163326508746, 4.217163326508746), (4.791419857062784, 4.791419857062784, 4.791419857062784), (9.9193513276846, 9.9193513276846, 9.9193513276846), (9.553712362070033, 9.553712362070033, 9.553712362070033), (7.708238778159992, 7.708238778159992, 7.708238778159992), (3.530348335326063, 3.530348335326063, 3.530348335326063), (8.626706236691353, 8.626706236691353, 8.626706236691353), (7.434993741615868, 7.434993741615868, 7.434993741615868), (7.588579337781814, 7.588579337781814, 7.588579337781814), (8.138223044397701, 8.138223044397701, 8.138223044397701), (6.153449493663682, 6.153449493663682, 6.153449493663682), (9.999999999999998, 9.999999999999998, 9.999999999999998)]
    print('Question 14 OBJECTIVE A (6): '+str(needsPerfectSqaureSticker(64))) # True
    print('Question 15 OBJECTIVE A (6): '+str(getPythagoreanTriples(boxes))) # 3
    print('Question 16 OBJECTIVE A (6): '+str(isBoxesLargeEnough(boxesSF, objects))) # [True, True, True, False, True, False, False, False, True, False, True, True, False, True, True, True, True, True, True, True, False, True, True, True, False, True, True, True, True, False, True, True, False, True, True, False, True, True, False, False, True, False, True, True, True, True, True, True, True, True, False, True, False, False, False, False, False, False, True, False, True, False, True, False, True, False, True, False, False, False, True, False, True, True, False, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, True, True, True, True, False, True, True, False]
    print('Question 17 OBJECTIVE A (8): '+str(getMostBoxesCount(boxes, 10000))) # 16
    print('Question 18 OBJECTIVE A (8): '+str(getPrimeNumberBoxesVolume(50))) # 130660163
    
    print('Question 19 OBJECTIVE A (4): '+str(getStatistics(boxes)))
    print('QUESTION 19 OBJECTIVE B (2): '+'Check for comment explaining function.')
    print('QUESTION 19 OBJECTIVE C (2): '+'Check if previous function in file was called.')
    print('QUESTION 19 OBJECTIVE D (2): '+'Check if import statement was used.')
    
main()