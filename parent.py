from school import School

class Parent(School):
  def __init__(self,fname, lname, age, role):
    super().__init__(fname, lname, age)
    self.role = role
    
  def activity(self):
    return "Paying school fees"
    

parent1 = Parent("Mawese", "Nord", 69, "PTA")

print(parent1.lname)