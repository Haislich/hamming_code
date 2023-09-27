def bit_len(input_: int) -> int:
    """Get the number of bits in a given number."""
    return len(format(input_, "b"))


def create_single_parity_code(input_: [str, int]) -> [list[int], int]:
    """We can construct single error detecting code having n binary digits in the following manner:
    In the first n-1 position we put n-1 digits of information.
    In the nth position we place either 0 or 1, so that the entire
    n positions have an even number of 1's"""

    def __create_single_parity_code(input_: int) -> int:
        res = 0
        parity_bit = 0
        len_input = bit_len(input_)
        for i in range(len_input):
            current_bit = (input_ >> i) & 1
            # This acts as a toggle.
            # The parity bit is set to 1 when an odd number of 1
            # bits are found and set to 0 otherwise.
            parity_bit ^= current_bit
            res += (2 << i) * current_bit
        return res + parity_bit

    if isinstance(input_, str):
        input_ = [ord(char) for char in input_]
        return [__create_single_parity_code(element) for element in input_]
    elif isinstance(input_, int):
        return __create_single_parity_code(input_)
    else:
        raise TypeError(f"Invalid input_ type: {type(input_)}")


def check_single_parity_code(
    input_: [str, int], single_parity_code: [list[int], int]
) -> bool:
    def __check_single_parity_code(input_: int, single_parity_code: int):
        return (create_single_parity_code(input_) & 1) == (single_parity_code & 1)

    if (
        isinstance(input_, str)
        and isinstance(single_parity_code, list)
        and all([isinstance(element, int) for element in single_parity_code])
    ):
        input_ = [ord(char) for char in input_]
        return all(
            [
                __check_single_parity_code(*element)
                for element in list(zip(input_, single_parity_code))
            ]
        )
    elif isinstance(input_, int) and isinstance(single_parity_code, int):
        return __check_single_parity_code(input_, single_parity_code)
    else:
        raise TypeError(f"Invalid input_ type: {type(input_)}")
