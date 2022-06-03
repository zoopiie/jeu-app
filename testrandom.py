

def build_color_string(preffix, suffix, randomcolor):
    refact_char = hex(randomcolor)[2::]  # On enlève le préfixe '0x' de la chaine hexadecimal
    if randomcolor < 16:
        add_char = "0"
        refact_char = "%s%s" % (add_char, refact_char)
    hexcolor = "%s%s%s" % (preffix, refact_char, suffix)
    return hexcolor



def hex_color(randomcolor):
    # 16 x 16 = 256
    # 256 x 6 = 1536 (6 unités dans un hexadécimal #F1A456)
    # 1536 + 4 = 1540 (4 teintes de blanc)
    #randomcolor = random.randint(0, 1540)

    if 0 <= randomcolor <= 255:
        hexcolor= build_color_string("#ff", "00", randomcolor)

    if 256 <= randomcolor <= 511:
        randomcolor = 511 - randomcolor
        hexcolor = build_color_string("#", "ff00", randomcolor)

    if 512 <= randomcolor <= 767:
        randomcolor = randomcolor - 512
        hexcolor = build_color_string("#ff00", "", randomcolor)

    if 768 <= randomcolor <= 1023:
        randomcolor = 1023 - randomcolor
        hexcolor = build_color_string("#00", "ff", randomcolor)

    if 1024 <= randomcolor <= 1279:
        randomcolor = randomcolor - 1024
        hexcolor = build_color_string("#", "00ff", randomcolor)

    if 1278 <= randomcolor <= 1535:
        randomcolor = 1535 - randomcolor
        hexcolor = build_color_string("#ff00", "", randomcolor)


    if 1536 <= randomcolor:
        hexcolor = "#ffffff"

    return hexcolor

while True:
    color = int(input("donne un chiffre  :"))
    print(hex_color(color))