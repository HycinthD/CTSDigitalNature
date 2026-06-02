def write_greeting():
    with open("greeting.txt", "w") as file:
        file.write("Hello World")

    print("File written successfully")

write_greeting()