#!/usr/bin/python3
''' module documentation '''


def print_file_size(file_size):
    '''
    function to print the file size
    
    Arguments:
        file_size (int): the file size
    '''
    print("File size: {}".format(file_size))

def print_status_codes(status_codes):
    '''
    function to print the status codes
    
    Arguments:
        status_code (dict): the status codes
    '''
    for code in status_codes:
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

if __name__ == "__main__":
    import sys
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    file_size = 0

    try:
        line_count = 0
        for line in sys.stdin:
            line = line.split()
            try:
                size = int(line[-1])
                code = int(line[-2])
            except ValueError:
                pass
            line_count += 1

            file_size += size

            if code in status_codes:
                status_codes[code] += 1

            if line_count == 10:
                print_file_size(file_size)
                print_status_codes(status_codes)
                line_count = 0
    except KeyboardInterrupt:
        print_file_size(file_size)
        print_status_codes(status_codes)
        raise

    print_file_size(file_size)
    print_status_codes(status_codes)
