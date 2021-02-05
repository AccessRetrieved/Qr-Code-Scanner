from PIL import Image
from pyzbar.pyzbar import decode
import easygui
import rumps
import pyperclip

path = easygui.fileopenbox()
data = decode(Image.open(path))
pyperclip.copy(data[0].data.decode('utf-8'))

rumps.Window(message='Output copied', title='Qr Code', default_text=data[0].data.decode('utf-8')).run()