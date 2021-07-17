print("Wanna Support us? Add a Question/Answer")
while True:
        f = open("Responses.txt", "a")
        qqs = input("Add an question: ")
        aqs = input("Add an answer: ")
        f.write("\n")
        f.write(f"{qqs} = {aqs}")
        print("Succesful")
