import webbrowser
import sys
import pyperclip

# Look up address based on passed arguments
if len(sys.argv) > 1:
    arguments = sys.argv[1:]
    address = ' '.join(arguments)
    webbrowser.open(
        'https://www.google.com/maps/place/' + address)
# Look up address based on latest copied text
elif len(sys.argv[1:]) == 0:
    address = pyperclip.paste()
    webbrowser.open(
        'https://www.google.com/maps/place/' + address)
else:
    # Open Google maps home page
    webbrowser.open('https://www.google.com/maps')
