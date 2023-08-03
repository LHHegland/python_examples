"""
logz.py: Initialize logging for messaging to file or stderr (e.g. info, debug, warning, error, critical).

PURPOSE: Store or view helpful information for testing and debugging.

USAGE: 
  - Testing: py logz.py -h
  - Import: import utils.logz
            mylog = utils.logz.setup(logger_name, logfile_path_name) -- see setup function use notes below

REFERENCES:
  - argparse -- used for command line only, not required for import use.
                See https://docs.python.org/3/library/argparse.html
  - datetime -- See https://docs.python.org/3/library/datetime.html
  - logging -- See https://docs.python.org/3/library/logging.html
  - os -- See https://docs.python.org/3/library/os.html
  - platform -- See https://docs.python.org/3/library/platform.html
"""
import argparse
import datetime
import logging
import os
import platform


def get_cli_help():
    """
    Initialize command line interface help messaging

    USAGE: py logz.py --h

    REFERENCES:
      - argparse -- used for command line only, not required for import use.
                    See https://docs.python.org/3/library/argparse.html
    """
    # Define filter functions
    parser = argparse.ArgumentParser(
        prog='logz',
        description='Initialize logging to file or stderr'
                    'for messaging (e.g. info, debug, warning, error,'
                    'critical).',
        epilog='For questions or concerns, please contact'
               ' lance.hegland@civic-innovations.com'
    )
    parser.add_argument('--tes', '--testexceptionspecified',
                        action='store_true',
                        dest='is_test_exception_specified',
                        help='optional flag to test specified exception handling'
    )
    parser.add_argument('--teu', '--testexceptionunspecified',
                        action='store_true',
                        dest='is_test_exception_unspecified',
                        help='optional flag to test unspecified exception handling'
    )
    parser.add_argument('--lfpn', '--logfilepathname',
                        required=False, action='store', type=str,
                        dest='logfile_path_name',
                        help='optional logging file\'s path and name (e.g. \'D:\\path\\file.log\')'
    )
    return parser.parse_args()


