# First i imported the exception so i go to the book recommender then inside that i have exceptionand inside that i have exception_handler
from books_recommender.exception.exception_handler import AppException
import sys

# Now i am importing the loggin
from books_recommender.logger.log import logging


# Now i will write wrong code to check if my exceptional handling works properly or not

try:
    a = 3/0   # So here is the error divide by zero 
except Exception as e: 
    logging.info(e)
    raise AppException(e, sys) from e

