from datetime import datetime, timedelta


def get_upcoming_birthdays(users):

    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        delta = birthday_this_year - today
        if delta.days <= 7:
            congratulation_date = birthday_this_year

            # If the birthday is on Saturday or Sunday, move it to Monday
            if congratulation_date.weekday() == 5:  # Saturday
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # Sunday
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return upcoming_birthdays


def main():

    users = [
        {"name": "John Doe", "birthday": "1985.03.28"},
        {"name": "Jane Smith", "birthday": "1990.03.27"},
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)


if __name__ == "__main__":
    main()
