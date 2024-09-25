# Heart rate tracker assignment

# Create list of times druing day
time_slots=["morning","noon","afternoon","evening"]
heart=[]

# Ask for heart rate
for time in time_slots:
    heart_rate=int(input(f"Enter your heart rate for {time} "))
    heart.append([time, heart_rate])

# Display data
print(heart)

# Calulate average heart rate
total=0
for hearts in heart:
    total+=hearts[1]
average=round(total/len(heart))
print("You average heart rate is ", average)