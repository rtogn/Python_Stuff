import os
from enum import Enum
from tkinter import *
# import shutil
# import datetime as dt
from tkinter import filedialog  # tkinter needs some methods imported one at a time


class FileExtension(Enum):
    #Enum for common file extensions used by the program. Feel free to add but dotn forget the manditory '.'
    EXCELL = ".xlsx"
    CSV = ".csv"
    PDF = ".pdf"
    TEXT = ".txt"
    PYTHON = ".py"
    ALL = "" #use all types

class FileInformation:
#static methods for selecting or getting file strings or creating lists out of provided files

    def getFilePath (defaultDir = "", fileType = FileExtension.ALL):
    #Opens standard file/dir slection UI. Optional FileExtension obj argument filters for one extension
        desktopDir = defaultDir
        assert isinstance(fileType, FileExtension)
        Tk().withdraw()  # closes empty TK box. TKinter specific method and object.

        fileName = filedialog.askopenfilename(
            initialdir= desktopDir,
            filetypes = [("extensionType", f"*{fileType.value}")]
        )  # this will open a file select dialog with default dir as the users Desktop
        return fileName

    @staticmethod
    def getDirPath(defaultDir = ""):
    #Opens standard file/dir slection UI. Returns full path of slected directory
        desktopDir = defaultDir
        Tk().withdraw()  # closes empty TK box. TKinter specific method and object.
        dirName = filedialog.askdirectory(initialdir= desktopDir)
        return dirName

    def createCSVList (fileName, column=0, skipHeaders=True):
        """
        :param column: column to look at. Defaults to the first column in the csv
        :param skipHeaders: set to false if there is no Header line in the CSV
        :return: List representing items in provided CSV List
        """
        import csv
        file = open(fileName)
        reader = csv.reader(file, delimiter=',')
        itemList = []

        if skipHeaders:
            next(reader, None)  # skip headers in csv

        for row in reader:
            rNum = row[column].strip()
            itemList.append(rNum)
        return itemList

    def createCSVHashMap (fileName, skipHeaders=True): # update to be non specific for file name
        import csv
        # loads csv and creates a hash table with first row value (row[0]) to a file name composed of parts of that row
        # currently is specific to labgenoutput.
        # always .strip() entries to remove space.
        # Use False as argument for skipHeaders to include the header row in the hashmap

        print("Creating hash table...")
        file = open(fileName)
        reader = csv.reader(file, delimiter=',')
        patientDict = {}

        if skipHeaders:
            next(reader, None)  # skip headers in csv

        for row in reader:
            rNum = row[0].strip()
            rName = row[3].strip()
            rInsType = row[7].strip()
            newFileName = rNum + " " + "_internal" + " " + rName + " " + rInsType
            patientDict[rNum] = newFileName
        print("...Hash table complete.")
        return patientDict

    def renameFilesByDict (targetDir, newFileNameDictionary, targetExtension = FileExtension.PDF):
        """
        use FileExtension.ALL or leave arg blank to look at all filetypes
        give full path string of darget directory. Use getDirPath in FileIO.getDirPath
        name dictionary needs to be a map that will take name of file and map it to a determined filename based on our file
        renames all files in a given directory to their corresponding name given in a dictionary map
        """
        os.chdir(targetDir)
        fileCount = 0
        skippedFileCount = 0

        for fileName in os.listdir (targetDir):
            fileNameNoExtension = fileName[0:len(fileName) - len(targetExtension.value)]
            try:
                if fileName.lower().endswith(targetExtension.value):
                    os.rename(fileName, f"{newFileNameDictionary[fileNameNoExtension]}{targetExtension.value}")
                    fileCount += 1
            except:
                print("File not renamed: " + fileName)
                skippedFileCount += 1
                pass
        print(f"{fileCount} files have been renamed. {skippedFileCount} were not listed in the selected source data.")

    def getSubfolderString (targetDir, targetFolderName: str):
        #Cehck and fetch for desired sub folder/file in a directory
        os.chdir(targetDir)
        try:
            for fileString in os.listdir():
                if targetFolderName == fileString.lower():
                    return fileString
        except:
            print("Invalid Directory")
            return ""

class FileMovement:
    #static methods for moving and copying files around
    @staticmethod
    def moveTargetFilesByList (targetList, dirFrom, dirTo, fileExtension, startWith = True):
        """
        Move files in directory listed in target list to destination.
        optional argument startWith: Set to end to check end of string instead of the start
        based on the target list string.
        function assumes every entry in the list is of same length
        """
        import os, shutil
        assert isinstance(fileExtension, FileExtension) #strictly necessary? no.
        tokenLength = len(targetList[0])
        hashMap = {}
        count = 0
        if startWith:
            #for all the files in the dir:
                #add to hashmap: key = value matching list value = full file name
            for fileName in os.listdir(dirFrom):
                hashMap[fileName[0:tokenLength]] = fileName
        else:
            for fileName in os.listdir(dirFrom):
                #to reach the end of the file string account for fileExtension
                #for example: .pdf we offset our start by 4 (the char length of the extension)
                #lot of erroneous variables here for what could be one line, but it kind of clears up what is going on.
                extLen = len(fileExtension.value)
                fileLen = len(fileName)
                stringStart = fileLen - extLen - tokenLength
                endPreExt = fileLen - extLen
                hashMap[fileName[stringStart:endPreExt]] = fileName

        os.chdir(dirFrom)
        for item in targetList:
            try:
                dest = os.path.join(dirTo,hashMap[item])
                shutil.move(hashMap[item], dest)
                count += 1
            except:
                print("Item from list: " + item + " not found as a " + fileExtension.value + ". Pass.")
        print(str(count) + " " + fileExtension.value + "s matched and moved")


if __name__ == '__main__':

    print(FileInformation.getDirPath())
