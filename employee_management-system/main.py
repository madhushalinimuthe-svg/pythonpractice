#OPPS
from abc import ABC, abstractmethod
class employee(ABC):
    def __init__(self,salary,working_days,work_status,employee_name):
        self.__salary=salary
        self.working_days=working_days
        self.work_status=work_status
        self.employee_name=employee_name
    @abstractmethod
    def work(self):
        pass
    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
        if salary>0:
            self.__salary=salary
            print("salary updated successfully")
        else:
            print("invalid salary")
    def show(self):
        print("salary :",self.__salary)
        print("working_days :",self.working_days)
        print("work_status :",self.work_status)
        print("employee_name :",self.employee_name)
    def salary_perday(self):
        return self.__salary/self.working_days
class developer(employee):
    def __init__(self, salary, working_days, work_status, employee_name,language):
        super().__init__(salary, working_days, work_status, employee_name)
        self.language=language
    def show(self):
        super().show()
        print("Language used for code :",self.language)
    def work(self):
        print("writes code for company")
class manager(employee):
    def show(self):
        super().show()
        print("Role : manager")
    def work(self):
        print("managing the team")
e1=developer(15000,30,"good","madhu","python")
e2=developer(13000,20,"average","shalini","java")
e3=developer(100000,25,"good","madhushalini","python")
m1=manager(300000,30,"good","shalini varma")
print("old salary :",e1.get_salary)
e1.set_salary(40000)
print("updated salary :",e1.get_salary())
e1.show()
e1.work()
e2.show()
e2.work()
e3.show()
e3.work()
m1.show()
m1.work()


        