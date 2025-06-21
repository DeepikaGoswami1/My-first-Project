
import random
import string

def generate_password(length=12):
    if length < 4:
        return "invalid"

    alphabets = string.ascii_letters
    symbol = string.punctuation
    digits = string.digits

    # Ensure at least one of each type
    password = [
        random.choice(alphabets),
        random.choice(digits),
        random.choice(symbol)
    ]

    all_char = digits + symbol + alphabets
    password += random.choices(all_char, k=length - 3)

    random.shuffle(password)
    return "".join(password)

password = generate_password(12)
print("password is :", password)