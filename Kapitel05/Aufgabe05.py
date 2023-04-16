from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import csv

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("layout")

        #layout erzeugen ------------------------------------------------------------
        layout = QFormLayout()

        #menubar erstellen ----------------------------------------------------------
        menubar =  self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu ("File")
        viewmenu = menubar.addMenu ("View")
        
        sichern = QAction("Speichern", self)
        load = QAction("Laden", self)
        quit = QAction("Schliessen", self)
        onMap = QAction("Auf Karte anzeigen", self)

        filemenu.addAction(sichern)
        filemenu.addAction(load)
        filemenu.addAction(quit)
        viewmenu.addAction(onMap)


        #gui Elemente erstellen -----------------------------------------------------
        self.vorname = QLineEdit()
        self.nachname = QLineEdit()

        self.vorname = QLineEdit()

        self.geburtstag = QDateEdit()
        self.geburtstag.setDisplayFormat("dd/MM/yyyy")
        

        self.adresse = QLineEdit()
        self.plz = QLineEdit()
        self.ort = QLineEdit()

        self.land = QComboBox()
        self.land.setEditable(True)
        self.land.addItems(["Deutschland","Österreich","Schweiz","Lichtenstein"])
        self.land.setEditText("Bitte auswählen")

        self.karte = QPushButton("Auf Karte zeigen")
        self.load = QPushButton("Laden")
        self.sichern = QPushButton("Speichern")


        #gui Elemente dem Layout hinzufügen -----------------------------------------
        layout.addRow("Vorname:",self.vorname)
        layout.addRow("Nachname:",self.nachname)
        layout.addRow("Geburtstag:",self.geburtstag)
        layout.addRow("Adresse:",self.adresse)
        layout.addRow("Plz:",self.plz)
        layout.addRow("Ort:",self.ort)
        layout.addRow("Land:",self.land)

        layout.addRow(self.karte)
        layout.addRow(self.load)
        layout.addRow(self.sichern)

        # Connects erstellen --------------------------------------------------------

        self.sichern.clicked.connect(self.speichern)
        sichern.triggered.connect(self.speichern)

        self.load.clicked.connect(self.laden)
        load.triggered.connect(self.laden)

        quit.triggered.connect(self.beenden)

        self.karte.clicked.connect(self.aufKarte)
        onMap.triggered.connect(self.aufKarte)


        # Zentrales Widget erstellen und layout hinzufügen --------------------------
        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        # Fenster anzeigen ----------------------------------------------------------

        self.show()
        self.raise_()


    #Konstruktor Widgets ------------------------------------------------------------
    def text(self):
        pass

    def datum(self):
        pass

    def aufKarte(self):
        adresse = self.adresse.text()
        plz = self.plz.text()
        ort = self.ort.text()
        land = self.land.currentText()

        if not adresse or not plz or not ort or not land:
            QMessageBox.warning(self, "Fehlende Informationen", "Um die Position auf der Karte abzufragen, müssen die Angaben vollständig sein.\nBitte prüfe Adresse, PLZ, Ort und Land.", QMessageBox.Ok)
            return

        link = F"https://www.google.ch/maps/place/{adresse},+{plz}+{ort},+{land}" 
        QDesktopServices.openUrl(QUrl(link))
        

    def laden(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Datei laden", "", "CSV (*.csv)")

        if filename:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    self.vorname.setText(row[0])
                    self.nachname.setText(row[1])
                    self.geburtstag.setDate(QDate.fromString(row[2], "dd/MM/yyyy"))
                    self.adresse.setText(row[3])
                    self.plz.setText(row[4])
                    self.ort.setText(row[5])
                    self.land.setCurrentText(row[6])
                print(f"Die Datei {filename} wurde geöffnet")
        
        else:
            print("abgebrochen")
        

    def speichern(self):
            filename, _ = QFileDialog.getSaveFileName(self, "Datei sichern", "", "CSV (*.csv)")
            file_save = open(filename, "w", encoding="utf-8")

            vorname = self.vorname.text()
            nachname = self.nachname.text()
            geburtstag = self.geburtstag.date().toString("dd/MM/yyyy")
            adresse = self.adresse.text()
            plz = self.plz.text()
            ort = self.ort.text()
            land = self.land.currentText()

            file_save.write(f"{vorname},{nachname},{geburtstag},{adresse},{plz},{ort},{land}")
            print(f"Datei {filename} wurde gesichert")
        

    def beenden(self):
        print("Datei wurde geschlossen")
        self.close()


def main():
    app = QApplication([])  # Qt Applikation erstellen
    mainwindow = Fenster()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()