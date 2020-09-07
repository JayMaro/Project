Client_list = []
num = 1
while num != '0':
    print('\n'+'#'*17)
    print("1. Add Client")
    print("2. Show Clients")
    print("3. Transfer")
    print("0. Exit")
    print('#'*17)
    num = input("Select: ")
    if num =='1':
        ID = int(input("Client ID: "))
        Name = input("Client Name: ")
        Deposit = int(input("Initial Deposit: "))
        list = [ID, Name, Deposit]
        Client_list.append(list)
    if num == '2':
        for index in range(len(Client_list)):
            print(Client_list[index])
    if num == '3':
        S_id = int(input("Sender ID: "))
        R_id = int(input("Receiver ID: "))
        H_much = int(input("How much: "))
        for index in range(len(Client_list)):
            if S_id == Client_list[index][0]:
                S_id = index
            if R_id == Client_list[index][0]:
                R_id = index
        if Client_list[S_id][2]<H_much:
            print(Client_list[S_id][0],"CANNOT TRANSFER",H_much)
            continue
        Client_list[S_id][2] -= H_much
        Client_list[R_id][2] += H_much
    if num == 'ilovepython':
        Client_list.sort(key = lambda x:x[2], reverse = True)
        for index in range(3):
            print(Client_list[index])
                         
print("Exit")
