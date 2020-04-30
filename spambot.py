import keyboard
import time

class SpamBot(object):

    loops = 2
    delay = 0.2
    text = 'python here'
    
    def spam(self):
        time.sleep(self.delay)
        keyboard.write(self.text)
        keyboard.press_and_release('enter')
        self.loops -= 1 
        if self.loops >= 1:
            self.spam()
        else:
            print('complited')