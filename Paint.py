import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QColorDialog
from PyQt5.QtGui import QImage, QIcon, QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt, QPoint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Paint by DeMoN:D")
        self.setWindowIcon(QIcon("icons/paint.png"))
        self.setGeometry(400, 400, 1024, 768)

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black

        self.lastPoint = QPoint()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        brushMenu = mainMenu.addMenu("Brush size")
        brushColor = mainMenu.addMenu("Color")
        geometryMenu = mainMenu.addMenu("Geometry")

        saveAction = QAction(QIcon("icons/box_green.png"), "Сохранить", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        openAction = QAction(QIcon("icons/box_green.png"), "Открыть", self)
        openAction.setShortcut("Ctrl+O")
        fileMenu.addAction(openAction)
        openAction.triggered.connect(self.openFile)

        clearAction = QAction(QIcon("icons/gnome_edit_clear.png"), "Очистить холст", self)
        clearAction.setShortcut("Ctrl+Z")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        threepxAction = QAction(QIcon("icons/paint.png"), "3px", self)
        threepxAction.setShortcut("Ctrl+K")
        brushMenu.addAction(threepxAction)
        threepxAction.triggered.connect(self.threePx)

        fivepxAction = QAction(QIcon("icons/paint.png"), "5px", self)
        fivepxAction.setShortcut("Ctrl+F")
        brushMenu.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivePx)

        sevenpxAction = QAction(QIcon("icons/paint.png"), "7px", self)
        sevenpxAction.setShortcut("Ctrl+E")
        brushMenu.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenPx)

        ninepxAction = QAction(QIcon("icons/paint.png"), "9px", self)
        ninepxAction.setShortcut("Ctrl+T")
        brushMenu.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninePx)

        blackAction = QAction(QIcon("icons/paint.png"), "Чёрный", self)
        blackAction.setShortcut("Ctrl+B")
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.black)

        redAction = QAction(QIcon("icons/box_red.png"), "Красный", self)
        redAction.setShortcut("Ctrl+R")
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.red)

        greenAction = QAction(QIcon("icons/box_green.png"), "Зелёный", self)
        greenAction.setShortcut("Ctrl+G")
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.green)

        yellowAction = QAction(QIcon("icons/box_yellow.png"), "Жёлтый", self)
        yellowAction.setShortcut("Ctrl+Y")
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellow)

        blueAction = QAction(QIcon("icons/box_blue.png"), "Синий", self)
        blueAction.setShortcut("Ctrl+P")
        brushColor.addAction(blueAction)
        blueAction.triggered.connect(self.blue)

        rgbAction = QAction(QIcon("icons/paint.png"), "Свой цвет(RGB)", self)
        rgbAction.setShortcut("Ctrl+J")
        brushColor.addAction(rgbAction)
        rgbAction.triggered.connect(self.rgb)

        washAction = QAction(QIcon("icons/eraser.png"), "Ластик", self)
        washAction.setShortcut("Ctrl+P")
        brushColor.addAction(washAction)
        washAction.triggered.connect(self.wash)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() and Qt.LeftButton) and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Сохранить изображение", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
        if filePath == "":
            return
        self.image.save(filePath)

    def openFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Загрузить изображение", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
        if filePath == "":
            return
        self.image.load(filePath)

    def clear(self):
        self.image.fill(QColor(255, 255, 255))
        self.update()

    def threePx(self):
        self.brushSize = 3

    def fivePx(self):
        self.brushSize = 5

    def sevenPx(self):
        self.brushSize = 7

    def ninePx(self):
        self.brushSize = 9

    def green(self):
        self.brushColor = QColor(0, 255, 0)

    def yellow(self):
        self.brushColor = QColor(255, 255, 0)

    def blue(self):
        self.brushColor = QColor(0, 0, 255)

    def black(self):
        self.brushColor = QColor(0, 0, 0)

    def red(self):
        self.brushColor = QColor(255, 0, 0)

    def wash(self):
        self.brushColor = QColor(255, 255, 255)

    def rgb(self):
        color = QColorDialog.getColor()
        if color.isValid():
            color.setNamedColor(color.name())
            self.brushColor = color


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    app.exec()
