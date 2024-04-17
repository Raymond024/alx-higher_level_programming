#!/usr/bin/python3
"""Reads standard input and computes metrics.
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size to that point.
    - Count of read status codes to that point.
"""

def print_stats(size, status_codes):
    """Prints accumulated metrics.
    Args:
        size (int): accumulated read file size.
        status_codes (dict): accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for lines in sys.stdin:
            if counter == 10:
                print_stats(size, status_codes)
                counter = 1
            else:
                counter += 1

            lines = lines.split()

            try:
                s += int(lines[-1])
            except (IndexError, ValueError):
                pass

            try:
                if lines[-2] in valid_codes:
                    if status_codes.get(lines[-2], -1) == -1:
                        status_codes[lines[-2]] = 1
                    else:
                        status_codes[lines[-2]] += 1
            except IndexError:
                pass

        print_stats(s, status_codes)

    except KeyboardInterrupt:
        print_stats(s, status_codes)
        raise
