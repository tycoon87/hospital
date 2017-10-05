class Patient(object):
    def __init__(self, idNum, name, allergies, bedNum):
        self.idNum = 0
        self.name = name
        self.bedNum = 0
        self.allergies = allergies
class Hospital(object):
    def __init__(self, pList, hName, Capacity):
        self.pList = []
        self.hName = hName
        self.Capacity = 100
    def admit(self, pList, name):
        self.patients += 1
        self.bed += 1
        if self.patients >= self.capacity:
            print "The hospital is full."
        else:
            print "Admission is complete."
    def discharge(self):
        if self.capacity >= 10:
            self.patients -= 1
            self.bed -= 1

#************************************************

class Hospital(object):
    def __init__(self, patients, hos_name, capacity):
     self.patients = []
     self.hos_name = hos_name
     self.capacity = 200
    
    def admit(self):
        self.patients += 1
        self.bed += 1
        if self.patients >= self.capacity:
            print "The hospital is full."
        else:
            print "Admission is complete."
    def discharge(self):
        if self.capacity >= 50:
            self.patients -= 1
            self.bed -= 1
    def display(self):
		print self.ID
		print self.name
		print self.allergies
		print self.bed_num
        
class Patient(object):
    def __init__(self, Id, name, allergies, bed):
         self.Id = 0
         self.name = name
         self.allergies = allergies
         self.bed = 0
    def display(self,):
		print self.name
		print self.allergies
		print self.bed_num
patient1 = Patient(1, "John Doe", "Fish,", 1).display()
