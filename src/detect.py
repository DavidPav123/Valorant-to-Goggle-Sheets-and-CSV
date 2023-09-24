import pytesseract
import cv2
import numpy as np
from ntpath import basename
from glob import glob
from os.path import splitext
from PIL import Image
from csv import writer

def create_images(file_path) -> None:
    im = Image.open(file_path)

    # Plyer 1 stats
    name_1 = im.crop((335, 355, 485, 380)).resize((300, 50))
    name_1.save( "files/images/P1/name.jpg", "png")
    kills_1 = im.crop((835, 345, 870, 380)).resize((100, 100))
    kills_1.save("files/images/P1/kills.jpg", "png")
    Deaths_1 = im.crop((885, 345, 920, 380)).resize((100, 100))
    Deaths_1.save("files/images/P1/Deaths.jpg", "png")
    Assists_1 = im.crop((935, 345, 970, 380)).resize((100, 100))
    Assists_1.save("files/images/P1/Assists.jpg", "png")
    Character_1 = im.crop((280, 340, 340, 390))
    Character_1.save("files/images/P1/Character.jpg", "png")
    ACS_1 = im.crop((705, 345, 755, 380)).resize((100, 100))
    ACS_1.save("files/images/P1/ACS.jpg", "png")
    FB_1 = im.crop((1175, 345, 1225, 380)).resize((100, 100))
    FB_1.save("files/images/P1/FB.jpg", "png")
    

    # Player 2 stats
    name_2 = im.crop((335, 405, 485, 430)).resize((300, 50))
    name_2.save("files/images/P2/name.jpg", "png")
    kills_2 = im.crop((835, 400, 870, 435)).resize((100, 100))
    kills_2.save("files/images/P2/kills.jpg", "png")
    Deaths_2 = im.crop((885, 400, 920, 435)).resize((100, 100))
    Deaths_2.save("files/images/P2/Deaths.jpg", "png")
    Assists_2 = im.crop((935, 400, 970, 435)).resize((100, 100))
    Assists_2.save("files/images/P2/Assists.jpg", "png")
    Character_2 = im.crop((280, 393, 340, 443))
    Character_2.save("files/images/P2/Character.jpg", "png")
    ACS_2 = im.crop((705, 400, 755, 435)).resize((100, 100))
    ACS_2.save("files/images/P2/ACS.jpg", "png")
    FB_2 = im.crop((1175, 400, 1225, 435)).resize((100, 100))
    FB_2.save("files/images/P2/FB.jpg", "png")

    # Player 3 stats
    name_3 = im.crop((335, 460, 485, 485)).resize((300, 50))
    name_3.save("files/images/P3/name.jpg", "png")
    kills_3 = im.crop((835, 450, 870, 485)).resize((100, 100))
    kills_3.save("files/images/P3/kills.jpg", "png")
    Deaths_3 = im.crop((885, 450, 920, 485)).resize((100, 100))
    Deaths_3.save("files/images/P3/Deaths.jpg", "png")
    Assists_3 = im.crop((935, 450, 970, 485)).resize((100, 100))
    Assists_3.save("files/images/P3/Assists.jpg", "png")
    Character_3 = im.crop((280, 445, 340, 495))
    Character_3.save("files/images/P3/Character.jpg", "png")
    ACS_3 = im.crop((705, 450, 755, 485)).resize((100, 100))
    ACS_3.save("files/images/P3/ACS.jpg", "png")
    FB_3 = im.crop((1175, 450, 1225, 485)).resize((100, 100))
    FB_3.save("files/images/P3/FB.jpg", "png")

    # Player 4 stats
    name_4 = im.crop((335, 510, 485, 535)).resize((300, 50))
    name_4.save("files/images/P4/name.jpg", "png")
    kills_4 = im.crop((835, 505, 870, 540)).resize((100, 100))
    kills_4.save("files/images/P4/kills.jpg", "png")
    Deaths_4 = im.crop((885, 505, 920, 540)).resize((100, 100))
    Deaths_4.save("files/images/P4/Deaths.jpg", "png")
    Assists_4 = im.crop((935, 505, 970, 540)).resize((100, 100))
    Assists_4.save("files/images/P4/Assists.jpg", "png")
    Character_4 = im.crop((280, 497, 340, 547))
    Character_4.save("files/images/P4/Character.jpg", "png")
    ACS_4 = im.crop((705, 505, 755, 540)).resize((100, 100))
    ACS_4.save("files/images/P4/ACS.jpg", "png")
    FB_4 = im.crop((1175, 505, 1225, 540)).resize((100, 100))
    FB_4.save("files/images/P4/FB.jpg", "png")

    # Player 5 stats
    name_5 = im.crop((335, 560, 485, 585)).resize((300, 50))
    name_5.save("files/images/P5/name.jpg", "png")
    kills_5 = im.crop((835, 555, 870, 590)).resize((100, 100))
    kills_5.save("files/images/P5/kills.jpg", "png")
    Deaths_5 = im.crop((885, 555, 920, 590)).resize((100, 100))
    Deaths_5.save("files/images/P5/Deaths.jpg", "png")
    Assists_5 = im.crop((935, 555, 970, 590)).resize((100, 100))
    Assists_5.save("files/images/P5/Assists.jpg", "png")
    Character_5 = im.crop((280, 549, 340, 599))
    Character_5.save("files/images/P5/Character.jpg", "png")
    ACS_5 = im.crop((705, 555, 755, 590)).resize((100, 100))
    ACS_5.save("files/images/P5/ACS.jpg", "png")
    FB_5 = im.crop((1175, 555, 1225, 590)).resize((100, 100))
    FB_5.save("files/images/P5/FB.jpg", "png")

    # Player 6 stats
    name_6 = im.crop((335, 615, 485, 640)).resize((300, 50))
    name_6.save("files/images/P6/name.jpg", "png")
    kills_6 = im.crop((835, 610, 870, 645)).resize((100, 100))
    kills_6.save("files/images/P6/kills.jpg", "png")
    Deaths_6 = im.crop((885, 610, 920, 645)).resize((100, 100))
    Deaths_6.save("files/images/P6/Deaths.jpg", "png")
    Assists_6 = im.crop((935, 610, 970, 645)).resize((100, 100))
    Assists_6.save("files/images/P6/Assists.jpg", "png")
    Character_6 = im.crop((280, 601, 340, 651))
    Character_6.save("files/images/P6/Character.jpg", "png")
    ACS_6 = im.crop((705, 610, 755, 645)).resize((100, 100))
    ACS_6.save("files/images/P6/ACS.jpg", "png")
    FB_6 = im.crop((1175, 610, 1225, 645)).resize((100, 100))
    FB_6.save("files/images/P6/FB.jpg", "png")

    # Player 7 stats
    name_7 = im.crop((335, 665, 485, 690)).resize((300, 50))
    name_7.save("files/images/P7/name.jpg", "png")
    kills_7 = im.crop((835, 660, 870, 695)).resize((100, 100))
    kills_7.save("files/images/P7/kills.jpg", "png")
    Deaths_7 = im.crop((885, 660, 920, 695)).resize((100, 100))
    Deaths_7.save("files/images/P7/Deaths.jpg", "png")
    Assists_7 = im.crop((935, 660, 970, 695)).resize((100, 100))
    Assists_7.save("files/images/P7/Assists.jpg", "png")
    Character_7 = im.crop((280, 653, 340, 703))
    Character_7.save("files/images/P7/Character.jpg", "png")
    ACS_7 = im.crop((705, 660, 755, 695)).resize((100, 100))
    ACS_7.save("files/images/P7/ACS.jpg", "png")
    FB_7 = im.crop((1175, 660, 1225, 695)).resize((100, 100))
    FB_7.save("files/images/P7/FB.jpg", "png")

    # Player 8 stats
    name_8 = im.crop((335, 715, 485, 740)).resize((300, 50))
    name_8.save("files/images/P8/name.jpg", "png")
    kills_8 = im.crop((835, 710, 870, 745)).resize((100, 100))
    kills_8.save("files/images/P8/kills.jpg", "png")
    Deaths_8 = im.crop((885, 710, 920, 745)).resize((100, 100))
    Deaths_8.save("files/images/P8/Deaths.jpg", "png")
    Assists_8 = im.crop((935, 710, 970, 745)).resize((100, 100))
    Assists_8.save("files/images/P8/Assists.jpg", "png")
    Character_4 = im.crop((280, 705, 340, 755))
    Character_4.save("files/images/P8/Character.jpg", "png")
    ACS_8 = im.crop((705, 710, 755, 745)).resize((100, 100))
    ACS_8.save("files/images/P8/ACS.jpg", "png")
    FB_8 = im.crop((1175, 710, 1225, 745)).resize((100, 100))
    FB_8.save("files/images/P8/FB.jpg", "png")

    # Player 9 stats
    name_9 = im.crop((335, 770, 485, 795)).resize((300, 50))
    name_9.save("files/images/P9/name.jpg", "png")
    kills_9 = im.crop((835, 765, 870, 800)).resize((100, 100))
    kills_9.save("files/images/P9/kills.jpg", "png")
    Deaths_9 = im.crop((885, 765, 920, 800)).resize((100, 100))
    Deaths_9.save("files/images/P9/Deaths.jpg", "png")
    Assists_9 = im.crop((935, 765, 970, 800)).resize((100, 100))
    Assists_9.save("files/images/P9/Assists.jpg", "png")
    Character_4 = im.crop((280, 757, 340, 807))
    Character_4.save("files/images/P9/Character.jpg", "png")
    ACS_9 = im.crop((705, 765, 755, 800)).resize((100, 100))
    ACS_9.save("files/images/P9/ACS.jpg", "png")
    FB_9 = im.crop((1175, 765, 1225, 800)).resize((100, 100))
    FB_9.save("files/images/P9/FB.jpg", "png")

    # Player 10 stats
    name_10 = im.crop((335, 820, 485, 845)).resize((300, 50))
    name_10.save("files/images/P9+1/name.jpg", "png")
    kills_10 = im.crop((835, 815, 870, 850)).resize((100, 100))
    kills_10.save("files/images/P9+1/kills.jpg", "png")
    Deaths_10 = im.crop((885, 815, 920, 850)).resize((100, 100))
    Deaths_10.save("files/images/P9+1/Deaths.jpg", "png")
    Assists_10 = im.crop((935, 815, 970, 850)).resize((100, 100))
    Assists_10.save("files/images/P9+1/Assists.jpg", "png")
    Character_4 = im.crop((280, 809, 340, 859))
    Character_4.save("files/images/P9+1/Character.jpg", "png")
    ACS_10 = im.crop((705, 815, 755, 850)).resize((100, 100))
    ACS_10.save("files/images/P9+1/ACS.jpg", "png")
    FB_10 = im.crop((1175, 815, 1225, 850)).resize((100, 100))
    FB_10.save("files/images/P9+1/FB.jpg", "png")


