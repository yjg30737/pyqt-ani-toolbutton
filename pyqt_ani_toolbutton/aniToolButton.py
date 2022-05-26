from PyQt5.QtWidgets import QToolButton
from pyqt_ani_abstractbutton import AniAbstractButton


class AniToolButton(QToolButton, AniAbstractButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)