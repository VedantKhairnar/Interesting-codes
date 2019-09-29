# Pangram checker --checks all the alphabets are there in the statement
print("pangram") if ''.join(sorted(set(''.join(input().split()).lower())))=="abcdefghijklmnopqrstuvwxyz"  else print("not pangram")
