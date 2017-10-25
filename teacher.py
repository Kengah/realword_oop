from school import School

class Teacher(School):
  
  def __init__(self,fname, lname, age, subject, staff_id):
    super().__init__(fname, lname, age)
    self.subject = subject
    self.staff_id = staff_id
    
  def activity(self):
    return "Teaching"
    
teacher1 = Teacher("Mole", "Keth", 39, "Mathematics","stid123")
teacher2 = Teacher("Jack", "Mbeto", 56, "English","stid437")

print(teacher1.activity())