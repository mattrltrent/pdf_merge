from PyPDF2 import PdfFileMerger, PdfFileReader
import os

files = []
 
for entry in os.scandir("tomerge"):
    files.append(entry.path)

mergedObject = PdfFileMerger()

for fileNumber in range(len(files)):
    mergedObject.append(PdfFileReader(files[fileNumber]))

mergedObject.write("merged.pdf")
