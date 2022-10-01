'''
Postconditions 
    - will need to use a function to run in the beginning
    1. (welcome): a welcome message is on the console 
    2. (user_complaint): user's respon se in reply to "please state your complaint: "
    3. (observed_complaint_type): observed complaint_type = get_complaint_type(user_complaint)
    4. (advice displayed): either "You have depression" OR nothing is displayed accoring to observed_complaint_type
'''
key_words = ['depress', 'sad', 'down']

def get_complaint_type(func_user_entry): 
    # input the adding onto the list to rip though
    target = set()
    for response in key_words:
        if response in func_user_entry.lower(): 
            target.add("bull's eye")
    return target 
# postcondition 01
print("Thank you for using Eliza300, a fun therapy program.\nPlease state your complaint:")
# postcondition 02
user_entry = input()
# postcondition 03
observed_complaint_type = get_complaint_type(user_entry)
# postcondition 04
if len(observed_complaint_type) > 0:
    print("You have depression")