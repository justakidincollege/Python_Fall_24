# Sorting list assignment

# Establish a list
names=[]

# Ask user for names
for i in range(5):
    name=input("Please input a name ")
    names.append(name)

# Start bubble sorting
swapped=True
for i in range(0, len(names)):
    names[i]=names[i].lower()
while swapped:
    swapped=False
    for i in range(len(names)-1):
        if names[i]>names[i+1]:
            swapped=True
            names[i], names[i+1]=names[i+1],names[i]

# Print list
print(names)

# Reverse list
names.reverse()

# Print reverse list
print(names)
