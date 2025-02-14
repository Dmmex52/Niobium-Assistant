from PyQt6 import QtWidgets, QtCore, QtGui
import sys
import os

class Gui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setFixedSize(400, 600)

        self.settings_icon = QtGui.QIcon(os.path.join(os.path.dirname(__file__), "icons", "settings_icon.png"))
        self.send_icon = QtGui.QIcon(os.path.join(os.path.dirname(__file__), "icons", "send_icon.png"))
        self.close_icon = QtGui.QIcon(os.path.join(os.path.dirname(__file__), "icons", "close_icon.png"))

        screen_geometry = QtWidgets.QApplication.primaryScreen().geometry()
        self.move(
            (screen_geometry.width() - self.width()) // 2,
            (screen_geometry.height() - self.height()) // 2,
        )

        self.background = QtWidgets.QLabel(self)
        self.background.setFixedSize(400, 600)
        self.background.setStyleSheet("background-color: #171717; border: none;")
        self.background.lower()

        self.input_field = QtWidgets.QLineEdit(self)
        self.input_field.setFixedSize(300, 50)
        self.input_field.move(0, 550)
        self.input_field.setStyleSheet("background-color: white; color: black; border-radius: 0; font-size: 18px;")
        self.input_field.setTextMargins(10, 0, 0, 0)
        self.input_field.setPlaceholderText("Ask anything...")
        self.input_field.setMaxLength(100)

        self.send_button = QtWidgets.QPushButton(self)
        self.send_button.setIcon(self.send_icon)
        self.send_button.setIconSize(QtCore.QSize(30, 30))
        self.send_button.setFixedSize(50, 50)
        self.send_button.move(300, 550)
        self.send_button.setStyleSheet("QPushButton { background-color: white; color: black; border: none; } QPushButton:hover { background-color: #e0e0e0; }")

        self.settings_button = QtWidgets.QPushButton(self)
        self.settings_button.setIcon(self.settings_icon)
        self.settings_button.setIconSize(QtCore.QSize(20, 20))
        self.settings_button.setFixedSize(50, 50)
        self.settings_button.setStyleSheet("QPushButton { background-color: white; color: white; border: none;} QPushButton:hover {background-color: #e0e0e0;}")
        self.settings_button.move(350, 550)

        self.close_button = QtWidgets.QPushButton(self)
        self.close_button.setIcon(self.close_icon)
        self.close_button.setIconSize(QtCore.QSize(20, 20))
        self.close_button.setFixedSize(50, 50)
        self.close_button.move(350, 0)
        self.close_button.setStyleSheet("QPushButton { background-color: transparent; border: none; } QPushButton:hover { background-color: #464646; }")
        self.close_button.clicked.connect(self.close)

        self.old_pos = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.old_pos is not None:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.old_pos = None

app = QtWidgets.QApplication(sys.argv)
window = Gui()
window.show()
sys.exit(app.exec())