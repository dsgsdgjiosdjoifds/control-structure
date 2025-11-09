facebook = True
twitter = False
instagram = True

account_count = 0

if facebook:
    account_count += 1

if twitter:
    account_count += 1

if instagram:
    account_count += 1

if account_count >= 2:
    print("You are a good influencer!")
else:
    print("You are a bad influencer...")