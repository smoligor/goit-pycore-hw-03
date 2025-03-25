import random


def get_numbers_ticket(min, max, quantity):

    if not (1 <= min <= max <= 1000 and min <= quantity <= max):
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)


def main():

    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)


if __name__ == "__main__":
    main()
