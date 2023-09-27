"""This tests if the methods are coherent when a disturbance is found
"""
import pytest
import random
import string
from hamming_code.single_error_detecting_codes import create_single_parity_code
from hamming_code.single_error_detecting_codes import check_single_parity_code
from hamming_code.single_error_detecting_codes import bit_len

UPPER_LIMIT = 100


# region Single disturbance
# If only a single bit if flipped it has to be detected.
def create_single_disturbance(input_: int):
    len_input = bit_len(input_)
    index = random.randint(0, len_input - 1)
    return input_ ^ 1 << index


def test_single_bit_flipped_in_int():
    res = True
    for input_ in range(UPPER_LIMIT):
        code = create_single_parity_code(input_=input_)
        disturbed_input_ = create_single_disturbance(input_=input_)
        res = res and (
            check_single_parity_code(input_, code)
            and not check_single_parity_code(disturbed_input_, code)
        )
    assert res


def test_single_bit_flipped_in_random_char_of_str():
    letters = string.ascii_lowercase
    strings = [
        "".join(random.choice(letters) for i in range(UPPER_LIMIT))
        for _ in range(UPPER_LIMIT)
    ]
    res = True
    for input_ in range(UPPER_LIMIT):
        code = create_single_parity_code(input_=input_)
        disturbed_input_ = create_single_disturbance(input_=input_)
        res = res and (
            check_single_parity_code(input_, code)
            and not check_single_parity_code(disturbed_input_, code)
        )
    assert res


# endregion


# region Double disturbance
# If two bits flip the disturbance cannot be detected and
# the code must be assumed correct
def create_double_disturbance(input_: int):
    len_input = bit_len(input_)
    index1 = random.randint(0, len_input - 1)
    input_ ^= 1 << index1
    index2 = random.randint(0, len_input - 1)
    input_ ^= 1 << index2
    return input_


def test_double_bit_flipped_in_int():
    res = True
    for input_ in range(UPPER_LIMIT):
        code = create_single_parity_code(input_=input_)
        disturbed_input_ = create_double_disturbance(input_=input_)
        res = res and (
            check_single_parity_code(input_, code)
            # Double flips are assumed correct.
            and check_single_parity_code(disturbed_input_, code)
        )
    assert res


def test_double_bit_flipped_in_random_char_of_str():
    upper_limit = 3
    letters = string.ascii_lowercase
    strings = [
        "".join(random.choice(letters) for i in range(UPPER_LIMIT))
        for _ in range(UPPER_LIMIT)
    ]
    res = True
    for input_ in range(UPPER_LIMIT):
        code = create_single_parity_code(input_=input_)
        disturbed_input_ = create_double_disturbance(input_=input_)
        res = res and (
            check_single_parity_code(input_, code)
            # Double flips are assumed correct.
            and check_single_parity_code(disturbed_input_, code)
        )
    assert res


# endregion
