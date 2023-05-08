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
            if num in used_list:
                break
        if num % 2 == 1:
            num = (3*num) + 1
    # outside while loop
    # add num to db
    db.createItem(num_before_change)

def startTestingNumbers():
    print("Started Testing Numbers.")
    db = numDB()
    used_list = db.getDB()
    print("used_list:", used_list)
    if used_list == []:
        used_list.append(RealDictRow([('num', 1)]))
    latest_num = (used_list[-1])['num']
    for i in range(latest_num, latest_num + 1_000_000):
        testNumber(i)
    startTestingNumbers()


    