from school import School

class Student(School):
  
  def __init__(self,fname, lname, age,form,reg_no):
    super().__init__(fname, lname, age)
    self.form = form
    self.reg_no = reg_no
    
    
  def activity(self):
    return "Studying"
    
  def getinfor(self):
    return self.fname, self.lname, self.age,self.form,self.reg_no
  
student1 = Student("Ken", "moza", 20, 3, "reg4656")
student2 = Student("Risa", "Izak", 24, 1, "reg4006")

print(student2.fname)
print(student1.activity())
print(student1.getinfor())