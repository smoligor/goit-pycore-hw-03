import re


def normalize_phone(phone_number):

    cleaned_number = re.sub(r"[^\d+]", "", phone_number)

    if cleaned_number.startswith("+"):

        if cleaned_number.startswith("+380"):
            return "+" + cleaned_number[3:]
        return cleaned_number
    else:

        if cleaned_number.startswith("380"):
            return "+" + cleaned_number[3:]

        else:
            return "+38" + cleaned_number


def main():

    phone_number = "    +38(050)123-32-34"
    normalized_number = normalize_phone(phone_number)
    print(f"Original phone number: {phone_number}")
    print(f"Normalized phone number: {normalized_number}")


if __name__ == "__main__":
    main()
