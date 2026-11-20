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
e1=employee(15000,30,"good","madhu")
e2=employee(13000,20,"average","shalini")
e3=employee(100000,25,"good","madhushalini")
e1.show()
e2.show()
e3.show
e1.salary_perday()
e2.salary_perday()
e3.salary_perday()


        