from datetime import datetime


def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - date_obj
        return delta.days
    except ValueError:
        return "Invalid date format. Please use 'YYYY-MM-DD'."


def main():
    date_str = "2021-10-09"
    result = get_days_from_today(date_str)
    print(f"The number of days between {date_str} and today is: {result}")


if __name__ == "__main__":
    main()
