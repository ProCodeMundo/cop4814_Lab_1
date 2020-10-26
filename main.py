message = "Hello Cop 4814"

print(message)

first_name = "Ruben"

# example of comments

print(first_name.title())
print(first_name.upper())
print(first_name.lower())

first_name = "Ada"
last_name = "Lovelace"

print(first_name.title(), last_name.title(), "is considered the first computer programmer.")

full_name = first_name + " " + last_name

print(full_name)

# List:

professors = ["greg", "Leo", "giri"]
print(professors)
print(len(professors))

# accesing element of the list
# name of list, square brackets, the Index
print(professors[0])

#the second element:
print(professors[1])

#the third element:
print(professors[2])

#print(professor[3] the list index is out of range

professors.append("rick")
professors.append("michael")
professors.append("prabakar")

print(professors)

print(professors[0:2])#this ranfe output elements 0 and 1
print(professors[:2]) # you do not need to write 0
print(professors[2:4]) # this range outpus element 2 and 3
print(professors[3:6])

# For loop
# functions, for loops, if statement, classes, etc. " : "
for i in professors:
    print(i)

for j, k in enumerate(professors):
    print(k, "is in position", j)

print(professors[-1])
print(professors[-2])

print(professors.index("Leo"))

professors.sort()

print(professors)

professors.sort(reverse=True)

print(professors)

# the range method
for i in range(10):
    print(i)

for j in range(2,10):
    print(j)

for k in range(1,21,2):
    print(k)

# Dictionaries

released_date ={
    "iphone":2007,
    "iphone4":2010,
    "iphone7": 2016,
    "iphoneX":2017
}

print(released_date,type(released_date))
#To access values in a dictionary:
# name of dict, square bracket, the KEY

print(released_date["iphone"])

print(len(released_date))

profile = {
    "name" : "Ruben",
    "email": "Ruben910",
    "area" : ["military", "Health admin", "Steam"],
    "year" : 1983
}

print(profile["area"]) #printing the va