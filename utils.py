import string
import random


def generate_request_id():
    letters_and_digits = string.ascii_letters + string.digits
    request_id = ''.join(random.sample(letters_and_digits, 8)).lower() + '-' + ''.join(random.sample(letters_and_digits, 4)).lower() + \
                 '-' + ''.join(random.sample(letters_and_digits, 4)).lower() + '-' + ''.join(
        random.sample(letters_and_digits, 4)).lower() \
                 + '-' + ''.join(random.sample(letters_and_digits, 12)).lower()
    return request_id