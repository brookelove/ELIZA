'''
precondition: possible_actions is the list defined below

postconditions: 
    1. (welcome): a welcome message is on the console 
    2. (user_complaint): users response to "please describe your emotional complaint in one punctuation-free line:"
    3. (how_long): users strign respnse to "how many months (between 1 and 99) have you expereinced ...?"
    4. (month validity): EITHER it is valif OR it will terminate AND print "sorry, illegal input. Eliza is quitting, run Eliza again on the console
    5. (advice): EITHER how_long >= 3 OR "please return in * months" is on the console where * is 3 minus how_long 
    6. (actions_not_taken): consists of the actions (elements) possible_actions that the user asnwered 'n' to when questioned "have you tried?"
    7. (summarized): Eliza300 recommmended that teh user take the following actions + actions_not_taken 
'''
# precondition 
possible_actions = ["taking up yoga.", "sleeping eight hours a night.", "relaxing.", "not working on weekends.", 'spending two hours a day with friends.']
advice_choices = []

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
# postcondition 6 
    for actions_not_taken in possible_actions:
        print("Have you tried " + actions_not_taken + "? Please answer y or n: ")
        yes_no_answer = input()
        if(yes_no_answer[0] == 'y') or (yes_no_answer[0] == 'Y'): 
            advice_choices.append(actions_not_taken)
# postcondition 7
print("Eliza300 recommends that the user take these actions:")
for each_advice in advice_choices: 
    print( "- " + each_advice)