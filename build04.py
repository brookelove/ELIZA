'''
Precondition: possible_actions is the list defined below

Postconditions: 
    1. (welcome): A welocme message is on the console
    2. (user_complaint): user_complaint is the rspomse to a prompt for the user's complaint
    3. (how_long): how_long os the users string respnse to "how many months have you experienced...?" and Eliza300 sympathized, mentioning the duration
    4. (Advice): 
    EITHER how_long < 3 and AND return "please return in 3 months 
    OR how_long >= 3 AND the prases in possible_action are on seperate lines ont eh console, each with a Try before it 
'''
# precondition 
possible_actions = ["taking up yoga.", "sleeping eight hours a night.", "relaxing.", "not working on weekends.", 'spending two hours a day with friends.']
# postcondition 1
print("Thank you for using Eliza300, a fun therapy program.\nPlease describe your emotional complaint in one punctuation-free line: ")

#postcondition 2
user_complaint = input()

#postcondition 3 
    # a. print the question with the user input
print("How many months have you expereinced '" + user_complaint + "' ?")
    # b. create a how_long input 
how_long = input()
min_months = 3 - int(how_long)
# postcondition 4 
if int(how_long) < 3: 
    print("Please return in " + str(min_months)+ " month(s) if these feelings persist.")
if int(how_long) >= 3: 
    print (how_long + " months is significant. Sorry to hear that.")
    for advice in possible_actions:

        print("Try " + advice)