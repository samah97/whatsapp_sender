# This is a sample Python script.
import whatsapp
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from whatsapp import Whatsapp


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    instance = whatsapp.Whatsapp()
    instance.do_action("+9613721112","Heyy",5)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
