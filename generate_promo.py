import sys,os
from checker.core_generate_promo import get_json_promo

#Generate json
if len(sys.argv) == 3:
    curr_fold = 0
    if ('amount' in str(sys.argv[1])) and ('group' in str(sys.argv[2])):
        amount = str(sys.argv[1])[len('amount')+1:]
        group = str(sys.argv[2])[len('group')+1:].replace('\'','')
        if amount.isdigit():
            get_json_promo(int(amount), group)
        else:
            print(f'''
            
                Amount is not a digit

            ''')
    else:
        print(sys.argv[1:])
        print(f'''
            Ouch!

            I don't know such a parameter
        ''')

# Open web-app
elif len(sys.argv) == 2:
    if ('start' == str(sys.argv[1])):
        os.system(f"python manage.py runserver")

#ERR
else:
    print(f'''
        Sorry, i need 2 parameter:
        - amount (amount of code)
        - group (group name)

        Nice to see u
    ''')
