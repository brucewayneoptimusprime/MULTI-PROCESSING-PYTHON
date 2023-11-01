#In this code, we will explain why multi processing in python
#is much faster than normal calculation methods. it is also important to note that
#multi-threading is not possible in python due to something known as the
#"GLOBAL INTERPRETOR LOCK". so, the only way to speed up our process is through the
#divisionof task in sub processes.

import multiprocessing as mp
import time
import math

list_a=[]
list_b=[]
list_c=[]

def calc_1(numbers):
    for number in numbers:
        list_a.append(math.sqrt(number**3))

def calc_2(numbers):
    for number in numbers:
        list_b.append(math.sqrt(number**4))

def calc_3(numbers):
    for number in numbers:
        list_c.append(math.sqrt(number**5))

#Now,let's measure the time difference between a simple non divided and single process code and
#the one which uses process division

if __name__ =='__main__':

    number_list=list(range(1000000))

    p1=mp.Process(target=calc_1,args=(number_list,))
    p2=mp.Process(target=calc_2,args=(number_list,))
    p3=mp.Process(target=calc_3,args=(number_list,))

    begin=time.time()
    p1.start()
    p2.start()
    p3.start()
    end=time.time()

    print(end-begin)

    begin2=time.time()
    calc_1(number_list)
    calc_2(number_list)
    calc_3(number_list)
    end2=time.time()

    print(end2-begin2)





