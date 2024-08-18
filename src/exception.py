import sys

def error_message_detail(error, error_detail):
    """
    This function formats the error message with the details of the exception.
    """
    _, _, exc_tb = sys.exc_info()  # Retrieve exception info directly
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        f"Error occurred in Python script name [{file_name}] "
        f"line number [{exc_tb.tb_lineno}] error message [{error}]"
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)  # Corrected the super call
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message
