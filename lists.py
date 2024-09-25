# List assignment

# Establish lists
days=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
steps=[]
total_steps=0
# Ask user for steps
for x in range(len(days)):
    day=days[x]
    print("How many steps did you walk on", day)
    step_1=int(input())
    steps.append(step_1)
    total_steps+=step_1

# Display steps for each day
for i in range(len(days)):
    day=days[i]
    step=steps[i]
    print("You walked", step,"steps on", day)

# Print total steps and average steps
print("You walked", total_steps,"total steps")
average=total_steps/7
print("You walked an average of", average,"steps")
