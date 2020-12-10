import shutil

# Rename a file
shutil.move('./demo.txt', './demo_renamed.txt')

# Move a file
shutil.move('./demo2.txt', '/PATH/TO/DIRECTORY')

# Move a directory
shutil.move('./demo-backup', '/PATH/TO/DIRECTORY')
