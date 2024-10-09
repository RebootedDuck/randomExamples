# Program should take user input of name, age, secondary school, date of birth, name of tutor

# OLD

name = input("What is your name?: ")
age = input("What is your age?: ")
secondary_school = input("What is your Secondary School?: ")
date_of_birth = input("What is your Date Of Birth?: ")
tutor_name = input("What is your tutor's name?: ")

# You make a new line in a print statement with \n

# This method is the most obvious, but difficult to read because of the multiple string concatenations
print("Your name is ", name, "\nYour age is: ", age, "\nYour secondary school is ", secondary_school, "\nDate Of Birth is ", date_of_birth, "\nYour tutor's name is ", tutor_name)

# This method is much nicer, as we use F-Strings (Formatted Strings) to insert variables inside the string, make an F-String by placing f before "" so f"", reference variables inside with {}
print(f"Your name is {name}\n Your age is {age} \nYour secondary school is {secondary_school} \nYour Date Of Birth is {date_of_birth},\n Your tutor's name is {tutor_name} ")

# We continue the best method in a separate file