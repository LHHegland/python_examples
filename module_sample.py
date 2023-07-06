"""
module_sample.py: Ask for user's full name and say hello.

PURPOSE: This is a simple python module example for educational purposes only.

USAGE: py module_sample.py

INPUT:
  - executes stdin prompts
      - What is your first and last name? (e.g. Pat Doe-Smith)

OUTPUT:
  - executes stdout messages
      - Hi, {first name}!

FUNCTIONS:
  - get_user_full_name() -> str
  - extract_first_name(full_name: str) -> str

REFERENCES:
  - config_log.setup = configure logging

"""

from config_log import setup

def get_user_full_name() -> str:
    """
    Ask for and return user's full name.

    INPUT:
    - executes stdin prompts
        - What is your first and last name? (e.g. Pat Doe-Smith)

    OUTPUT:
    - stdin -> string
    """
    return input("\nWhat is your first and last name? (e.g. Pat Doe-Smith)\n")


def extract_first_name(full_name: str) -> str:
    """
    Return assumed first name (i.e. all but the last word in the string; e.g. Mary Kay Smith -> Mary Kay)

    INPUT:
    - full_name: str

    OUTPUT:
    - first_name -> string
    """
    name_parts = full_name.split()
    return ' '.join(name_parts[:-1])


if __name__ == '__main__':
    # Configure logging to stderr, or to log file by specifying path and name
    logger = setup(__name__, 'module_sample.log')
    logger.info('STARTING: module_sample.py')

    try: # Code to execute, at least until an exception occurs.
        # Ask user for their full name, put response in variable my_full_name.
        my_full_name = get_user_full_name()
        logger.debug('USER INPUT: my_full_name = ' + my_full_name)

        # Get user's first name, put in variable my_first_name
        my_first_name = extract_first_name(my_full_name)
        logger.debug('FUNC RETURN: extract_first_name -> my_first_name = ' + my_first_name)

        # Print personalized greeting to console.
        print('\nHi, ' + my_first_name + '!')

        # Notify user that successful execution has completed.
        logger.info('SUCCESSFUL EXECUTION: module_sample.py')


    except Exception as e: # Code to handle all other unexpected exceptions
        logger.exception(
            'Oops! Something went wrong. The application stopped to'
            ' make sure it doesn\'t give you any wrong or unreliable'
            ' information.\n'
            '\n'
            'But, don\'t worry! Let\'s figure out what went wrong and'
            ' get you back on track. First, please double-check the'
            ' information you entered. Make sure everything is correct'
            ' and matches what you intended. If there\'s anything that'
            ' needs to be changed, go ahead and fix it.\n'
            '\n'
            'If you\'re still having trouble, we\'re here to help! You'
            ' can reach out to our support team in a way that\'s most'
            ' convenient for you.\n'
            '\n'
            'If you like chatting online, you can connect with a'
            ' support team member on our website at'
            ' support-chat.domain.tld. They\'re available all the time'
            ' to assist you.\n'
            '\n'
            'If you prefer talking on the phone, you can call us at'
            ' 800-555-1234 on weekdays between 9 AM and 5 PM Central'
            ' Time.\n'
            '\n'
            'If you want to send us a message and get a response by'
            ' email, you can use our online support request form at'
            ' support-form.domain.tld. We\'ll make sure to get back'
            ' to you within 1 to 2 business days.\n'
            '\n'
            'We\'re here to make sure everything runs smoothly for'
            ' you, so don\'t hesitate to get in touch.\n'
            '\n'
            'Technical Error Details to Share with Our Help Desk Team:\n'
            + str(e),
            exc_info = True
        )
        

    finally: # Code to always execute, even if an exception occurs
        logger.info('EXITING: module_sample.py')