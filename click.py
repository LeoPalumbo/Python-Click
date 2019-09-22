#install pynput with pip3 install pynput
import time
from pynput.mouse import Button, Controller

mouse=Controller()
print("Start...")
i=0
max_click= 200

while i < max_click:
  mouse.click(Button.left,1)
  i+=1
  time.sleep(0.3)

print("stopped")
