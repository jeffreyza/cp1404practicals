"""
CP1404/CP5632 Practical
Jeffrey Timms
Hexadecimal colour picker
"""

COLOR_HEX = {"blanchedalmond": "#ffebcd", "brown": "#a52a2a", "cadetblue": "#5f9ea0", "coral": "#ff7f50",
             "cornflowerblue": "#6495ed", "darkgreen": "#006400", "darkorange": "#ff8c00", "darkviolet": "#9400d3",
             "ghostwhite": "#f8f8ff", "goldenrod": "#daa520"}

color_choice = input("What color would you like to get the hexadecimal code for? ").lower()
while color_choice != "":
    if color_choice in COLOR_HEX:
        print(color_choice, "hexadecimal is", COLOR_HEX[color_choice])
    else:
        print("Invalid color choice!")
    color_choice = input("What color would you like to get the hexadecimal code for? ")
