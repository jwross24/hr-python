def print_formatted(number):
    # your code goes here
    for i in range(1, number + 1):
        # Calculate the field width (the max width of the binary field)
        bin_number = bin(number)[2:]
        field_width = str(len(bin_number))

        # Create the format_spec
        num_str = ['d', 'o', 'X', 'b']
        format_num_str = ['{0:>' + field_width + num + '}' for num in num_str]
        format_spec = ' '.join(format_num_str)
        print(format_spec.format(i))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
