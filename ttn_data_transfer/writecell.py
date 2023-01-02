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

def update_values(spreadsheet_id, range_name, value_input_option, _values):
    try:
        service = getService()
        values = _values
        body = {
            'values': values
        }
        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id, range=range_name,
            valueInputOption=value_input_option, body=body).execute()
        print(f"{result.get('updatedCells')} cells updated.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error
    
def batch_update_values(spreadsheet_id, value_input_option, r0, v0, r1, v1):
    try:
        service = getService()

        data = [
            {
                'range': r0,
                'values': v0
            },
            {
                'range': r1,
                'values': v1
            }
        ]
        body = {
            'valueInputOption': value_input_option,
            'data': data
        }
        result = service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id, body=body).execute()
        print(f"{(result.get('totalUpdatedCells'))} cells updated.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error
    
def append_values(spreadsheet_id, range_name, value_input_option, values):
    try:
        service = getService()
        body = {
            'values': values
        }
        result = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id, range=range_name,
            valueInputOption=value_input_option, body=body).execute()
        print(f"{(result.get('updates').get('updatedCells'))} cells appended.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error
    
def test():
    result = update_values(SHEET_ID, "A1:C2", "USER_ENTERED", [ ['A1', 'B1'], ['C1', 'D1'] ])
    print(result)
    
def test2():
    result = batch_update_values(SHEET_ID, "USER_ENTERED", "E1:F2", [[1, 2], [3, 4]], "E4:F5", [['a', 'b'], ['c', 'd']])
    print(result)
    
def test3():
    result = append_values(SHEET_ID, "A1:C2", "USER_ENTERED", [ ['F', 'G'], ['C', 'D'] ])
    print(result)

def main():
    # test()
    # test2()
    test3()

if __name__ == '__main__':
    # Pass: spreadsheet_id,  range_name, value_input_option and  _values
    main()