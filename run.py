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
SHEET = GSPREAD_CLIENT.open('travel_survey')

distance = SHEET.worksheet('distance')

data = distance.get_all_values()


def get_distance_data():
    """
    Get distance travelled data input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be one value.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter your distance to work each day to the nearest mile.")

        data_str = input("How many miles do you travel to work each day?\n")

        distance_data = data_str.split(",")

        if validate_data(distance_data):
            print("Data is valid!")
            break

    return distance_data


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if more than one value is entered.
    """
    try:
        [int(value) for value in values]
        if len(values) != 1:
            raise ValueError(
                f"Please only enter one value, you provided {len(values)}"
            )
        if isinstance(values, int) != True:
            raise ValueError(
                "Please enter your distance to the nearest whole mile"
            )
        
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_distance_worksheet(data):
    """
    Update distance worksheet, add new row with the list data provided
    """
    print("Updating distance worksheet...\n")
    sales_worksheet = SHEET.worksheet("distance")
    sales_worksheet.append_row(data)
    print("Distance worksheet updated successfully.\n")


data = get_distance_data()
distance_data = [int(num) for num in data]
update_distance_worksheet(distance_data)