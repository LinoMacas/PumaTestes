def main():
    user = input('')
    user1 = convert(user)
    print(user1)

def convert(msg):
    msg1 = msg.replace(':)','🙂')
    msg2 = msg1.replace(':(','😔')
    return msg2

main()