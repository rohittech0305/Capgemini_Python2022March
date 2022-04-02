class Employee():
    hike=1.5
    def __init__(self,fname,lname,sal):
        self.fname=fname
        self.lname=lname
        self.salary=sal
        self.email=self.fname+"_"+self.lname+'@capgemini.com'

    def fullname(self):
        return "{} {}".format(self.fname,self.lname)

    def appraisal(self):
        self.salary=int(self.salary*self.hike)

    @classmethod
    def create_object(cls,emp_info):
        fn,ln,pay=emp_info.split("-")
        return cls(fn,ln,int(pay))

    @staticmethod
    def is_workingday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return "Holiday"
        else:
            return "Workingday"

class Manager():
    def appraisal(self):
        self.salary = int(self.salary * 2)

class Developer(Employee,Manager):
    def __init__(self,fname,lname,salary,tech):
        self.tech=tech
        super().__init__(fname,lname,salary)
    def project_detail(self):
        print("{} is working as a {} Developer".format(self.fullname(), self.tech))

    def fullname(self,title):
        self.title=title
        print("{} {} {}".format(self.title,self.fname,self.lname))

    def sum_nums(self,*x):
        return sum(x)

    def appraisal(self):
        #Manager.appraisal(self)
        super(Employee,self).appraisal()

dev_1=Developer('Durga','Devi',100000,'Python')
dev_2=Developer('Satya','Ram',200000,'Java')

print(dev_1.salary)
dev_1.appraisal()
print(dev_1.salary)

# str1="Levin-Lenus-100000"
# str2="Pankaj-sharma-200000"
#
# emp_1=Employee.create_object(str1)
# emp_2=Employee.create_object(str2)
#
# import datetime
# tday=datetime.date(2022,4,1)
# print(Employee.is_workingday(tday))

