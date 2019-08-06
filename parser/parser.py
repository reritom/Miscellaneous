


def parse(string: str, delimiter: str = ' ', nest_characters: str = '()') -> list:
    """
    This function is for recursively parsing a nested string structure of opening and closing
    parentheses and converting it into nested list structure

    >>>parse("hello world")
    ["hello", "world"]

    >>>parse("a b (c d (e f)) g")
    ["a", "b", ["c", "d", ["e", "f"]], "g"]
    """

    nest = [] # Holds the resultant list
    openers = [] # Holds indices of opening characters
    closers = [] # Holds indices of closing characters
    pairs = [] # Holds tuples of opening and closing index pairs

    # Find the indexes of matching parentheses
    for index, character in enumerate(string):
        if character == nest_characters[0]:
            openers.append(index)
        elif character == nest_characters[1]:
            closers.append(index)

        if openers and closers and len(openers) >= len(closers):
            pairs.append((openers.pop(-1), closers.pop()))

    # If we have pairs, look at each subsection and recursively apply this function if applicable
    if pairs:
        for pair_index, (open_index, close_index) in enumerate(pairs):
            # Check if this pair is a nested pair
            nested = False
            for sub_pair_index, (sub_open_index, sub_close_index) in enumerate(pairs):
                if pair_index == sub_pair_index:
                    continue

                if open_index > sub_open_index and close_index < sub_close_index:
                    # This pair is nested, so we ignore it
                    nested = True

            # If it isn't nested, recurse, else, a lower level will deal with this pair
            if not nested:
                parsed_sub = parse(
                    string=string[open_index + 1:close_index],
                    delimiter=delimiter,
                    nest_characters=nest_characters
                )
                nest.append(parsed_sub)

        # Strip any characters from the string which are left at this level
        string = ''.join([
            char
            for index, char in enumerate(string)
            if not [
                index
                for start, end in pairs
                if index >= start and index <= end
            ]
        ])

    nest.extend([word for word in string.split(delimiter) if word])
    return nest

if __name__ == '__main__':
    string = "a b c (d e (f g)) h"
    print(parse(string))
