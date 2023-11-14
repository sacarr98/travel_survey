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

d_data = distance.get_all_values()

transport = SHEET.worksheet('transport')

t_data = transport.get_all_values()


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
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_distance_worksheet(d_data):
    """
    Update distance worksheet, add new row with the list data provided
    """
    print("Updating distance worksheet...\n")
    distance_worksheet = SHEET.worksheet("distance")
    distance_worksheet.append_row(d_data)
    print("Distance worksheet updated successfully.\n")


def get_transport_data():
    """
    Asks questions about method of travel to work, adds values to a list.
    """
    walking_str = input("How many times do you walk to work each week?\n")

    cycling_str = input("How many times do you cycle to work each week?\n")

    driving_str = input("How many times do you drive to work each week?\n")

    carpool_str = input("How many times do you car pool to work each week?\n")

    bus_str = input("How many times do you take the bus to work each week?\n")

    train_str = input("How many times do you take the train to work each week?\n")

    transport_data = [walking_str, cycling_str, driving_str, carpool_str, bus_str, train_str]

    return transport_data


def update_transport_worksheet(t_data):
    """
    Update distance worksheet, add new row with the list data provided
    """
    print("Updating transport worksheet...\n")
    transport_worksheet = SHEET.worksheet("transport")
    transport_worksheet.append_row(t_data)
    print("Transport worksheet updated successfully.\n")


def main(): 
    """
    Run all program functions
    """
    d_data = get_distance_data()
    distance_data = [int(num) for num in d_data]
    update_distance_worksheet(distance_data)
    t_data = get_transport_data()
    transport_data = [int(num) for num in t_data]
    update_transport_worksheet(transport_data)


print("Thank you for taking the time to complete our survey")
main()
