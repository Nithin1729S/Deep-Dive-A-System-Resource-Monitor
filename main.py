import os
import sys

from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication

from sources.commons import resources  
from sources.screens.mainwind.operations import MainWind


def populate_font_database():
    fontlist = [
        ":/fontrsrc/fonts/intr-bold.ttf",
        ":/fontrsrc/fonts/intr-rlar.ttf",
        ":/fontrsrc/fonts/brlw-rlar.ttf",
        ":/fontrsrc/fonts/fnas-icon.ttf",
    ]
    for indx in fontlist:
        QFontDatabase.addApplicationFont(indx)


def main():
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    QApplication.setStyle("Fusion")
    app = QApplication(sys.argv)
    populate_font_database()
    window = MainWind()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
