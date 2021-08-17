import random

stuList = ['alice', 'bob', 'cindy', 'david', 'ellen', 'frank', 'grace', 'hellen']
courseList  = [110, 213, 315, 316, 412, 121, 223, 326, 328, 422, 136, 238, 335, 336, 432, 140, 243, 345, 346, 448, 150, 253, 355, 356, 452]

needPreReq = [213, 412, 326, 422, 238, 345, 355, 452]

preReqValueDic = {213:110, 412:316, 326:223, 422:328, 238:136, 345:243, 355:253, 452:356}
finishedCourses = []
selectedCourses = []

class Person:
  def __init__(self, name):
    self.name = name

  def getName(self):
    return self.name

class Student(Person):
  
  def __init__(self, name, stuID, finishedCourses, selectedCourses):
    Person.__init__(self, name)
    self.stuID = stuID
    self.finishedCourses = finishedCourses
    self.selectedCourses = selectedCourses

  def getCourses(self):
    return self.selectedCourses

  def getSudentID(self):
    return self.stuID

  def getFinishedCourses(self):
    return self.finishedCourses
    
  def getSelectedCourse(self, courseList, preReqs):
    self.selectedCourses = []
    self.finishedCourses = []
    while((len(self.finishedCourses) != 3)):
      finishedCourse = courseList[random.randint(0, len(courseList) - 1)]
      if(finishedCourse not in preReqs):
        if(finishedCourse not in self.finishedCourses):
          if(int(finishedCourse) < 400):
            self.finishedCourses.append(finishedCourse)
    
    while((len(self.selectedCourses) != 3)):
      selectedCourse = courseList[random.randint(0, len(courseList) - 1)]
      if (selectedCourse not in self.selectedCourses):
        if(selectedCourse not in self.finishedCourses):
          self.selectedCourses.append(selectedCourse)
    return self.selectedCourses  

  def sendCourseRegistrationRequest(self, course, message):

      if (message == "Not Approved"):
          self.selectedCourses.remove(course)
          self.selectedCourses.append(Student.updateSelectedCourse(self))

  def updateSelectedCourse(self):
    while(self.selectedCourses != 3):
      newCourse = courseList[random.randint(0,len(courseList) - 1)]
      if(newCourse not in self.selectedCourses):
        if(newCourse not in needPreReq):
          if(newCourse not in self.finishedCourses):
            return newCourse
  def confirmRecievedMsg(self, msg):
    print('I am ' + self.name + ' and I have recieved: ' + msg)


class Advisor(Person):

  def __init__(self, name):
    Person.__init__(self, name)
  
  def approveSelectedCourse(self, course, stuFinishedCourses):
    for stuObj in studentObjList:
      if course in needPreReq:
        if preReqValueDic[course] not in stuFinishedCourses:
          return "Not Approved"
      else:
        return "Approved"
  
  def sendAnnouncement(self, msg, studentObjList):
    for stuObj in studentObjList:
      stuObj.confirmRecievedMsg(msg)
      

#I created a variable here called advisor that contains the Advisor instance
advisor = Advisor("Sherry")

StuCourseDic = {}
studentObjList = []
advisorObjList = []


#This part of my code creates the student objects
for name in stuList:
  studentObjList.append(Student(name, "88555", finishedCourses, selectedCourses))


#This part of my code creates the list of finished classes and initially selected classes and prints the finished classes
for stuObj in studentObjList:
  print(stuObj.getName() + ":")
  print("Finished courses are: ")
  tenativeCourses = stuObj.getSelectedCourse(courseList, needPreReq)
  print(stuObj.getFinishedCourses())
  
  #this part of my code will run through all the selected courses 3 times to check for deficiencies
  for course in tenativeCourses:
    message = advisor.approveSelectedCourse(course, stuObj.finishedCourses)
    stuObj.sendCourseRegistrationRequest(course, message)
  courses = stuObj.getCourses()
  for course in courses:
    message = advisor.approveSelectedCourse(course, stuObj.finishedCourses)
    stuObj.sendCourseRegistrationRequest(course, message)
  for course in courses:
    message = advisor.approveSelectedCourse(course, stuObj.finishedCourses)
    stuObj.sendCourseRegistrationRequest(course, message)
  StuCourseDic[stuObj.name] = stuObj.selectedCourses

#This part of my code prints out the final selected courses after they have been approved by the advisor
  print("The final approved courses are: ")
  print(stuObj.getCourses())
  print("\n")
