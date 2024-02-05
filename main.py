import sys

from PyQt5.QtWidgets import QApplication

from screens.mainwind.mainwind_op import MainApp


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
