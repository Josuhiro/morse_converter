from converter import ConvertText

text_converter = ConvertText()
working = True

while working:
    while True:
        choice = input("A) Convert text to morse code\n"
                       "B) Convert morse code to text\n"
                       "If you want to quit type any other character: ")
        if choice.upper() == "A":
            text_converter.set_text()
            text_converter.convert_to_morse()
            text_converter.play_morse_sound()
        elif choice.upper() == "B":
            text_converter.set_morse()
            text_converter.convert_to_text()
        else:
            working = False
            break