def setup(logger_name: str, logfile_path_name: str | None = None) -> logging.Logger:
    """
    Initialize logging to file or stderr (e.g. info, debug, warning, error, critical).

    PURPOSE: Store or display helpful logging record messages for testing and debugging.

    USAGE: 
        import utils.logz
        [ … other imports and definitions … ]
        if __name__ == '__main__':
            mylog = utils.logz.setup(logger_name, logfile_path_name) [--OR-- mylog = utils.logz.setup(logger_name) # to stderr ]

    INPUT:
      - logger_name (str) = name of logger instance (e.g. __name__)
      - logfile_path_name (str)(optional) = path and name of log file, if omitted stream to stderr
                                            (e.g. D:\\application\\logs\\execution.log)

    OUTPUT:
      - mylog (logging.Logger) = logger instance

    REFERENCES:
      - logging -- See https://docs.python.org/3/library/logging.html
    """
    # Define filter functions
    def filter_fyi(record: logging.LogRecord) -> bool:
        """
        Filter to accept logging records with level less than or equal to info level, otherwise ignore.

        USAGE: 
        - handler.addFilter(filter_fyi)

        INPUT:
        - record (logging.LogRecord) = logging record instance -- see https://docs.python.org/3/library/logging.html#logging.LogRecord

        OUTPUT:
        - (bool) = true to accept, false to ignore

        REFERENCES:
        - logging -- See https://docs.python.org/3/library/logging.html
        """
        return record.levelno <= 20 # logging.INFO value
    
    
    # Create logging instance and set logging level.
    # See https://docs.python.org/3/howto/logging.html#logging-flow
    #     https://docs.python.org/3/howto/logging.html#loggers
    mylog = logging.getLogger(logger_name)
    mylog.setLevel(logging.DEBUG)

    # Create logging handlers for storage or display (stderr), as desired
    # See https://docs.python.org/3/library/logging.handlers.html
    if logfile_path_name == None: # logging record messages to stderr
        handler_fyi = logging.StreamHandler()
        handler_alert = logging.StreamHandler()
    else:  # logging record messages to logfile_path_name
        handler_fyi = logging.FileHandler(logfile_path_name, mode='a', encoding='utf-8')
        handler_alert = logging.FileHandler(logfile_path_name, mode='a', encoding='utf-8')
    
    # Set logging handlers' level.
    handler_fyi.setLevel(logging.DEBUG)
    handler_alert.setLevel(logging.WARNING)
    
    # Add handler filter.
    # See https://docs.python.org/3/library/logging.html#filter-objects
    handler_fyi.addFilter(filter_fyi)

    # Create logging record date format for handlers.
    # See https://docs.python.org/3/library/time.html#time.strftime
    datefmt = '%Y-%m-%d %H:%M:%S %z'
    
    # Create logging record formats for handlers.
    # See https://docs.python.org/3/library/logging.html#logrecord-attributes
    fmt_fyi = (
        '\n'
        '%(asctime)s - %(name)s - %(levelname)s: %(message)s'
    )
    fmt_alert = (
        '\n'
        '%(message)s \n'
        '%(asctime)s - %(name)s - %(levelname)s \n'
        '%(threadName)s → %(processName)s \n'
        '%(pathname)s \n'
        '→ %(module)s → %(funcName)s @ %(lineno)d'
    )

    # Create logging formatters for handlers.
    # See https://docs.python.org/3/howto/logging.html#formatters
    formatter_fyi = logging.Formatter(fmt_fyi, datefmt)
    formatter_alert = logging.Formatter(fmt_alert, datefmt)

    # Set logging formatters for handlers.
    handler_fyi.setFormatter(formatter_fyi)
    handler_alert.setFormatter(formatter_alert)

    # Add logging handlers to instance mylog.
    mylog.addHandler(handler_fyi)
    mylog.addHandler(handler_alert)

    # Return mylog instance.
    return mylog


def init_filelog(logpath: str, modname: str, filename: str) -> logging.Logger:
    """
    Setup logging to file in {logpath}\{module_name}-{timestamp}.log

    USAGE: 
        import utils.logz
        [ … other imports and definitions … ]
        if __name__ == '__main__':
            
        if __name__ == '__main__':
            logpath = 'path\\to\\log\\directory\\'
            mylog = utils.logz.init_filelog(logpath, __name__, __file__)

            try: # Code to execute, at least until an exception occurs
                mylog.info('⬛ Trying Actions…')

                # … module code to execute, at least until an exception occurs …

                mylog.info('🟩 …Completed Actions.')
            # … optional code to handle specified exceptions …
            except Exception: # Code to handle unspecified exceptions
                mylog.exception('🟥🟥 FATAL ERROR: UNEXPECTED EXCEPTION OCCURRED!',
                                exc_info = True
                )
            finally: # Code to always execute, even if an exception occurs
                term_logger(mylog, __file__)

    INPUT:
      - logpath (str) = path to directory for log file (e.g. 'D:\\application\\logs\\')
      - modname (str, filename: str

    OUTPUT:
      - mylog (logging.Logger) = logger instance

    REFERENCES:
      - logging -- See https://docs.python.org/3/library/logging.html
    """
    start_time = datetime.datetime.now()
    log_filename = logpath + os.path.basename(filename).split('.')[0] + '-' + start_time.strftime('%Y%m%d%H%M%S') + '.log'
    logger = setup(modname, log_filename)
    logger.info('\n'
                'OPERATING SYSTEM: ' + str(platform.uname()) + '\n'
                'PYTHON VERSION:: ' + str(platform.python_version()) + '\n'
                'FILE: ' + filename + '\n'
                '========== STARTING =========='
                )
    return logger


def term_filelog(logger: logging.Logger, filename: str):
    logger.info('\n'
                '========== ENDING ==========\n'
                'FILE: ' + filename
                )


