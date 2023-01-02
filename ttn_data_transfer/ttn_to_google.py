from __future__ import print_function

import gspread

# 계정에서 특정폴더 가져오기 (없으면 생성)
# 구글에서 파일명의 이름을 가지고 있는지 찾기

from quickstart import CredentialsSpreadSheet

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def search_file():
    creds = CredentialsSpreadSheet()
    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        files = []
        page_token = None
        while True:
            # pylint: disable=maybe-no-member
            response = service.files().list(q="mimeType = 'application/vnd.google-apps.folder' and name = 'ttn_data'",
                                            spaces='drive',
                                            fields='nextPageToken, '
                                                   'files(id, name)',
                                            pageToken=page_token).execute()
            folders = response.get('files', [])
            
            if(len(folders) == 0):
                folder_id = createFolder('ttn_data')
            elif(len(folders) == 1):
                folder_id = folders[0].get("id")
            else:
                folder_id = None
    except HttpError as error:
        print(F'An error occurred: {error}')
        folder_id = None

    return folder_id
        
def createFolder(title):
    creds = CredentialsSpreadSheet()
    service = build('drive', 'v3', credentials=creds)
    file_metadata = {
        'name': title,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    file = service.files().create(body=file_metadata, fields='id').execute()
    print(F'Folder ID: "{file.get("id")}".')
    return file.get('id')

def create(title):
    creds = CredentialsSpreadSheet()
    try:
        service = build('sheets', 'v4', credentials=creds)
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = service.spreadsheets().create(body=spreadsheet, fields='spreadsheetId').execute()
        print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
        return spreadsheet.get('spreadsheetId')
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error
    
    
if __name__ == '__main__':
    search_file()