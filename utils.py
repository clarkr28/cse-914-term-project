# random functions needed for the project


def int2hex(integer, output_length):
    """
    take an integer and convert it to a hex string of a specific value.  Throws a value error if the hex
    representation of the integer is longer than the output_length
    :param integer: integer to convert
    :param output_length: required length of the string
    :return: hex representation as a string, padded with zeros in the front if necessary
    """
    converted = hex(integer)[2:]
    if len(converted) > output_length:
        # raise an error because the converted value is too large
        raise ValueError('int2hex error: the hex value was longer than the desired output length\n' +
                         'dec: {}, hex: {}, outLen: {}'.format(integer, converted, output_length))
    elif len(converted) < output_length:
        # pad the proper number of zeros at the beginning to make the string the proper length
        converted = '0' * (output_length - len(converted)) + converted

    return converted
