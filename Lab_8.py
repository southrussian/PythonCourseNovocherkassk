# importing the "tarfile" module
import tarfile

# open file
file = tarfile.open('points.tar.gz')

# extracting file
file.extractall('./tar_folder')

file.close()
