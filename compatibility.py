print("..............The Love Calculator is calculating your score..............")
name1 = input("Enter your name: ") 
name2 = input("Enter your loves name: ") 
combined_names = name1 + name2
lower_names = combined_names.lower()

# Count the occurrences of the letters in "TRUE"
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

# Count the occurrences of the letters in "LOVE"
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

# Calculate the score
score = int(str(first_digit) + str(second_digit))

# Print the result based on the score:
if score < 10 or score > 90: 
    print(f"Your score is {score}, You go together like love and a heartbeat..")
elif 40 <= score <= 50:
    print(f"Your score is {score}, You bring out the best in each other..")
else: 
    print(f"Your score is {score}, You are alright togther.")
