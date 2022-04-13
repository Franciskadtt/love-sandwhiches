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
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    # Create a while loop to keep running until stopped
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")

        # check if the data is validated which is the sales data
        if validate_data(sales_data):
            # to print to get feedback
            print("Data is valid!")
            # end the while loop
            break

    # return validated sales_data from get_sales_data funtion
    return sales_data


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
        # if error return false for if statement in get_sales_data() function
        return False

    # if function run without errors return true for if statement in
    # get_sales_data() function
    return True


# Function to insert sales_data in Google Sheet, pass in data to insert
def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    # give user feedback in the terminal while program is busy
    print("Updating sales worksheet...\n")
    # access sales worksheet from Google Sheet refer to SHEET variable at top
    # use gspread worksheet() method to access our sales worksheet
    sales_worksheet = SHEET.worksheet("sales")
    # use gspread method append_row() to add new row at end of data
    # pass in data to be inserted
    sales_worksheet.append_row(data)
    # give feedback to user that sales worksheet updated successfully
    print("Sales worksheet updated successfully.\n")


# Because function returns a value, need to place it where it is called
data = get_sales_data()
# Convert each numbers in data list into a integers
sales_data = [int(num) for num in data]
# call our function and pass it our sales_data list
update_sales_worksheet(sales_data)