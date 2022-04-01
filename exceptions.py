'''
4 clauses :
=========
try
except
else
finally
'''

try:
    with open('days.txt','r') as fh:
        print(fh.read())
    # num=int(input("Enter a number:"))
    # res=100/num
    # print("RESULT :", res)
    #
    # age=int(input("Enter your age:"))
    # if age < 0 or age > 100:
    #     raise ValueError("Age cannot be less than 0 or greater than 100")
    # print("AGE:",age)

    #print("Chennai"+100)

except FileNotFoundError as e:
    print("FILE IS NOT AVAILABLE, PLEASE CHECK. ", e)
except ZeroDivisionError as e:
    print("CAN'T BE DIVIDED BY ZERO:",e)
except ValueError as e:
    print("RECEIVED:",e)
except Exception as e:
    print("RECEIVED NEW EXCEPTION:",e)
# else:
#     print("I AM FROM ELSE BECUASE THERE IS NO EXCEPTION")
# finally:
#     print("I RUN ALWAYS REGARDLESS OF EXCEPTION")
#
print("CAPGEMINI - TRAINING PROGRAMS")