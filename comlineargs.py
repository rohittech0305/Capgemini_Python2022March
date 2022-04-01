import sys

#argv , exit
if len(sys.argv) != 3:
    print("USAGE: {} {} {} ".format(sys.argv[0], 'UserName','Acount_Number'))
    print("Please rerun with valid input.")
    sys.exit(0)
    
print("Programm name is :",sys.argv[0])
print("User Name:",sys.argv[1])
print("Account Number:", sys.argv[2])
