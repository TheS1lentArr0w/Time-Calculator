import math
hours = 0
minutes = 0

def user_input():
    while True:
        user_in = input("Input: ")
        # lowercase everything to allow for 'Q' or 'q' to quit, also doesn't affect hours:minutes
        user_in = user_in.lower()

        if user_in in ['q']:
            return user_in 

        # Past this, the input should be a time
        # Need to add input validation
        # Condition 1: == 2 digits after ':'
        # Condition 2: the 2 digits after ':' max 59
        user_in = user_in.split(':')
        if len(user_in[1]) != 2:
            print("Sorry, the minutes value must be 2 digits.")
        elif int(user_in[1]) > 59:
            print("Sorry, the maximum number of minutes is 59.")
        else:
            return ':'.join(user_in)

def input_manipulator(user_in):
    user_in = user_in.split(':')
    return int(user_in[0]), int(user_in[1])

def print_output(hours, minutes):
    print(f"Total time: {hours}:{minutes}")

def total_time(hours,minutes):
    hours += math.floor(minutes/60)
    minutes = minutes%60
    return hours,minutes

def intro():
    print("Time Calculator")
    print("The calculator is defaulted into a time summation.")
    print("\n")
    print("Enter the times in the format 'hours:minutes'")
    print("After entering all your times, quit by entering 'q'.")
    print("\n")
    print("If you would like to find the duration of time between \na start and end time, please enter 'a'\n")


intro()
# Main input loop
while True:
    user_in = user_input()

    if user_in == 'q':
        break
    
    new_hours, new_minutes = input_manipulator(user_in)
    hours += new_hours
    minutes += new_minutes
    
hours,minutes = total_time(hours,minutes)

print_output(hours,minutes)