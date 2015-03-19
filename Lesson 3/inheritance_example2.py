class Parent():
    def __init__(self, last_name, city_of_birth):
        self.last_name = last_name
        self.city_of_birth = city_of_birth

class Child(Parent):
    def __init__(self, last_name, city_of_birth, school):
        Parent.__init__(self, last_name, city_of_birth)
        self.school = school

george = Child("Bush", "New Haven", "Yale")
print george.last_name
print george.city_of_birth
print george.school

