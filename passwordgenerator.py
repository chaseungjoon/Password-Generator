import random
import string

def pw_generate(min_char, max_char, inc_num, inc_spc, inc_upp):
    spc = '~`!@#$%^&*()_-+={[}]|\:;"<,>.?/'
    pw_length = random.randint(min_char, max_char)
    #include or not include and generate
    if (inc_num == 'y'):
        if(inc_spc == 'y'):
            if(inc_upp == 'y'):
                #Must include - while loop
                while True:
                    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + spc
                    pw = ''.join(random.choices(chars, k = pw_length))
                    if any(ch.isdigit() for ch in pw) and any(ch.islower() for ch in pw) and any(ch.isupper() for ch in pw) and any(sym in spc for sym in pw):
                        break
            else:
                #Must include - while loop
                while True:
                    chars = string.ascii_lowercase + string.digits + spc
                    pw = ''.join(random.choices(chars, k = pw_length))
                    if any(ch.isdigit() for ch in pw) and any(ch.islower() for ch in pw) and any(ch.isupper() for ch in pw) and any(sym in spc for sym in pw):
                        break
        else:
            if(inc_upp == 'y'):
                #Must include - while loop
                while True:
                    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
                    pw = ''.join(random.choices(chars, k = pw_length))
                    if any(ch.isdigit() for ch in pw) and any(ch.islower() for ch in pw) and any(ch.isupper() for ch in pw):
                        break
            else:
                #Must include - while loop
                while True:
                    chars = string.ascii_lowercase + string.digits
                    pw = ''.join(random.choices(chars, k = pw_length))
                    if any(ch.isdigit() for ch in pw) and any(ch.islower() for ch in pw):
                        break
    else:
        if(inc_spc == 'y'):
            if(inc_upp == 'y'):
                #Must include - while loop
                while True:
                    chars = string.ascii_uppercase + string.ascii_lowercase + spc
                    pw = ''.join(random.choices(chars, k = pw_length))
                    if any(ch.islower() for ch in pw) and any(ch.isupper() for ch in pw) and any(sym in spc for sym in pw):
                        break
            else:
                #Must include - while loop
                while True:
                    chars = string.ascii_lowercase + spc
                    pw = ''.join(random.choices(chars, k = pw_length))
                    if any(ch.islower() for ch in pw) and any(sym in spc for sym in pw):
                        break
        else:
            if(inc_upp == 'y'):
                #Must include - while loop
                while True:
                    chars = string.ascii_uppercase + string.ascii_lowercase
                    pw = ''.join(random.choices(chars, k = pw_length))
                    if any(ch.islower() for ch in pw) and any(ch.isupper() for ch in pw):
                        break
            else:
                #Must include - while loop
                while True:
                    chars = string.ascii_lowercase
                    pw = ''.join(random.choices(chars, k = pw_length))
                    if any(ch.islower() for ch in pw):
                        break
    print("Your password is :",pw)
    end = input("")

print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print("┃     Welcome to Password Generator    ┃")
print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
print("                                        ")
print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print("┃  Default including lowercase letters ┃")
print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
print("                                        ")
print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print("┃        Made By Seung joon Cha        ┃")
print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
print("                                        ")

#define absolute minimum
minimum = 1

while True:
    #input minimum characters
     min_char = input("Type the minimum character limit for your password :")
    #min_char must be integer
     try:
        min_char = int(min_char)
     except:
        print("Wrong input. Type again.")
        continue
    #min_char must be greater than or equal to absolute minimum
     if (minimum > min_char):
        print("Your minimum character limit must be greater than or equal to", minimum,". Type again.")
        continue
     else:
        break

while True:
    #input maximum characters
     max_char = input("Type the maximum character limit for your password :")
    #max_char must be integer
     try:
        max_char = int(max_char)
     except:
        print("Wrong input. Type again.")
        continue
    #minimum must be equal or smaller than maximum
     if (min_char > max_char):
        print("Your maximum character limit must be greater than or equal to your minimum character limit.")
        continue
     else:
        break

while True:
    #include numbers
     inc_num = input("Include numbers? y/n :")
     if (inc_num != 'y' and inc_num != 'n'):
        print("Wrong input. Type again.")
        continue
     elif(inc_num == 'y'):
        minimum+=1
        if(minimum>min_char):
            print("Your minimum character limit must be greater than or equal to", minimum,". Type again.")
            continue
        else:
            break
     else:
        break

while True:
    #include special characters
     inc_spc = input("Include special characters? y/n :")
     if (inc_spc != 'y' and inc_spc!= 'n'):
        print("Wrong input. Type again.")
        continue
     elif (inc_spc == 'y'):
        minimum +=1
        if(minimum>min_char):
            print("Your minimum character limit must be greater than or equal to ", minimum,". Type again.")
            continue
        else:
            break
     else:
        break

while True:
    #include uppercase
     inc_upp = input("Include uppercase letters? y/n :")
     if (inc_upp != 'y' and inc_upp != 'n'):
        print("Wrong input. Type again.")
        continue
     elif (inc_spc == 'y'):
        minimum +=1
        if(minimum>min_char):
            print("Your minimum character limit must be greater than or equal to ", minimum,". Type again.")
            continue
        else:
            break
     else:
        break

pw_generate(min_char, max_char, inc_num, inc_spc, inc_upp)
