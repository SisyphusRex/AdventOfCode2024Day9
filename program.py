"""program module"""

number_of_file_blocks_dict = {}
number_of_free_space_blocks_dict = {}


def main(*args):
    """main method"""
    data = get_data("data.txt")
    assign_key_values_to_dicts(data)
    main_block = make_block()

    sorted_block = move_blocks(main_block)

    checksum = get_checksum(sorted_block)
    print(checksum)


def get_checksum(block):
    """calculate checksum"""
    total = 0
    for index, value in enumerate(block):
        if value != ".":
            total += index * value
    return total


def move_blocks(main_block):
    """move empty to end"""
    aux_block = []
    length = len(main_block)
    final_file_index = get_total_file_blocks() - 1

    for element in main_block:
        aux_block.append(element)
    for index, value in enumerate(main_block):
        if index <= final_file_index:
            if value == ".":
                for reversed_list_index, value2 in enumerate(aux_block[::-1]):
                    if value2 != ".":
                        aux_block[index] = value2

                        aux_block[length - 1 - reversed_list_index] = "."
                        break

    return aux_block


def get_total_file_blocks() -> int:
    """get total number of file blocks"""
    total = 0
    number_of_ids = len(number_of_file_blocks_dict)
    for index in range(number_of_ids):
        total += number_of_file_blocks_dict[index]
    return total


def make_block() -> list[int]:
    """make a block including file ids and blank space"""
    main_block = []
    number_of_ids = len(number_of_file_blocks_dict)
    for index in range(number_of_ids):
        number_of_file_blocks = number_of_file_blocks_dict[index]
        number_of_free_space_blocks = number_of_free_space_blocks_dict[index]
        for file in range(number_of_file_blocks):
            main_block.append(index)
        for free in range(number_of_free_space_blocks):
            main_block.append(".")
    return main_block


def assign_key_values_to_dicts(data: list[int]):
    file_blocks = data[::2]
    free_blocks = data[1::2]
    for index, value in enumerate(file_blocks):
        number_of_file_blocks_dict[index] = value
    for index, value in enumerate(free_blocks):
        number_of_free_space_blocks_dict[index] = value

    if len(data) % 2 == 1:
        last_index = len(file_blocks) - 1
        number_of_free_space_blocks_dict[last_index] = 0


def get_data(filename):
    """Reads a maze from a text file and returns it as a list of lists."""
    data = []
    with open(filename, "r") as f:
        for line in f:
            strip_line = line.strip()
            inted_list = []
            for element in strip_line:
                inted_list.append(int(element))
            for element in inted_list:
                data.append(element)
    return data
