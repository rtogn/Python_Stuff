
import tkinter as tk
from tkinter import ttk
from Scripts.FileIO import FileInformation, FileExtension, FileMovement
import os
LARGEFONT = ("Verdana", 20)
MEDIUMFONT = ("Verdana", 12)

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

        # to display the current frame passed as

    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Reporting Tools", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=2, padx=10, pady=10)

        button1 = ttk.Button(self, text="\"Do Not Upload\" File Cleanup",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=2, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Under Construction",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=2, padx=10, pady=10)

    # second window frame page1

class Page1(tk.Frame):
    """
    Page for moving to the do not upload folder. Will create sub fodlers
    and will move PDFs and CSVs for numbers listed in selected CSV list
    """
    #GENERAL STRINGS
    title = "Move PDfs and CSVs to DO NOT UPLOAD"
    label1Text = u"Data File Path (.CSV): "
    label2Text = u"Path To Base Folder (Contains PDFs and csv folder): "
    label3Text = u"Path To csv Folder (will auto generate, please verify):"
    emptyPathText = "Click Browse to select!"
    CSVdefaultDir = ""
    fromDefaultDir = ""
    csvDefaultDir = ""
    runButtonText = "Move Files"
    openButtonText = "Open Selected Base Folder"
    backButtonText = "Back to Main Menu"
    instructionButtonText = "Open Instructions"
    instructionFileName = "Reporting Tools Do Not Use Cleanup Instructions.docx"
    descriptionLabelText = "+Please select your csv file in line 1. " \
                           "\n+Column A = Files to move to Do Not Upload" \
                           "\n+Column B = Files to move from rerun to rerun do not upload" \
                           "\n+Then select your primary folder (eg 11Nov2020)" \
                           "\n+The location of the csv files you want to move will generate." \
                           "\n+To move your files select the move files button"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text=self.title, font=MEDIUMFONT)
        label.grid(row=0, column=0, columnspan = 5, padx=10, pady=10)
        controller.geometry("600x500")

        #StringVar values used by the tk entry boxes**********************
        CSVPathText = tk.StringVar()
        CSVPathText.set(self.emptyPathText)
        folderPathText = tk.StringVar()
        folderPathText.set(self.emptyPathText)
        csvFolderPathText = tk.StringVar()
        csvFolderPathText.set(self.emptyPathText)
        #Group1 CSV****************************************************
        self.label1 = tk.Label(self, text=self.label1Text, background= 'lightgreen',
                               anchor="w", font=MEDIUMFONT)
        self.label1.grid(row=1, columnspan=2, sticky='EW')
        self.entry1 = tk.Entry(self, textvariable=CSVPathText)
        self.entry1.grid(row = 2,column=0,columnspan= 4,sticky='EW')

        self.browseButton1 = tk.Button(self,text=u"Browse",
                                command = lambda:
                                GeneralFunctions.OnBrowseClickFile(CSVPathText, self.CSVdefaultDir)
                                       )
        self.browseButton1.grid(row=2,column=4)


        #Group2 BaseFilePath****************************************************
        self.label2 = tk.Label(self, text=self.label2Text, background= 'tan',
                               anchor="w", font=MEDIUMFONT)
        self.label2.grid(row=3, columnspan=2, sticky='EW')
        self.entry2 = tk.Entry(self, textvariable=folderPathText)
        self.entry2.grid(row = 4,column=0,columnspan= 4,sticky='EW')

        self.browseButton2 = tk.Button(self,text=u"Browse",
                                command = lambda:[
                                    GeneralFunctions.OnBrowseClickDir(folderPathText, self.fromDefaultDir),
                                    csvFolderPathText.set(folderPathText.get() + "/" +
                                    FileInformation.getSubfolderString(folderPathText.get(), "csv"))
                                ])

        self.browseButton2.grid(row=4,column=4)

        #Group3 BaseFilePath****************************************************
        self.label3 = tk.Label(self, text=self.label3Text, background= 'tan',
                               anchor="w", font=MEDIUMFONT)
        self.label3.grid(row=5, columnspan=2, sticky='EW')

        self.entry3 = tk.Entry(self, textvariable=csvFolderPathText)
        self.entry3.grid(row = 7,column=0,columnspan= 4,sticky='EW')

        self.browseButton3 = tk.Button(self,text=u"Browse",
                                command = lambda:GeneralFunctions.OnBrowseClickDir(csvFolderPathText, self.csvDefaultDir))
        self.browseButton3.grid(row=7,column=4)

        #Group4 RunButtons****************************************************
        self.moveButton = ttk.Button(self, text=self.runButtonText,
                             command=lambda: GeneralFunctions.moveAndMakeAll(folderPathText.get(), CSVPathText.get()))

        self.moveButton.grid(row=8, column=0, padx=0, pady=0)

        self.openButton = ttk.Button(self, text=self.openButtonText,
                             command=lambda: os.startfile(folderPathText.get()))
        self.openButton.grid(row=8, column=1, padx=0, pady=0)

        self.backButton = ttk.Button(self, text=self.backButtonText,
                             command=lambda: controller.show_frame(StartPage))
        self.backButton.grid(row=9, column=0, padx=10, pady=10)

        self.instructionButton = ttk.Button(self, text=self.instructionButtonText,
                             command=lambda: os.startfile(self.instructionFileName))
        self.instructionButton.grid(row=9, column=1, padx=0, pady=0)


        self.descriptionLabel = tk.Label(self, text=self.descriptionLabelText, background='lightgray',
                               anchor="w", font=MEDIUMFONT)
        self.descriptionLabel.grid(row=11, columnspan=2, sticky='EW')

    # third window frame page2
        self.grid_columnconfigure(0,weight=1)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

