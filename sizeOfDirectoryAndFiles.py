import os

directory = "YOUR/PATH/TO/DIRECTORY"
totalSize = 0

# get_printable_size function adapted from https://gist.github.com/Pobux/0c474672b3acd4473d459d3219675ad8


def get_printable_size(byte_size):
    BASE_SIZE = 1024.00
    MEASURE = ["B", "KB", "MB", "GB", "TB", "PB"]

    def _fix_size(size, size_index):
        if not size:
            return "0"
        elif size_index == 0:
            return str(size)
        else:
            return "{:.3f}".format(size)

    current_size = byte_size
    size_index = 0

    while current_size >= BASE_SIZE and len(MEASURE) != size_index:
        current_size = current_size / BASE_SIZE
        size_index = size_index + 1

    size = _fix_size(current_size, size_index)
    measure = MEASURE[size_index]
    return size + measure


for file in os.listdir(directory):
    if not(os.path.isfile(os.path.join(directory, file))):
        continue
    else:
        print(file + " : " + get_printable_size(os.path.getsize(os.path.join(
            directory, file))))
        totalSize = totalSize + os.path.getsize(os.path.join(
            directory, file))
print("Total Size : " + get_printable_size(totalSize))
