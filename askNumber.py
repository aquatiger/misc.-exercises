def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high, 1):
        response = input(question)
        return response

ask_number(5, 1, 10)
