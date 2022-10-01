'''
precondition: possible_actions is the list defined below

Postconditions: 
    1. (welcome): A welcome message is on the console
    2. (user_complaint): user's response to "Please describe your emotional complaint in one punctuation-free line: "
    3. (how_long): how_long is the user's string response to "How many motnhs (between 1 and 99) have you experienced
    4. (month validity): EITHER how_long has filled the request form OR this terminated AND "Sorry,  illegal input. Eliza is quitting; run Eliza again is on the console
     5. (Advice):
     EITHER how_long < 3 RETURNS "Please return in * months' is on the console where * is the difference between 3 and how_long OR how_long >= 3 RETURNS teh phrases in possible_action are on seperate lines on teh console, each preceded by "Try " 
'''
# precondition 
possible_actions = ["taking up yoga.", "sleeping eight hours a night.", "relaxing.", "not working on weekends.", 'spending two hours a day with friends.']


# postcondition 1
print("Thank you for using Eliza300, a fun therapy program.\nPlease describe your emotional complaint in one punctuation-free line: ")


#postcondition 2
user_complaint = input()


#postcondition 3 
    # a. print the question with the user input
print("How many months (between 1 and 99) have you expereinced '" + user_complaint + "' ?")
    # b. create a how_long input 
how_long = input()


# postcondition 4
# if-else conditions that talks about validity put the biggest one first
if ((int(how_long) <= 1) or (int(how_long) >= 99)): 
    print("Sorry, illegal input. Eliza is quitting, run Eliza again.")
    import sys
    sys.exit()


# postcondition 5
min_months = 3 - int(how_long)
if int(how_long) < 3: 
    print("Please return in " + str(min_months)+ " month(s) if these feelings persist.")
if int(how_long) >= 3: 
    print (how_long + " months is significant. Sorry to hear that.")
    for advice in possible_actions:

        print("Try " + advice)