
from PyPDF2 import PdfFileMerger
import os

#Create an instance of PdfFileMerger() class
merger = PdfFileMerger()

#Define the path to the folder with the PDF files
path_to_files = r'input-pdf/'

#Get the file names in the directory
for root, dirs, file_names in os.walk(path_to_files):
    #Iterate over the list of the file names
    print("FILE NAMES :", file_names)
    for file_name in file_names:
        print("file name :", file_name)
        #Append PDF files
        merger.append(path_to_files + file_name)

#Write out the merged PDF file
merger.write("merged_all_pages.pdf")
merger.close()