# Functions in Python: "def" define the function

def greetings(name, course):
    print("Hi", name, " I am your classmate in", course)


greetings("Gabriela", "COP4814")


def _sum(a, b):
    return a + b


c = _sum(2, 3)
print(c)


def _double(x):
    return 2*x

professors = ["greg", "giri", "george", "julia"]


def get_len(lst):
    for i in lst:
        print(i.title(),"has",len(i), "characters.")


get_len(professors)




"""Object-Oriented Paradigm in Python"""

class COP4814Student():
    def __init__(self,first_name,last_name,panther_id,email,grade):
        self.first_name = first_name
        self.last_name = last_name
        self.panther_id = panther_id
        self.email = email
        self.grade = grade

    def current_grade(self):
        return "{0} {1}\'s current grade is {2}.".format(self.first_name,self.last_name,self.grade)

    def grade_mesage(self):
        return "{0} {1} will likely get an A is this course.".format(self.first_name,self.last_name)

        return "{0} {1} you will not ge an A.".format(self.first_name,self.last_name)

andriusB = COP4814Student("Andrius","Bubelis",12001,"adrius@mail",87)
print(andriusB)
print(andriusB.grade)

## Change Grade from 87 to 89
andriusB.grade =89

print(andriusB.panther_id)
print(andriusB.grade)
print(andriusB.current_grade())

## Write a for loop in range 20 to print each value to the power of 2

lst=[x**2 for x in range(20)]
print(lst)

## Write a list comprehesion to count the number of "g" in each element of list professors
# Hint: use method.count() to get the number of occurrences of a certain character

lst2 =[y.count("g") for y in professors]
print(lst2)

