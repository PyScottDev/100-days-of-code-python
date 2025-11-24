with open("Input/Names/invited_names.txt") as f:
    name_list = f.readlines()

cleaned_list = []

for name in name_list:
    clean = name.strip()
    if clean:                  # skip empty lines just in case
        cleaned_list.append(clean)

print("RAW NAMES:", name_list)
print("CLEANED:", cleaned_list)

for addressee in cleaned_list:
    with open("Input/Letters/starting_letter.txt") as f:
        contents = f.read()
        print("\n--- DEBUG ---")
        print("Addressee:", repr(addressee))
        print("Placeholder present?", "[name]" in contents)

        x = contents.replace("[name]", addressee)
        print("Result preview:", repr(x[:80]))  # first 80 chars

    output_path = f"Output/ReadyToSend/{addressee}.txt"
    print("Writing to:", output_path)
    with open(output_path, mode="w") as f:
        f.write(x)
