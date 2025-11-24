#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt") as f:
    name_list = f.readlines()

print(name_list)
cleaned_list = []

for name in name_list:
    clean = name.strip()
    cleaned_list.append(clean)

# print(name_list)
# print(cleaned_list)

for addressee in cleaned_list:
    with open("Input/Letters/starting_letter.txt") as f:
        contents = f.read()
        x = contents.replace("[name]", addressee)

    with open(f"Output/ReadyToSend/{addressee}.txt", mode="w") as f:
        f.write(x)

    # print("DEBUG placeholder present?", "[name]" in contents)
    # print("DEBUG addressee:", repr(addressee))

