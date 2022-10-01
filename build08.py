
'''
Precondition...
        1. user_input_complaint is a string 
        2. complaint_type is a list of strings 
        3. key_words is a list of list of strings
        4. complaint_type and keywords are the same length
    Returns...
    observed_complaint_type, whic consists fo the ondicies in complaint_type that correspond to key_words elements partly in user_input_complaint

            Ex. If the user enters "I've been saddeded by the world conflicts", the function returns the set consising of 0 and 1 because it contains "sad" and "conflict"
Postconditions
    1. (welcome): a welcome message is on the console 
    2. (user_complaint): user's response to in response to "Please state complaint:"
    3. (observed_complaint_types): observed_complaint_types = get_complaint_type(user_complaint)
    4.(Indives displayed): observed_complaint_types is on the console
'''
# precondition 02
complaint_type = ['Depression', 'Human Relations', 'Substance Abuse']
# precondition 03
key_words = [['depress', 'sad', 'down'], ['conflict', 'argument', 'mistreat', 'quarrel'],['drug', 'alcohol', 'drink','cocaine', 'opioid', 'heroin']]
# print(key_words[0])
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
# Postcondition 01
print("Thank you for using Eliza300, a fun therapy program.\nPlease state your complaint:")

#postcondition 02
user_complaint = input()

#postcondition 03 and precondition 01
obeserved_complaint_types = get_complaint_type(user_complaint)

print(obeserved_complaint_types)