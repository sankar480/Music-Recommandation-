import sys 
import traceback

def error_message_details(error_message,error_detail:sys):
    try:
        _,_,exc_tb = sys.exc_info()
        if exc_tb:
            file_name = exc_tb.tb_frame.f_code.co_filename
            return f"Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message[{error_message}]"
        else:
            # Handle manually raised exception
            return f"Error message[{error_message}]"
    except Exception as e:
        return f"Failed to get error details: {str(e)}"
    
class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail)

    def __str__(self):
        return self.error_message
    
