import pyautogui
import pynput
import PIL
from PIL import Image
from pynput import mouse
from pynput import keyboard
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key, Controller as KeyController

mouse = MouseController()

print("Waiting for user to press F3...")

def on_press(key):
        None
    
def on_release(key):
    if key == keyboard.Key.f3:
        print("F3 pressed, determining the color of the pixel your cursor was on...")
        screenshot = pyautogui.screenshot()
        screenshot.save("./screenshot.jpg")
        screenshot = PIL.Image.open("./screenshot.jpg")
        screenshot_rgb = screenshot.convert("RGB")
        pixel_color = screenshot_rgb.getpixel(mouse.position)
        pixel_color_str = str(pixel_color)
        print("The RGB value of the pixel your mouse was on is: " + pixel_color_str)
        try:
            f = open("rgb.txt", 'x')
            f.close()
        except FileExistsError:
            None
        f = open("rgb.txt", 'w')
        f.write("The RGB value of the pixel your mouse was on is: " + pixel_color_str)
        f.close()
        
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
