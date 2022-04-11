import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches(v2)')


def get_sales_data():
    """
    Get sales figures input from the user.
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")

    sales_data = data_str.split(",")
    validate_data(sales_data)


# Create function check for 6 numbers
def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    # Try & Run code with no errors if the data is valid
    # Lets you test a block of code for errors.
    try:
        # Convert each value in values list into an integer
        [int(value) for value in values]
        # Check how many values we have in our values list
        # if length of values is not 6
        if len(values) != 6:
            # Raise ValueError if the length of our data is not 6
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    # Lets you handle the error
    # Assign ValueError object to error variable
    except ValueError as e:
        # using an f string to insert the e variable into the string
        print(f"Invalid data: {e}, please try again.\n")


get_sales_data()
