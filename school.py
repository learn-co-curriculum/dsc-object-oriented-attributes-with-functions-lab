class School:
    def __init__(self, name):
        self.name = name
        self.roster = {}
    def add_student(self, name, grade):
        if grade in self.roster:
            self.roster[grade].append(name)
        else:
            self.roster[grade] = [name]

        #Alternatively, this could be written as:
        #self.roster[grade] = self.roster.get(grade, []).append(name)
    def grade(self, grade):
           return self.roster[grade]
    def sort_roster(self):
            new_dict = self.roster
            for key in new_dict:
                new_dict[key].sort()
            return new_dict
