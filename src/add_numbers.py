import re
import logging
import os

filename = os.path.join('logs', 'string_log.txt')

# Configure logging to write to a file
logging.basicConfig(filename=filename, level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class NegativeNumberException(Exception):
    """Custom exception raised when negative numbers are found in the input string."""

    def __init__(self, negatives):
        self.negatives = negatives
        super().__init__(f"Negative numbers found: {', '.join(map(str, negatives))}")


def add_numbers_in_string(input_string):
    """
    This function takes a string as input and returns the sum of all positive integers found within the string,
    including exponential integers. If negative numbers are found, an exception is raised.

    :param input_string: The input string that may contain numbers.
    :return: Sum of all positive integers in the string.
    :raises ValueError: If the input is not a string.
    :raises NegativeNumberException: If negative numbers are found in the input.
    """
    try:
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")

        # Regex to match integers and exponential notation (excluding floats)
        all_numbers = re.findall(r'-?\b\d+(?:e\d+)?\b', input_string, re.IGNORECASE)

        # Separate positive and negative numbers
        negatives = [int(num) for num in all_numbers if int(num) < 0]
        positives = [int(float(num)) for num in all_numbers if int(num) >= 0]

        # If there are negative numbers, raise an exception
        if negatives:
            logging.error(f"Negative numbers found: {negatives}")
            raise NegativeNumberException(negatives)

        # Calculate the sum of positive numbers
        result = sum(positives)

        logging.info(f"Input string: {input_string}, Extracted positives: {positives}, Sum: {result}")

        return result
    except Exception as e:
        logging.error(f"Error: {e}")
        raise
