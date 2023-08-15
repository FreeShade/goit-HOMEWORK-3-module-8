import datetime


def get_birthdays_per_week(users):
    days_of_week = {
        0: "monday",
        1: "tuesday",
        2: "wednesday",
        3: "thursday",
        4: "friday",
        5: "saturday",
        6: "sunday",
    }

    today = datetime.datetime.today().weekday()

    birthday_list = [[] for _ in range(7)]

    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        day_of_birthday = birthday.weekday()

        if day_of_birthday > today:
            birthday_list[0].append(name)
        else:
            birthday_list[day_of_birthday + 1].append(name)

    for i, day in enumerate(birthday_list):
        if day:
            print(f"{days_of_week[i]}: {', '.join(day)}")


def main():
    test_users = [
        {"name": "Bill", "birthday": datetime.datetime(2023, 3, 24)},
        {"name": "Jill", "birthday": datetime.datetime(1992, 4, 14)},
        {"name": "Kim", "birthday": datetime.datetime(2018, 9, 8)},
        {"name": "Jan", "birthday": datetime.datetime(2003, 12, 1)},
        # Додайте інших користувачів тут
    ]

    # Виклик функції для виведення списку іменинників
    get_birthdays_per_week(test_users)


if __name__ == "__main__":
    main()
