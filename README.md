# 1to50-Game-Hack
A python project to finish the 1 to 50 Game within 2 secs 😎 using Tesseract OCR engine

# Description
This is a fun project i made for solving the 1to50 game available at https://zzzscore.com/1to50/en/

Make sure to try it out yourselves first.
The project works only for this website.
You can follow me to get more awesome projects :thumbsup:

## System Requirements
1. Windows OS
2. Internet Connection (LOL)
3. Tesseract installed on PC which you can get here -> https://digi.bib.uni-mannheim.de/tesseract/ (Just download any .exe file and install and add the exe file path to system variables)

## Instructions to run the project
1. Clone or Download the project to your PC.
2. Open https://zzzscore.com/1to50/en/ in your browser of choice.
3. Scroll down until the grey line below the advert in exactly below the timer 0.00.
3. Printscreen and paste image in paint.
4. Make sure these values are same in the code. If not then change it.
![PrintScreen image](https://i.imgur.com/7f4IBXM.png)

5. Pip install all the required libraries 
`pip install pillow pynput numpy time pyscreenshot`

6. Now run the code and switch to the game tab.
7. By default press the left ctrl button and see the magic happen.

## Average time of solve : 2.05 s

## Working
The code simply takes a screenshot of the screen area twice. Once initially and once when the first 25 are clicked.
The screenshot is processed, tiled to 25 images, recombined with a buffer for high accuracy and then sent for OCR using tesseract.
The output list is mapped for the position of each number and mouse is moved and clicked.

# Thank You for checking out this project. :pray:
