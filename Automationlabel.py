animals = "0 bellflower\n1 black_eyed_s...\n2 daisy\n3 dandelion\n4 iris\n5 rose\n6 sunflower\n7 tulip\n8 Water_lily\n9 carnation"

# Split the string by newline character and store in a list
animal_list = animals.split("\n")

# Extract only the animal names and store in a new list
name_list = [animal.split(" ", 1)[1] for animal in animal_list]

# Print the list of animal names
print(name_list)