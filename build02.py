'''
Eliza300: Postconditions
1. (Welcome): A welcome message is on the console
2. (Complaint): A complaint was entered by the user in response to a prompt
3. (Duration): A duration was entered by user in response to a prompt
4. (Action Recommended): EITHER how long exceeds 2 months, and the phrase
   “ … months is too much time to go without help! Let's schedule a few sessions"
   is on the console
   OR the following is on the console:
   "Come back in a couple of months if this persists".
'''
print("\nThank you for using Eliza300, a fun therapy program.\nPlease state your emotional complaint then hit 'ENTER':")

user_input = input()

print('How many months has it been that you have experienced "' + user_input + '"')
months = input()
if int(months) <= 2: 
    print ("Come back in a couple of months if this persists")
if int(months) >=3:
    print(months + " months is too much time to go without help! Lets schedule a few sessions.")