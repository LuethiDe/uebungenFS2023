from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *

class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel06/showmap.ui", self)
        self.raise_
        self.show()

        self.button.clicked.connect(self.buttonclick)
        

    def buttonclick(self):
        länge = self.lineEdit.text()
        breite = self.lineEdit_2.text()

        if not länge or not breite:
            QMessageBox.warning(self, "Fehlende Informationen", "Angaben nicht vollständig.", QMessageBox.Ok)
            return

        link = F"https://www.google.ch/maps/place/{länge},+{breite}" 
        QDesktopServices.openUrl(QUrl(link))
        


app = QApplication([])
win = UIFenster()
app.exec()