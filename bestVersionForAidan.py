to_ask = ["Name", "Age","Secondary School", "Date Of Birth", "Tutor's name"]
answers = []

for i in to_ask:  # When you loop through a list directly, i is the value, NOT the list position
    answers.append(input(f"What is your {i}")) # This asks the user for whatever the current value in this iteration is, and appends to answers
    # Crucially "name" will be in the same position as the answer "14", it is critical they have the same position, this could be done better with a dictionary
    
print(answers)

for i, idx in enumerate(to_ask): # When you loop through a list using enumerate(), i is the POSITION, idx is the VALUE
    print(i, idx) # idx isn't needed
    print(f"Your {to_ask[i]}, is {answers[i]}") # This prints that the users to_ask[i] is answers[i], crucially, we reference the same position so the value is the same