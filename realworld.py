class School(object):
  """ school super class """
  
  def __init__(self, fname, lname, age):
    self.fname = fname
    self.lname = lname
    self.age = age
    
  def fullname(self):
    return "{} {}".format(self.fname, self.lname)
    
  def Activity(self):
    return "I"
      
    
class Student(School):
  
  def __init__(self,fname, lname, age,form,reg_no):
    super().__init__(fname, lname, age)
    self.form = form
    self.reg_no = reg_no
    
    
  def activity(self):
    return "Studying"
    
  def getinfor(self):
    return self.fname, self.lname, self.age,self.form,self.reg_no
    
    
class Teacher(School):
  
  def __init__(self,fname, lname, age, subject, staff_id):
    super().__init__(fname, lname, age)
    self.subject = subject
    self.staff_id = staff_id
    
  def activity(self):
    return "Teaching"
    
class Parent(School):
  def __init__(self,fname, lname, age, role):
    super().__init__(fname, lname, age)
    self.role = role
    
  def activity(self):
    return "Paying school fees"
    
student1 = Student("Ken", "moza", 20, 3, "reg4656")
student2 = Student("Risa", "Izak", 24, 1, "reg4006")
    
teacher1 = Teacher("Mole", "Keth", 39, "Mathematics","stid123")
teacher2 = Teacher("Jack", "Mbeto", 56, "English","stid437")

parent1 = Parent("Mawese", "Nord", 69, "PTA")

print(student1.activity())
print(student1.getinfor())
    
    
    
  
  