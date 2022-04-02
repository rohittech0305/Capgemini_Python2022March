import multiprocessing
from time import sleep
def calc_square(numbers):
    for n in numbers:
        print("Square of {}:{}".format(n,n*n))
        sleep(1)

def calc_cube(numbers):
    for n in numbers:
        print("Cube of {}:{}".format(n,n*n*n))
        sleep(1)

if __name__=="__main__":
    print("PROGRAM STARTED RUNNING")
    arr=[1,2,3,4,5]

    p1=multiprocessing.Process(target=calc_square,args=(arr,))
    p2=multiprocessing.Process(target=calc_cube,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("DONE!")