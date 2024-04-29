import logging
import random

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_input(method, input_param, expected_type, operation):
    """ Generic processor for handling different types of inputs and operations. """
    try:
        if isinstance(input_param, expected_type):
            return operation(input_param)
        else:
            raise ValueError(f"Invalid input type for {method.__name__}")
    except Exception as e:
        logging.error(f"Error in {method.__name__} with input {input_param}: {e}")
        raise

def method_1(input_param):
    return process_input(method_1, input_param, int, lambda x: x * 2)

def method_2(input_param):
    return process_input(method_2, input_param, str, str.upper)

def method_3(input_param):
    return process_input(method_3, input_param, list, sorted)

def method_4(input_param):
    return process_input(method_4, input_param, float, lambda x: round(x, 2))

def method_5(input_param):
    return process_input(method_5, input_param, bool, lambda x: not x)

# Sample data for testing
sample_data = {
    'int': random.randint(1, 100),
    'str': "hello",
    'list': [3, 1, 4, 1, 5, 9],
    'float': 3.14159,
    'bool': True
}

# Call and log each method with sample data
if __name__ == "__main__":
    logging.info("Starting forensics testing...")
    for name, method in [('int', method_1), ('str', method_2), ('list', method_3), ('float', method_4), ('bool', method_5)]:
        result = method(sample_data[name])
        logging.info(f"{method.__name__} result: {result}")

    logging.info("Forensics testing completed.")
