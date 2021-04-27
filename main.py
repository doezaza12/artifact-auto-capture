import time
import argparse
from pynput.keyboard import Key, Listener
from config import Configuration
from imageProcess import screenshot

def readKey(key):
    # global exit
    # exit = False

    print('{0} pressed'.format(key))

    # take screenshot
    if key == Key.print_screen:
        screenshot()
        time.sleep(1)
    # exit key monitoring
    elif key == Key.esc:
        # exit = True
        return False

def main():
    # initiallize file path for save screenshot
    # Configuration.setSaveImagePath()
    print('start working.')

    Configuration.setSaveAnnotationPath('artifactsAnnotations')
    Configuration.setSaveImagePath('artifactsImages')

    with Listener(on_press=readKey) as listener:
        listener.join()

if __name__ == '__main__':
    main()