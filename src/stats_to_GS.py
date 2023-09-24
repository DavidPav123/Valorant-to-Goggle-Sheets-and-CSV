from detect import read_images, export_to_csv
from google_sheets_push import update_sheet
from googleapiclient.errors import HttpError

if __name__ == "__main__":
    try:
        stats0 = read_images('screenshots/game1.png')
        export_to_csv(stats0, 'game1.csv')

        try:
            update_sheet(stats0, "Sheet1!A1:Z26")
        except FileNotFoundError:
            print("No Google Sheets credentials found!")
        except HttpError:
            print("Something went wrong during upload.")

        print("Game 1 analysis complete.")
    except FileNotFoundError:
        print("Game 1 file not found!")
    
    try:
        stats1 = read_images("screenshots/game2.png")
        export_to_csv(stats1, 'game2.csv')

        try:
            update_sheet(stats1, "Sheet2!A1:Z26")
        except FileNotFoundError:
            print("No Google Sheets credentials found!")
        except HttpError:
            print("Something went wrong during upload.")

        print("Game 2 analysis complete.")
    except FileNotFoundError:
        print("Game 2 file not found!")      

    try:
        stats2 = read_images("screenshots/game3.png")
        export_to_csv(stats2, 'game3.csv')

        try:
            update_sheet(stats2, "Sheet3!A1:Z26")
        except FileNotFoundError:
            print("No Google Sheets credentials found!")
        except HttpError:
            print("Something went wrong during upload.")

        print("Game 3 analysis complete.")
    except FileNotFoundError:
        print("Game 3 file not found!")

