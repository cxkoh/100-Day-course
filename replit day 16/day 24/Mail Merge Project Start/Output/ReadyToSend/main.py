
with open("../../Input/Names/invited_names.txt") as name_data:
    names = name_data.readlines()

with open("../../Input/Letters/starting_letter.txt") as data:
    letter = data.read()
    for name in names:
        new_names = name.strip()
        letter_new = letter.replace("[name]", new_names)
        with open(f"Letter to {new_names}", mode="w") as completed:
            completed.write(letter_new)

