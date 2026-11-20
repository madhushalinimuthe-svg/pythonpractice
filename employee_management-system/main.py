#OPPS
class employee:
    def __init__(self,salary,working_days,work_status,employee_name):
        self.salary=salary
        self.working_days=working_days
        self.work_status=work_status
        self.employee_name=employee_name
    def show(self):
        print("salary :",self.salary)
        print("working_days :",self.working_days)
        print("work_status :",self.work_status)
        print("employee_name :",self.employee_name)
    def salary_perday(self):
        pds=self.salary/self.working_days
        print("salary_perday :",pds)
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
e1.show()
e1.work()
e2.show()
e2.work()
e3.show()
e3.work()
m1.show()
m1.work()

        