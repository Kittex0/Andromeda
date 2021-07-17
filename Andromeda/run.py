while True:
    qs = input("> ")
    with open("Responses.txt", "r") as file:
        data = file.readlines()  # reads it line by line

        for i in data:
            if qs == i.split(" = ")[0]:
                answer = i.split(" = ")[1]
                print(answer)
