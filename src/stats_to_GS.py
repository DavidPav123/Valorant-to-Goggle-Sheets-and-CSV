from detect import read_images, export_to_csv
from google_sheets_push import update_sheet

if __name__ == "__main__":
    stats = read_images('src\screenshots\game1.png')
    update_sheet(stats, "Sheet1!A1:Z26")
    export_to_csv(stats, 'game1.csv')
    stats = read_images("src\screenshots\game2.png")
    update_sheet(stats, "Sheet2!A1:Z26")
    export_to_csv(stats, 'game2.csv')
    stats = read_images("src\screenshots\game3.png")
    update_sheet(stats, "Sheet3!A1:Z26")
    export_to_csv(stats, 'game3.csv')
