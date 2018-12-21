import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction
from PyQt5.QtGui import QImage, QIcon
from PyQt5.QtCore import Qt, QPoint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Paint by DeMoN:D")
        self.setWindowIcon(QIcon("icons/paint.png"))
        self.setGeometry(400, 400, 800, 600)

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black

        self.lastPoint = QPoint()

        mainMenu = QMenuBar()
        fileMenu = mainMenu.addMenu("File")
        brushMenu = mainMenu.addMenu("Brush size")
        brushColor = mainMenu.addMenu("Color")

        saveAction = QAction(QIcon("icons/paint.png"), "Save", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)

        clearAction = QAction(QIcon("icons/paint.png"), "Clear", self)
        clearAction.setShortcut("Ctrl+Z")
        fileMenu.addAction(clearAction)

        threepxAction = QAction(QIcon("icons/paint.png"), "3px", self)
        threepxAction.setShortcut("Ctrl+T")
        fileMenu.addAction(threepxAction)

        fivepxAction = QAction(QIcon("icons/paint.png"), "5px", self)
        fivepxAction.setShortcut("Ctrl+F")
        fileMenu.addAction(fivepxAction)

        sevenpxAction = QAction(QIcon("icons/paint.png"), "7px", self)
        sevenpxAction.setShortcut("Ctrl+G")
        fileMenu.addAction(sevenpxAction)

        ninepxAction = QAction(QIcon("icons/paint.png"), "9px", self)
        ninepxAction.setShortcut("Ctrl+T")
        fileMenu.addAction(ninepxAction)

        blackAction = QAction(QIcon("icons/paint.png"), "Black", self)
        blackAction.setShortcut("Ctrl+B")
        brushColor.addAction(blackAction)

        redAction = QAction(QIcon("icons/paint.png"), "Red", self)
        redAction.setShortcut("Ctrl+R")
        brushColor.addAction(redAction)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    app.exec()
