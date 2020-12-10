import os

# Adapted from https://github.com/jsoto3000/os_walk_dir
# Quick print directory contents
for dirpath, dirs, files in os.walk('PATH'):
    path = dirpath.split('/')
    print('|', (len(path))*'---', '[', os.path.basename(dirpath), ']')
    for f in files:
        print('|', len(path)*'---', f)

# Verbose print directory contents
for folderName, subfolders, filenames in os.walk('PATH'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

print('')

# Write directory file tree to file
dirFile = open('current_dir_tree.txt2', 'w')
curFolderName = ('PATH')
dirFile.write('The current folder is ' + curFolderName + '\n\n')

for dirpath, dirs, files in os.walk(curFolderName):
    path = dirpath.split('/')
    dirFile.write('|' + (len(path))*' ' +
                  '[' + os.path.basename(dirpath) + ']' + '\n')
    for f in files:
        dirFile.write('|' + len(path)*' ' + f + '\n')

dirFile.close()
