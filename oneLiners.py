# Pangram checker -- checks all the alphabets are there in the statement
print("pangram") if ''.join(sorted(set(''.join(input().split()).lower())))=="abcdefghijklmnopqrstuvwxyz"  else print("not pangram")

# Anagram Checker -- checks if entered word can be obtained by rearranging the alphabets of another entered word
print("Anagram") if sorted(input().lower())==sorted(input().lower()) else print("Not Anagram")


