from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
from googleapiclient import discovery

# Scopes the program is allowed to access
SCOPES: list[str] = ["https://www.googleapis.com/auth/spreadsheets"]

# ID of spreadsheet to modify
SPREADSHEET_ID: str = "1_s8kTUCKG7wWY43Fa24knmBPAW-iV0uoNBLLUXUxLA0"
# How the input data should be interpreted.
VALUE_INPUT_OPTION: str = "USER_ENTERED"


def update_sheet(values_to_update, range_to_update) -> None:
    creds: Credentials = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow: InstalledAppFlow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = discovery.build("sheets", "v4", credentials=creds)

        value_range_body: dict = {"values": values_to_update}

        request = (
            service.spreadsheets()
            .values()
            .update(
                spreadsheetId=SPREADSHEET_ID,
                range=range_to_update,
                valueInputOption=VALUE_INPUT_OPTION,
                body=value_range_body,
            )
        )
        response = request.execute()

        print(response)
    except HttpError as err:
        print(err)
