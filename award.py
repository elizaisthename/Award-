# asking the user to input the swimming time
swim = int(input("Enter the time taken for swimming, in minutes, please: "))

# asking the user to input the cycling time
cycle = int(input("Enter the time taken for cycling, in minutes, please: "))

# asking the user to input the running time
run = int(input("Enter the time taken for running, in minutes, please: "))

total_minutes = swim+cycle+run

if total_minutes <= 100:
    print("Provincial colours")
elif total_minutes <= 105:
    print("Provincial Half Colours")
elif total_minutes <= 110:
    print("Provincial Scroll")
elif total_minutes >= 111:
    print("No award")
