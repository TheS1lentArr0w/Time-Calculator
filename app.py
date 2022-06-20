hours = 0
minutes = 0

def user_input():
    user_in = input("Provide a time in the format 'hours:minutes'. (To exit, please enter 'q'): ")
    # lowercase everything to allow for 'Q' or 'q' to quit, also doesn't affect hours:minutes
    user_in = user_in.lower()
    
    # Need to add verification to ensure the input is num:num
    return user_in

# Main input loop
while True:
    user_in = user_input()

    if user_in == 'q':
        break
    
    
    print('in while loop')

print('broke out of while loop')