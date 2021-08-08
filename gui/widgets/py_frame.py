from qt_import import *


class PyFrame(QFrame):
    def __init__(
        self,
        layout_type="h",
        background_color="#3a3b3c",
        color="#b1b3b7",
        width=0,
        height=0
    ):
        super().__init__()
        # FRAME
        style = f"""
            background-color: {background_color};
            color: {color};
        """
        self.setStyleSheet(style)
        if width is not 0:
            self.setFixedWidth(width)
        if height is not 0:
            self.setFixedHeight(height)

        # CHECK LAYOUT TYPE
        if layout_type.lower() == "h" or layout_type.lower() == "horizontal":
            self.layout = QHBoxLayout(self)
        elif layout_type.lower() == "v" or layout_type.lower() == "vertical ":
            self.layout = QVBoxLayout(self)
        else:
            self.layout = QGridLayout(self)

        # CONFIGURE LAYOUT
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
