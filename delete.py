import os
import shutil
import send2trash

# delete a single file
os.unlink('./demo.txt')

# delete an empty directory
os.rmdir('./demo')

# delete a directory and its contents
shutil.rmtree('./demo')

# send file or folder to OS trash instead of deleting permanently
send2trash.send2trash('./demo.txt')
