# store the gate log in a list
gate_log = ["Maxine", "Jim", "Billy", "Billy", "Maxine", "Mike", "El", "Dustin", "Billy", "Maxine", "Joyce", "Billy", "Maxine", "Joyce", "Mike", "Nancy", "El", "Jonathan", "Dustin", "Steve", "Joyce"]

# create a set for first entry
first_entry = set()

# create a set for second entry
second_entry = set()

# create a set for third entry
third_entry = set()

# loop through the gate log
for i in gate_log:
    # if they have not visited yet
    if not(i in first_entry):
        # add them to the set for first entry
        first_entry.add(i)
    # if this is their second visit
    elif not(i in second_entry):
        # add them to the set for second entry
        second_entry.add(i)
    # if this is their third or beyond entry
    else:
        # add them to the set for third entry
        third_entry.add(i)


print("FIRST ENTRY CHARGES")

# loop through the set for first entry
for i in first_entry:
    # display that the person has been charged $10
    print(f"{i:10} Charged $10")

print("\nSECOND ENTRY CHARGES")

# loop through the set for second entry
for i in second_entry:
    # display that the person has been charged $5
    print(f"{i:10} Charged $5")

print("\nTHIRD ENTRY CHARGES")

# loop through the set for third entry
for i in third_entry:
    # display that the person has been charged $2
    print(f"{i:10} Charged $2")