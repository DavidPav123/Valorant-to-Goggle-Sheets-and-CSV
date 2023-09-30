# Valorant matches data to Google Sheets and CSV

## Usage:

1. Download the latest release of this project and unzip it.
2. Download Tesseract OCR from the following link and install it on your computer, taking note of the location it is installed to: https://github.com/UB-Mannheim/tesseract/wiki.
3. In the ***config.json*** file change the ***Spreadsheet ID*** parameter to your spreadsheets ID.
4. In the ***config.json*** file change the ***Spreadsheet Pages*** parameter to the pages where the data should be uploaded.
5. In the ***config.json*** file change the ***Tesseract OCR Path*** parameter to the location of Tesseract OCR noted earlier.
6. Place a ***credentials.json*** file containing google sheets api key in the ***files*** folder. The first time the program is run it will prompt for a login.
7. To run the program put up to three screenshots of the Valorant end game screen in the ***screenshots*** folder and name them game1.png, game2.png, and game3.png. Run ***stats_to_GS.exe*** by double-clicking on it or through the terminal to if debug information is desired. The information extracted will be uploaded to the specified spreadsheet and exported to CSV files in the ***CSV*** folder.

## Notes:
- Non english characters will not be detected properly and will need to be manually inputted.
- Characters may not be detected properly due to missing images or lack of image data.
- If a CSV file is open when the program attemps to write to it, the program will crash.