# Usage example
if __name__ == '__main__':
    # Configure command line interface arguments plus help and usage messages
    args = get_cli_help()
    
    # Configure logging per command line options
    if args.logfile_path_name == None:
        mylog = setup(__name__)
    else:
        mylog = setup(__name__, args.logfile_path_name)

    mylog.info('\n'
                'FILE: ' + __file__ + '\n'
                '========== STARTING =========='
                )
    try: # Code to execute, at least until an exception occurs
        print('⬛ Trying actions.')
        mylog.info('⬛ Trying actions.')

        if args.is_test_exception_specified:
            # test specified ZeroDivisionError exception handling
            some_variable = 1 / 0
        if args.is_test_exception_unspecified:
            # Test unspecified exception handling
            raise Exception('🟥🟥 Oh, golly. Something really bad unexpectedly happened.')
        
        mylog.info(
            '⬛ TEST INFO: Message to confirm execution is working as'
            ' expected. Generally, displayed only in DEVELOPMENT'
            ' environment; typically, suppressed in TEST and PRODUCTION'
            ' environments.'
        )
        mylog.debug(
            '⚪ TEST DEBUG: Message with critical details to help identify'
            ' and resolve problems. Generally, displayed only in'
            ' DEVELOPMENT environment; typically, suppressed in TEST and'
            ' PRODUCTION environments.'
        )
        mylog.warning(
            '🟧 TEST WARNING: Message indicating that an unexpected minor problem'
            ' happened, or will likely happen in the near future (e.g.'
            ' disk space low), even though execution is currently working'
            ' as expected.',
            exc_info = True
        )
        mylog.error(
            '🟥 TEST ERROR: Message indicating that an unexpected serious problem'
            ' has occurred, which prevented some code or function to finish'
            ' executing as expected. State that results are likely invalid'
            ' or unreliable. Suggest 2 or 3 of the most common causes and'
            ' related corrective actions. Refer to a specific, credible'
            ' help article title and URL. Recommend contacting the help'
            ' desk if errors continue. Offer several contact response'
            ' levels depending on the user\'s urgency. Provide help desk'
            ' contact information; e.g. online form, email address, chat'
            ' URL, phone number.',
            exc_info = True
        )
        mylog.critical(
            '🟥🟥 TEST CRITICAL: Message indicating that an unexpected near-fatal'
            ' or fatal problem has occurred, which will very likely'
            ' prevent any further execution to occur. State that results'
            ' are very likely invalid or unreliable. Suggest 2 or 3 of the'
            ' most common causes and related corrective actions. Refer to'
            ' a specific, credible help article title and URL. Recommend'
            ' contacting the help desk if errors continue. Offer several'
            ' contact response levels depending on the user\'s urgency.'
            ' Provide help desk contact information; e.g. online form,'
            ' email address, chat URL, phone number.',
            exc_info = True
        )
        
        # Notify user that successful execution has completed.
        if args.logfile_path_name == None:
            print('\n\n🟩 SUCCESSFUL EXECUTION: See output displayed above.')
        else:
            print('\n\n🟩 SUCCESSFUL EXECUTION: See output in ' + args.logfile_path_name + '.')

        mylog.info('🟩 Completed actions successfully.')
    except ZeroDivisionError: # Code to handle specific exception
        mylog.exception(
            '🟧 Oops! Something went wrong. The application tried to do a'
            ' math problem where it tried to divide a number by zero,'
            ' but that is impossible to do. So the program stopped to'
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
            'Technical Error Details to Share with Our Help Desk Team:',
            exc_info = True
        )
    except Exception as e: # Code to handle unspecified exception
        mylog.exception(
            '🟥🟥 Oops! Something went wrong. The application stopped to'
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
            'Technical Error Details to Share with Our Help Desk Team:',
            exc_info = True
        )


    finally: # Code to always execute, even if an exception occurs
        mylog.info('\n'
                    '========== ENDING ==========\n'
                    'FILE: ' + __file__
                    )