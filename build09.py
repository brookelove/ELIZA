'''
Postcondition:
    1. (welcome): a welcome message is on the console 
    2. (user_complaint): user's response in reply to "please state your complaint:"
    3. (observed_complaint_types): observed_complaint_types = get_complaint_types(user_complaint)
    4. (remidies displayed): remidies in advice_per_type corresponding to observed_complaint_types are on the monitor, one for each line
'''
complaint_type = ['Depression', 'Human Relations', 'Substance Abuse']

key_words = [['depress', 'sad', 'down'], ['conflict', 'argument', 'mistreat', 'quarrel'],['drug', 'alcohol', 'drink','cocaine', 'opioid', 'heroin']]

advice_per_type = [
    ['Get out more.', 'Take up a hobby that your love.'],
    ["Don't expect too much of people.", "Don't take offence easily."],
    ['Get Counseling.', "Don't delay action on conseling."]
]

def get_complaint_type(user_input_complaint): 
    target = set()
    # to get into the first list we need ot look at the range of the complaint_type
    for index in range(len(complaint_type)):
        # in order to look into the list and read the correct words, I have been looking at the correct key_words[index] 
        for diagnosis in key_words[index]: 
            if diagnosis.lower() in user_input_complaint.lower():
                # add current index of the diagnosis to the set 
                target.add(index)
    return target
# postcondition 01
print("Thank you for using Eliza300, a fun therapy program.\nPlease state your complaint: ")

# postcondition 02
user_complaint = input()

# postcondition 03
observed_complaint_types = get_complaint_type(user_complaint)
print(observed_complaint_types)

# postcondition 04
print("Here are some of the remidies that I suggest for, '" + user_complaint + "'")
for index in observed_complaint_types: 
    for remidies in advice_per_type[index]: 
        print(remidies)