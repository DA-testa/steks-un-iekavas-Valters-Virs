# python3

from collections import namedtuple
import pathlib

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []

    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            # Process closing bracket
            if not opening_brackets_stack:
                return 1
            if not are_matching(opening_brackets_stack.pop().char, next):
                return i + 1

    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1

    return "Success"

def main():
    while True:
        # Input F or I
        input_type = input()
        if input_type.upper()[0] == "I" or input_type.upper()[0] == "F":
            break

    if input_type.upper()[0] == "I":
        # Input I
        text = input()
    elif input_type.upper()[0] == "F":
        # Input F, get files
        path = pathlib.Path(__file__).parent.resolve()
        files = list(path.joinpath('test').glob('*[0-9]'))
        files.sort()

        # Display files
        print("Choose file")
        for key, file in enumerate(files):
            print(str(key + 1) + ". " + file.name)

        while True:
            file_choice = input()

            try:
                if int(file_choice) in range(1, len(files) + 1):
                    break
            except:
                pass

        text = files[int(file_choice) - 1].read_text()

    mismatch = find_mismatch(text)
    # Printing answer
    print(mismatch)


if __name__ == "__main__":
    main()
