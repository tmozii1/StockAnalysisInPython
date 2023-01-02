from __future__ import print_function

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from quickstart import CredentialsSpreadSheet

SHEET_ID = '13dko4IsWFON9HvbkbD1k9PXMkBZRTwKVoZ1X_hJ7qvA'


def get_values(spreadsheet_id, range_name):
    creds = CredentialsSpreadSheet()
    try:
        service = build('sheets', 'v4', credentials=creds)
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=range_name).execute()
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

def batch_get_values(spreadsheet_id, _range_names):
    """
    Creates the batch_update the user has access to.
    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
        """
    # creds, _ = google.auth.default()
    creds = CredentialsSpreadSheet()
    # pylint: disable=maybe-no-member
    try:
        service = build('sheets', 'v4', credentials=creds)
        range_names = _range_names
        result = service.spreadsheets().values().batchGet(
            spreadsheetId=spreadsheet_id, ranges=range_names).execute()
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


def main():
    result = get_values(SHEET_ID, "A1:B2")
    print(result)
    result = batch_get_values(SHEET_ID, ["A1:C2", "B1:C3"])
    print(result)

if __name__ == '__main__':
    # Pass: spreadsheet_id, and range_name
    main()