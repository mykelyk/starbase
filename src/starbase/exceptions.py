__title__ = 'starbase.exceptions'
__version__ = '0.2'
__build__ = 0x000002
__author__ = 'Artur Barseghyan'

class StarbaseException(Exception):
    """
    Parents all starbase specific exceptions.
    """

class ImproperlyConfigured(Exception):
    """
    Exception raised when developer didn't configure the code properly.
    """

class InvalidArguments(ValueError):
    """
    Exception raised when invalid arguments supplied.
    """

class ResponseParseError(StarbaseException):
    """
    Exception raised when we failed to parse a rest response.
    """