class GeneralFunctions:
    def OnBrowseClickDir (targetTkString, defaultDir = ""):
        #sets directory path string via selection box
        targetTkString.set(FileInformation.getDirPath(defaultDir))

    def OnBrowseClickFile (targetTkString, defaultDir = ""):
        #sets CSV path string via selection box
        targetTkString.set(FileInformation.getFilePath(defaultDir, FileExtension.CSV))

    def createFolders (workingDir, newDirPaths: str):
        os.chdir(workingDir)
        try:
            os.makedirs(newDirPaths)
        except:
            pass

    def runMoveFunction (fromDir, toDir, csv, csvCol, extension = FileExtension.PDF):
        """
        :param fromDir: directory to move file
        :param toDir: dir we are moving to
        :param csv: csv file containing a list of files we want to move from the group
        :param extension: target file extension.
        :return:
        """
        dlist = FileInformation.createCSVList (csv, csvCol, False)
        FileMovement.moveTargetFilesByList (dlist, fromDir, toDir, extension)

    def moveAndMakeAll(fromDir, csv):
        #for pg1 button.
        os.chdir (fromDir)
        GeneralFunctions.createFolders (fromDir, "do not upload/csv")
        GeneralFunctions.createFolders (fromDir, "special/csv"),
        GeneralFunctions.createFolders (fromDir, "rerun/csv")
        GeneralFunctions.createFolders(fromDir, "rerun/rerun do not upload/csv")

        GeneralFunctions.runMoveFunction (fromDir, "Do Not Upload", csv, 0, FileExtension.PDF),
        GeneralFunctions.runMoveFunction (f"{fromDir}/csv", f"{fromDir}/Do Not Upload/csv",csv, 0, FileExtension.CSV)

        GeneralFunctions.runMoveFunction (fromDir, f"{fromDir}/rerun/rerun do not upload", csv, 1, FileExtension.PDF),
        GeneralFunctions.runMoveFunction (f"{fromDir}/csv", f"{fromDir}/rerun/rerun do not upload/csv",csv, 1, FileExtension.CSV)


    # def OnFinalClick(self, targetTkCSV, targetTkFolder):
    #     #When viable folder and file are selected run rename routine on the contained files.
    #     try:
    #         patientDict = FileManipulation.createCSVHashMap(targetTkCSV.get())
    #         print("Starting renaming...")
    #         FileManipulation.renameFilesByDict(targetTkFolder.get(), patientDict, FileExtension.PDF)
    #         print("Process Complete!")
    #     except:
    #         print("Invalid directory or file. Choose a correct path.")


if __name__ == "__main__":
    app = tkinterApp()
    app.mainloop()