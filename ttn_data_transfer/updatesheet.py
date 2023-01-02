from __future__ import print_function

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from quickstart import CredentialsSpreadSheet

SHEET_ID = '13dko4IsWFON9HvbkbD1k9PXMkBZRTwKVoZ1X_hJ7qvA'

def getService():
    creds = CredentialsSpreadSheet()
    try:
        service = build('sheets', 'v4', credentials=creds)
        return service
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error
    
    
def getsheetinfo():
    try:
        service = getService()
        result = service.spreadsheets().values().get(spreadsheetId=SHEET_ID).execute()
        print(result)
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error
    
    
def sheets_batch_update(spreadsheet_id, title, find, replacement):
    try:
        service = getService()

        requests = []
        # Change the spreadsheet's title.
        requests.append({
            'updateSpreadsheetProperties': {
                'properties': {
                    'title': title
                },
                'fields': 'title'
            }
        })
        # Find and replace text
        requests.append({
            'findReplace': {
                'find': find,
                'replacement': replacement,
                'allSheets': True
            }
        })
        # Add additional requests (operations) ...

        body = {
            'requests': requests
        }
        response = service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=body).execute()
        find_replace_response = response.get('replies')[1].get('findReplace')
        print('{0} replacements made.'.format(
            find_replace_response.get('occurrencesChanged')))
        return response

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


def main():
    sheets_batch_update(SHEET_ID, 'new title', '777', '1')

if __name__ == '__main__':
    main()