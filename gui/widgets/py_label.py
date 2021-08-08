from qt_import import *


class PyLabel(QLabel):
    def __init__(
        self,
        text="",
        background_color="",
        color="",
        font="",
        width=0,
        height=0
    ):
        super().__init__()

        self.setText(text)

        style = f"""
            backgroud-color:{background_color};
            color:{color};
            font:{font};
        """
        self.setStyleSheet(style)

        if width is not 0:
            self.setFixedWidth(width)
        if height is not 0:
            self.setFixedHeight(height)
