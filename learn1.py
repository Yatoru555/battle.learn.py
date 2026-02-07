
# функция, создаем профиль
# функция, изменить профиль
# функция, битва
# словари, враг, игрок
# выйти

player = {
    "user": "",
    "age": "",
    "hp": 100,
    "damage": 12,
    "max_hp": 100,
    "gold": 111,
    "exp": 0
}

enemy = { 
    "name": "слизь", 
    "hp": 60, 
    "damage": 10 
}

def create_profile(player):
    input("нажмите - Enter, чтобы создать профиль:-> ")

    while True:
        user = input("придумайте свой уникальный юзер:-> ")
        if user.replace(" ", "").isalpha():
            player["user"] = user
            break
        else:
            print("ошибка. попробуйте еще раз!")

    while True:
        age = input("введите ваш возраст:-> ")
        if age.isdigit():
            player["age"] = age
            break
        else:
            print("ошибка. попробуйте еще раз!")

    return player




def edit_profile(player):
    if player["user"] == "" or player["age"] == "":
        print("сначала создайте профиль")
        return player


    print("\n== выберите что сделать ==")
    print("1. имя")
    print("2. возраст")
    print("3. выйти, ничего не менять")

    choice = input("выберите действие:-> ")

    if not choice.isdigit():
        print("ошибка. попробуйте еще раз!")
        return player
    
    choice = int(choice)

    if choice == 1:

        while True:
            new_user = input("придумайте новый юзер:-> ")
            if new_user.replace (" ", "").isalpha():
                player["user"] = new_user
                break
            else:
                print("ошибка. попробуйте еще раз!")

    elif choice == 2:

        while True:
            new_age = input("введите ваш возраст:-> ")
            if new_age.isdigit():
                player["age"] = new_age
                break
            else:
                print("ошибка. попробуйте еще раз!")

    return player



def battle(player, enemy):
    enemy = enemy.copy()
    player["hp"] = player["max_hp"]
    print("вы встретили врага")

    while player["hp"] > 0 and enemy["hp"] > 0:
        input("нажмите - Enter, чтобы ударить:-> ")

        enemy["hp"] -= player["damage"]
        print(f"вы удврили: осталось {enemy['hp']} хп")

        if enemy["hp"] <= 0:
            player["gold"] += 10
            player["exp"] += 10
            print("вы победили: вы получили золото")
            break

        player["hp"] -= enemy["damage"]
        print(f"вас ударили: осталось {player['hp']} хп")

        if player["hp"] <= 0:
            print("вы проиграли")
            break







while True:
    print("\n== Старт меню ==")
    print("1. создать профиль")
    print("2. изменить профиль")
    print("3. профиль")
    print("4. битва")
    print("5. выйти")

    choice = input("выберите действие:->")

    if not choice.isdigit():
        print("ошибка. попробуйте еще раз!")
        continue

    choice = int(choice)

    if choice == 1:
        create_profile(player)

    elif choice == 2:
        edit_profile(player)

    elif choice == 3:
        print("ваш профиль:-> ")
        print(f"user: {player['user']}")
        print(f"age: {player['age']}")
        print(f"gold: {player['gold']}")
        print(f"exp: {player['exp']}")

    elif choice == 4:
        battle(player, enemy)

    elif choice == 5:
        print("выход")
        break
    else:
        print("ошибка. попробуйте еще раз!")