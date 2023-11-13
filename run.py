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
    Get distance figures input from the user.
    """
    distance_data = input("How many miles do you travel to work everyday?\n")

    return distance_data


