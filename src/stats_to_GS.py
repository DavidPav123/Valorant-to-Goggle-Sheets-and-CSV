from detect import read_images, export_to_csv
from google_sheets_push import update_sheet
from googleapiclient.errors import HttpError
from json import load
from os.path import exists

def get_spreadsheet_pages():
    with open("config.json", 'r') as file:
        data = load(file)
        return data.get("Spreadsheet Pages", None)
    
def get_spreadsheet_id():
    with open("config.json", 'r') as file:
        data = load(file)
        return data.get("Spreadsheet ID", None)

if __name__ == "__main__":
    credentials_exist = exists("files/credentials.json")
    pages_to_update = []
    spreadsheet_id_exists = False
    spreadsheet_pages_exists = False

    if credentials_exist:
        try:
            spreadsheet_id = get_spreadsheet_id()
            if spreadsheet_id == "" or spreadsheet_id == None:
                print("No spreadsheet ID found!")
            else:
                print(f"Uploading to spreadsheet ID: {spreadsheet_id}")
                spreadsheet_id_exists = True

        except:
            print("No spreadsheet ID found!")
        if spreadsheet_id_exists:
            try:
                pages_to_update = get_spreadsheet_pages()
                if pages_to_update ==  [] or pages_to_update == None:
                    print("No spreadsheet pages found!")
                else:
                    print(f"Uploading to spreadsheet pages: {pages_to_update}")
                    spreadsheet_pages_exists = True
            except:
                print("No spreadsheet pages found!")
    else:
        print("No credentials.json found!")

    if credentials_exist and spreadsheet_id_exists and spreadsheet_pages_exists:
        upload = True
    else:
        upload = False
        print("Not uploading to Google Sheets!")

    try:
        print("Reading game 1 image...")
        stats0 = read_images('screenshots/game1.png')
        print("Game 1 image read!")
        print("Creating game 1 CSV...")
        export_to_csv(stats0, 'game1.csv')
        print("Game 1 CSV created!")

        if upload:
            try:
                print("Uploading game 1...")
                update_sheet(stats0, f"{pages_to_update[0]}!A1:Z26")
                print("Game 1 uploaded!")
            except FileNotFoundError:
                print("No Google Sheets credentials found!")
            except HttpError:
                print("Something went wrong during upload.")

    except FileNotFoundError:
        print("Game 1 file not found!")
    
    try:
        print("Reading game 2 image...")
        stats1 = read_images("screenshots/game2.png")
        print("Game 2 image read!")
        print("Creating game 2 CSV...")
        export_to_csv(stats1, 'game2.csv')
        print("Game 2 CSV created!")

        if upload:
            try:
                print("Uploading game 2...")
                update_sheet(stats1, f"{pages_to_update[1]}!A1:Z26")
                print("Game 2 uploaded!")
            except FileNotFoundError:
                print("No Google Sheets credentials found!")
            except HttpError:
                print("Something went wrong during upload.")

    except FileNotFoundError:
        print("Game 2 file not found!")      

    try:
        print("Reading game 3 image...")
        stats2 = read_images("screenshots/game3.png")
        print("Game 3 image read!")
        print("Creating game 3 CSV...")
        export_to_csv(stats2, 'game3.csv')
        print("Game 3 CSV created!")

        if upload:
            print("Uploading game 3...")
            try:
                update_sheet(stats2, f"{pages_to_update[2]}!A1:Z26")
                print("Game 3 uploaded!")
            except FileNotFoundError:
                print("No Google Sheets credentials found!")
            except HttpError:
                print("Something went wrong during upload.")

    except FileNotFoundError:
        print("Game 3 file not found!")

    input("Press enter to exit:")