def run_comparison(file_path) -> str:
    img1 = cv2.imread(file_path, 0)
    chars = glob("files/char_check/*")
    comparisons = [chars, []]

    for image in chars:
        img2 = cv2.imread(image, 0)

        # --- take the absolute difference of the images ---
        res = cv2.absdiff(img1, img2)

        # --- convert the result to integer type ---
        res = res.astype(np.uint8)

        # --- find percentage difference based on number of pixels that are not zero ---
        percentage = (np.count_nonzero(res) * 100) / res.size
        comparisons[1].append(percentage)
    return splitext(
        basename(comparisons[0][comparisons[1].index(min(comparisons[1]))])
    )[0].split("_", 1)[0]


def read_images(file_path):
    player_arr = [
        ["Name", "Agent", "ACS", "Kills", "Deaths", "Assists", "First Bloods"],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    ]
    # Create screenshots from initial screenshot
    create_images(file_path)

    # Defining paths to tesseract.exe
    path_to_tesseract: str = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

    folders = glob("files/images/*")

    for i in range(1, len(folders) + 1):
        # Name
        image_path = f"{folders[i -1 ]}/name.jpg"
        image = cv2.imread(image_path, 0)
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[
            1
        ]
        data = pytesseract.image_to_string(thresh, lang="eng", config="--psm 6")
        player_arr[i].append(data.strip())

        # Character
        image_path = f"{folders[i - 1]}/Character.jpg"
        player_arr[i].append(run_comparison(image_path))

        # ACS
        image_path = f"{folders[i - 1]}/ACS.jpg"
        image = cv2.imread(image_path, 0)
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[
            1
        ]
        data = pytesseract.image_to_string(
            thresh, lang="eng", config="--psm 6 -c tessedit_char_whitelist=0123456789"
        )
        player_arr[i].append(data.strip())

        # Kills
        image_path = f"{folders[i - 1]}/Kills.jpg"
        image = cv2.imread(image_path, 0)
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[
            1
        ]
        data = pytesseract.image_to_string(
            thresh, lang="eng", config="--psm 6 -c tessedit_char_whitelist=0123456789"
        )
        player_arr[i].append(data.strip())

        # Assists
        image_path = f"{folders[i - 1]}/Assists.jpg"
        image = cv2.imread(image_path, 0)
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[
            1
        ]
        data = pytesseract.image_to_string(
            thresh, lang="eng", config="--psm 6 -c tessedit_char_whitelist=0123456789"
        )
        player_arr[i].append(data.strip())

        # Deaths
        image_path = f"{folders[i - 1]}/Deaths.jpg"
        image = cv2.imread(image_path, 0)
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[
            1
        ]
        data = pytesseract.image_to_string(
            thresh, lang="eng", config="--psm 6 -c tessedit_char_whitelist=0123456789"
        )
        player_arr[i].append(data.strip())

        # First Bloods
        image_path = f"{folders[i - 1]}/FB.jpg"
        image = cv2.imread(image_path, 0)
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[
            1
        ]
        data = pytesseract.image_to_string(
            thresh, lang="eng", config="--psm 6 -c tessedit_char_whitelist=0123456789"
        )
        player_arr[i].append(data.strip())
        

    return player_arr

def export_to_csv(rows,file_name):
    with open(f'CSVs/{file_name}', 'w') as f:
        write = writer(f, delimiter=',', lineterminator="\n")
        write.writerows(rows)
