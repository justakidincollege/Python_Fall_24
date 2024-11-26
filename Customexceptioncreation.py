# Custom Exception Creation Assignment
# Create custom exception
class NotNumericError(Exception):
    pass

def main():
    try:
        user_input = input("Enter a number: ")
        
        if not user_input.isnumeric():
            raise NotNumericError("The input is not a valid number.")
        
    except NotNumericError as e:
        print(f"Error: {e}")
    else:
        print(f"Valid input received: {user_input}")
    finally:
        print("Execution of the current attempt completed.")
        if not user_input.isnumeric():
            main()
main()
