"""Asks for a name and age, then estimates the user's birth year.

Input:
    The user's name, entered as a string.
    The user's age, entered as text and converted to an integer.

Process:
    Subtract the user's age from the current year to estimate their birth year.

Output:
    A personalized message displayed on the screen, greeting the user and stating their estimated birth year.

Typical usage example:
    Input prompt: "What is your name? " → "Michael"
    Input prompt: "How old are you? " → 20
    Output: "Hello Michael! You were born in 2006."""



# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

       # Get user input.
    user_name = input("What is your name? ")
    user_age = int(input("How old are you? "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - user_age

    # Output personalized message with user's name and birth year.
    print(f"Hello {user_name}! You were born in {birth_year}.")




# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# OpenAI. (2026). ChatGPT (Sept. 13 version) [Large language model]. https://chat.openai.com/chat
# Note: AI assistance was used to identify and correct Python indentation/spacing errors in this code.
# TODO: Replace with another APA-style reference, or delete this TODO line.
