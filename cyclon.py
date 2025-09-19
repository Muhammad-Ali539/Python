height=int(input('Enter you height:'))
credits=int(input('Enter your credits:'))
if height>=137 and credits>=10:
    print('Enjoy The Ride!')
elif height<137 and credits>=10:
    print('You are not tall enough')
elif height>=137 and credits<=10:
    print('You dont Have enough credits')
else:
    print('You have not met either requirement:')