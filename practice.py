chat = [
    "2025-06-12 14:00:11 | alice@example.com: Hey Bob, you suck!",
    "2025-06-12 14:00:15 | bob99@gmail.com: Shut up idiot!",
    "2025-06-12 14:00:18 | alice@example.com: Sorry bro 😅"
]

def mask_email(email):
    user,domain=email.split('@')
    user_mask=user[0]+'*'*(len(user)-2)+user[-1]
    email_mask=user_mask+'@'+domain
    return email_mask

def cencor_msg(msg):
    msg=msg.lower()
    badwords=['suck','idiot','shut up']
    for word in badwords:
        if word in msg:
            maskword=word[0]+'*'*(len(word)-2)+word[-1]
            msg=msg.replace(word,maskword)
    return msg

    



for line in chat:
    timestamp,rest=line.split('|')
    timestamp.strip()
    email,msg=rest.split(':')
    email,msg=email.strip(),msg.strip()
    clean_email=mask_email(email)
    clean_msg=cencor_msg(msg)
    print(f'{timestamp}|{clean_email} {clean_msg}')
      
     
    