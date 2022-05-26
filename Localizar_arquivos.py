from tkinter import filedialog
from tkinter import messagebox


class LocalizarArquivos:

    def pdfFiles(self, label_pdf):
        """
        solicita ao usuario localizar o pdf através de uma janela
        """
        filenamePDF = filedialog.askopenfilename(initialdir="/",
                                                      title="Selecionar o Arquivo",
                                                      filetypes=(('Adobe Acrobat Document', '*.pdf'),
                                                                 ("all files", "*.*")))

        label_pdf.configure(text=filenamePDF)
        
        return filenamePDF

    def exlFiles(self, label_excel):
        """
        solicita ao usuario localizar o excel através de uma janela

        """
        filenameEXL = filedialog.askopenfilename(initialdir="/",
                                                 title="Selecionar o Arquivo",
                                                 filetypes=(('Microsoft Excel Worksheet', '*.xlsx'),
                                                            ("all files", "*.*")))
        label_excel.configure(text=filenameEXL)
        return filenameEXL