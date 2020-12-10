import shutil

# Copy and rename a file
shutil.copy('./demo.txt', './demo_copy.txt')

# Copy a and rename a folder
shutil.copytree('./demo', './demo-backup')
