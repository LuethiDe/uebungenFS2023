from PyQt5.QtWidgets import *
import csv

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI-Programmierung")

        #layout erzeugen ------------------------------------------------------------
        layout = QFormLayout()


        #menubar erstellen ----------------------------------------------------------
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu("File")

        save = QAction("Save", self)
        save.triggered.connect(self.menu_save)
        
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)

        filemenu.addAction(save)
        filemenu.addAction(quit)


        quit.setMenuRole(QAction.QuitRole)

        #gui Elemente erstellen -----------------------------------------------------
        self.vorname = QLineEdit()
        self.nachname = QLineEdit()

        self.geburtstag = QDateEdit()
        self.geburtstag.setDisplayFormat("dd/MM/yyyy")
        
        self.adresse = QLineEdit()
        self.plz = QLineEdit()
        self.ort = QLineEdit()

        self.land = QComboBox()
        self.land.addItems(["bitte wählen","Deutschland","Österreich","Schweiz","Lichtenstein"])

        save = QPushButton("Save")
        save.clicked.connect(self.save)

     
        #gui Elemente dem Layout hinzufügen -----------------------------------------
        layout.addRow("Vorname:", self.vorname)
        layout.addRow("Nachname:", self.nachname)

        layout.addRow("Geburtstag:", self.geburtstag)

        layout.addRow("Adresse:", self.adresse)

        layout.addRow("PLZ:", self.plz)

        layout.addRow("Ort:", self.ort)

        layout.addRow("Land:", self.land)

        layout.addRow(save)
        

        # Zentrales Widget erstellen und layout hinzufügen --------------------------
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen ---------------------------------
        self.setCentralWidget(center)

        # Fenster anzeigen ----------------------------------------------------------
        self.show()
        self.raise_()

        # Connects erstellen --------------------------------------------------------
        self.vorname.textChanged.connect(self.text)
        self.nachname.textChanged.connect(self.text)

        self.geburtstag.dateChanged.connect(self.datum)

        self.adresse.textChanged.connect(self.text)

        self.plz.textChanged.connect(self.text)

        self.ort.textChanged.connect(self.text)

        self.land.currentIndexChanged.connect(self.combobox_indexchan)


    #Konstruktor Menubefehle --------------------------------------------------------
    
    def menu_save(self):
        with open("output.csv", 'w', encoding="utf-8") as file:
            file = csv.writer(file)
            file.writerow(["Vorname", "Nachname", "Geburtstag", "Adresse", "PLZ", "Ort", "Land"])
            file.writerow([self.vorname.text(), self.nachname.text(), self.geburtstag.text(),
                             self.adresse.text(), self.plz.text(), self.ort.text(), 
                             self.land.currentText()])
        
        print("Datei wurde gesichert")

    #Altenative Speicherung ---------------------------------------------------------
    #def menu_save(self):
    #        filename = QFileDialog.getSaveFileName(self, "Save file", "", "CSV(*.csv)")
    #        if filename:
    #            with open(filename, "w", encoding="utf-8") as file:
    #                file = csv.writer(file)
    #                file.writerow(["Vorname", "Nachname", "Geburtstag", "Adresse", "PLZ", "Ort", "Land"])
    #                file.writerow([self.vorname.text(), self.nachname.text(), self.geburtstag.text(),
    #                            self.adresse.text(), self.plz.text(), self.ort.text(), 
    #                            self.land.currentText()])
    #                print("Datei wurde gesichert")  
    #        else:
    #            print("Datei wurde nicht gesichert")


    def menu_quit(self):
        print("file closed")
        self.close()

    #Konstruktor Widgets ------------------------------------------------------------

    def text(self, text):
        print(text)

    def datum(self, datum):
        print(datum)

    def combobox_indexchan(self, index):
        print(index)

    def save(self,):
        with open("output.csv", 'w', encoding="utf-8") as file:
            file = csv.writer(file)
            file.writerow(["Vorname", "Nachname", "Geburtstag", "Adresse", "PLZ", "Ort", "Land"])
            file.writerow([self.vorname.text(), self.nachname.text(), self.geburtstag.text(),
                             self.adresse.text(), self.plz.text(), self.ort.text(), 
                             self.land.currentText()])
        
        print("Datei wurde gesichert")
    

app = QApplication([])
win = Fenster()
app.exec()