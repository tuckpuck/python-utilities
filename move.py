import shutil

# Rename a file
shutil.move('./demo.txt', './demo_renamed.txt')

# Move a file 
shutil.move('./demo2.txt', '/YOUR/PATH/TO/DIRECTORY')

# Move a directory
shutil.move('./demo-backup', '/YOUR/PATH/TO/DIRECTORY')
