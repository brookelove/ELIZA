'''
Postconditions
1 (Welcome): A welcome message is on the console
2 (Complaint): A complaint was entered by the user in response to a prompt
AND Eliza has responded "I am sorry to hear you report <the complaint entered by the user>"
'''
print("\nThank you for using Eliza300, a fun therapy program.\nPlease state your emotional complaint then hit 'ENTER':\n")

user_input = input()

print('\nI am sorry to hear you report "' + user_input + '"\n')