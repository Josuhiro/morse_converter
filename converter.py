from dictionary import MORSE_DICTIONARY
import winsound
import time


class ConvertText:

    def __init__(self):
        self.text = ""
        self.morse = ""

    def set_text(self):
        self.text = input("Enter the text to be converted to Morse code (only english characters): ")

    def convert_to_morse(self):
        self.morse = ""
        for char in self.text:
            morse_char = MORSE_DICTIONARY[char.upper()]
            self.morse += morse_char + " "
        print(f" Here is your text converted to morse code: \n{self.morse}")

    def play_morse_sound(self):
        for word in self.morse.split("/"):
            for char in word:
                if char == ".":
                    winsound.Beep(frequency=700, duration=200)
                    time.sleep(0.15)
                elif char == "-":
                    winsound.Beep(frequency=700, duration=500)
                    time.sleep(0.15)
                elif char == " ":
                    time.sleep(0.45)
            time.sleep(1)

    def set_morse(self):
        self.morse = input("Enter the morse code to be converted to text: ")

    def convert_to_text(self):
        self.text = ""
        morse_words = self.morse.split("/")
        for word in morse_words:
            morse_letters = word.split(" ")
            for morse_letter in morse_letters:
                for letter, morse in MORSE_DICTIONARY.items():
                    if morse == morse_letter:
                        self.text += letter
            self.text += " "
        print(f"Here is your morse code converted to text: \n {self.text} \n")
