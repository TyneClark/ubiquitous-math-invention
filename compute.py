from db import *

def testNumber(num):
    db = numDB()
    used_list = db.getDB()
    num_before_change = num
    steps = []
    while num != 4:
        if num in steps:
            print("3N+1 Exception at:", num_before_change)
            return
        steps.append(num)
        if num % 2 == 0:
            num = num / 2
            if db.getOne(int(num)): # if the number already exists in the db then we can skip further calculations
                break
        if num % 2 == 1:
            num = (3*num) + 1
    # outside while loop
    # add num to db
    db.createItem(num_before_change)

def startTestingNumbers():
    print("Testing has begun.")
    print("10,000 numbers are being tested")
    db = numDB()
    used_list = db.getDB()
    #print("used_list:", used_list)
    #if used_list == []:
        #used_list.append(RealDictRow([('num', 1)]))
    latest_num = (used_list[-1])['num']
    for i in range(latest_num, latest_num + 10_000):
        testNumber(i)
    print(i, "was the last number tested of the above 10,000")
    startTestingNumbers()


    