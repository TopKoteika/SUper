import json 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.notes = {
            "Перша замітка":{
                "текст":"Це текст першої замітки",
                "теги": []
            }
        }
        self.ui.listWidget.addItems(self.notes)
        self.ui.listWidget.itemClicked.connect(self.show_note)
        self.ui.save_btn.clicked.connect(self.save_notes)



    def show_note( self):
        name = self.ui.listWidget.selectedItems()[0].text()
        self.ui.title.setText(name)
        self.ui.texp.setText(self.notes[name]["текст"])


    def save_notes(self):
        self.notes[self.ui.title.text()] = self.ui.texp.toPlainText()
        with open("notes.json","w", encoding="utf-8") as file:
            json.dump(self.notes , file)








app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
