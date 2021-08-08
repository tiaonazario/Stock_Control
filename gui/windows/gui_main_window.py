from gui.widgets.py_push_button import PyPushButton
from qt_import import *
from gui.widgets.py_frame import *
from gui.widgets.py_label import *


class GUI_MainWindow(object):
    def setup_gui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        parent.resize(1080, 607.5)
        parent.setMinimumSize(540, 303.75)

        # CENTRAL FRAME
        self.central_frame = PyFrame()

        # LEFT FRAME
        self.left_frame = PyFrame(
            layout_type="v",
            background_color="#3a3b3c",
            width=50
        )

        # Top left buttons
        self.toggle_button = PyPushButton(
            text="Ocultar menu",
            icon_path="toggle_icon.svg"
        )
        self.home_button = PyPushButton(
            text="Página inicial",
            is_active=True,
            icon_path="home_icon.svg"
        )
        self.add_button = PyPushButton(
            text="Adicionar",
            icon_path="add_icon.svg"
        )
        self.edit_button = PyPushButton(
            text="Editar",
            icon_path="edit_icon.svg"
        )
        self.delete_button = PyPushButton(
            text="Deletar",
            icon_path="delete_icon.svg"
        )

        # left frame spacer
        self.left_frame_spacer = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Add to left frame layout
        self.left_frame.layout.addWidget(self.toggle_button)
        self.left_frame.layout.addWidget(self.home_button)
        self.left_frame.layout.addWidget(self.add_button)
        self.left_frame.layout.addWidget(self.edit_button)
        self.left_frame.layout.addWidget(self.delete_button)
        self.left_frame.layout.addItem(self.left_frame_spacer)

        # RIGHT FRAME
        self.right_frame = PyFrame(
            layout_type="v",
            background_color="#242526"
        )

        # TOP RIGHT FRAME
        self.top_right_frame = PyFrame(
            layout_type="H",
            background_color="#18191a",
            height=30
        )

        # Title label
        self.title_label = PyLabel(
            text="  Sistema CRUD com Python e PySide6",
            font="700 9pt 'Segoe UI'"
        )

        # Top right frame spacer
        self.top_right_spacer = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Page label
        self.page_label = PyLabel(
            text="| Início  ",
            font="700 9pt 'Segoe UI'"
        )

        # Add to top right frame layout
        self.top_right_frame.layout.addWidget(self.title_label)
        self.top_right_frame.layout.addItem(self.top_right_spacer)
        self.top_right_frame.layout.addWidget(self.page_label)

        # CENTRAL CONTENT
        self.central_content = QStackedWidget()

        # BOTTOM RIGHT FRAME
        self.bottom_right_frame = PyFrame(
            layout_type="H",
            background_color="#18191a",
            height=30
        )

        # Crated by label
        self.created_by_label = PyLabel(
            text="  Criado por: Tião Nazário",
            font="700 9pt 'Segoe UI'"
        )

        # Bottom right frame spacer
        self.bottom_right_spacer = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Copyright label
        self.copyright_label = PyLabel(
            text="© 2021  ",
            font="700 9pt 'Segoe UI'"
        )

        # Add to top right frame layout
        self.bottom_right_frame.layout.addWidget(self.created_by_label)
        self.bottom_right_frame.layout.addItem(self.bottom_right_spacer)
        self.bottom_right_frame.layout.addWidget(self.copyright_label)

        # Add to right frame layout
        self.right_frame.layout.addWidget(self.top_right_frame)
        self.right_frame.layout.addWidget(self.central_content)
        self.right_frame.layout.addWidget(self.bottom_right_frame)

        # Add to central frame layout
        self.central_frame.layout.addWidget(self.left_frame)
        self.central_frame.layout.addWidget(self.right_frame)

        parent.setCentralWidget(self.central_frame)
