from __future__ import print_function

from quickstart import CredentialsSpreadSheet

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def create(title):
    creds = CredentialsSpreadSheet()
    # creds, _ = google.auth.default()
    # pylint: disable=maybe-no-member
    try:
        service = build('sheets', 'v4', credentials=creds)
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                                    fields='spreadsheetId') \
            .execute()
        print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
        return spreadsheet.get('spreadsheetId')
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


if __name__ == '__main__':
    # Pass: title
    create("mysheet1")