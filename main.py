import os

source='main.txt'
destination='newFile.txt'
os.rename(source,destination)
print('The Source Path has been renamed to the Destination Path Successfully')