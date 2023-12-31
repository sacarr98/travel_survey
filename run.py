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


def get_distance_data():
    """
    Get distance travelled data input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be one value.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Enter your distance to work each day to the nearest mile.\n")

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


def get_distance_column():
    """
    Collects column of data from distance worksheet, and returns the data
    as a list of lists.
    """
    distance = SHEET.worksheet("distance")

    d_columns = []
    for ind in range(1, 2):
        d_column = distance.col_values(ind)
        d_columns.append(d_column[2:])

    return d_columns[0]


def calculate_distance_data(d_data):
    """
    Produces data to plot a graph showing the average distances travelled by
    employees,
    sorting the data into numerical order and providing the number of
    occurances of each distance
    """
    from collections import Counter
    distances_counted = Counter(d_data)
    distances_sorted = sorted(distances_counted.items())

    return distances_sorted


def update_distance_result_worksheet(d_data):
    """
    Update distance worksheet, add new row with the list data provided
    """
    print("Updating distance result worksheet...\n")
    distance_result_worksheet = SHEET.worksheet("distance_results")
    distance_result_worksheet.delete_rows(2, end_index=30)
    for row in d_data:
        distance_result_worksheet.append_row(row)
    print("Distance_result worksheet updated successfully.\n")


def get_transport_data():
    """
    Asks questions about method of travel to work, adds values to a list.
    """
    print('''The following questions are about your mode of transport,
            please enter the number of days you use each mode of
            transport as a single whole digit.
            If you never use that mode of transport please enter 0.\n''')

    while True:

        walking_str = input("How often do you walk to work each week?\n")

        cycling_str = input("How often do you cycle to work each week?\n")

        driving_str = input("How often do you drive to work each week?\n")

        carpool_str = input("How often do you car pool to work each week?\n")

        bus_str = input("How often do you take the bus to work each week?\n")

        train_str = input("""How often do you take the train
        to work each week?\n""")

        transport_data = [
            walking_str, cycling_str, driving_str, carpool_str,
            bus_str, train_str
            ]

        if validate_transport_data(transport_data):
            print("Data is valid!")
            break

    return transport_data


def validate_transport_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if more than one value is entered.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"""Please only enter one value per question,
                you provided a total of {len(values)}"""
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_transport_worksheet(t_data):
    """
    Update transport worksheet, add new row with the list data provided
    """
    print("Updating transport worksheet...\n")
    transport_worksheet = SHEET.worksheet("transport")
    transport_worksheet.append_row(t_data)
    print("Transport worksheet updated successfully.\n")


def get_transport_columns():
    """
    Collects columns of data from transport worksheet,
    and returns the data as a list of lists.
    """
    transport = SHEET.worksheet("transport")

    columns = []
    for ind in range(1, 7):
        column = transport.col_values(ind)
        columns.append(column[2:])

    return columns


def calculate_transport_data(t_data):
    """
    Sums the number of times each method of transport is taken
    """
    print("Calculating transport data...\n")
    new_transport_data = []

    for column in t_data:
        int_column = [int(num) for num in column]
        total = sum(int_column)
        new_transport_data.append(total)

    return new_transport_data


def update_transport_results_worksheet(t_data):
    """
    Update transport results worksheet,
    clearing previous data so only new sum is visible
    """
    print("Updating transport results worksheet...\n")
    transport_results_worksheet = SHEET.worksheet("transport_results")
    transport_results_worksheet.delete_rows(2, end_index=3)
    transport_results_worksheet.append_row(t_data)
    print("Transport results worksheet updated successfully.\n")


def main():
    """
    Run all program functions
    """
    d_data = get_distance_data()
    distance_data = [int(num) for num in d_data]
    update_distance_worksheet(distance_data)
    d_columns = get_distance_column()
    distances_counted = calculate_distance_data(d_columns)
    update_distance_result_worksheet(distances_counted)
    t_data = get_transport_data()
    transport_data = [int(num) for num in t_data]
    update_transport_worksheet(transport_data)
    transport_columns = get_transport_columns()
    total_transport_data = calculate_transport_data(transport_columns)
    update_transport_results_worksheet(total_transport_data)


print("Thank you for taking the time to complete our survey")
main()
