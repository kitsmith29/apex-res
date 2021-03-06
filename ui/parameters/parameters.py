from pathlib import Path
import sys

root_dir = (Path(__file__).parent / "../../").resolve()
sys.path.append(str(root_dir))

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QGridLayout,
    QSizePolicy,
    QHBoxLayout,
    QFrame,
)

from .group import ParametersGroupWidget
from .names import (
    ParameterGroupNames,
    InstrumentParameterNames,
    MethodParameterNames,
    PeakParameterNames,
)


class ParametersWidget(QWidget):
    def __init__(self, optimiser):
        super(ParametersWidget, self).__init__()

        self.optimiser = optimiser

        self._configure()

    def add_parameters(self):
        self.instrument = ParametersGroupWidget(
            self.optimiser, ParameterGroupNames.INSTRUMENT
        )
        self.method = ParametersGroupWidget(self.optimiser, ParameterGroupNames.METHOD)
        # peak_parameters = ParametersGroupWidget(
        #     self.optimiser, ParameterGroupNames.PEAKS
        # )

        self.parameters = self.instrument.parameters + self.method.parameters

        self.layout.addWidget(self.instrument, 1, 0, 1, 1)
        self.layout.addWidget(self.method, 2, 0, 1, 1)
        # self.layout.addWidget(peak_parameters, 1, 4, 1, 1)

    def _configure(self):
        self.setObjectName("ParametersWidget")

        self._configure_layouts()
        self._configure_fonts()

        # self._add_background()
        self._add_label()

    def _configure_layouts(self):
        self.layout = QGridLayout(self)

        self.layout.setContentsMargins(20, 2, 20, 0)
        self.layout.setSpacing(10)

        self.layout.setColumnMinimumWidth(1, 1)
        self.layout.setColumnMinimumWidth(0, 3)

    def _configure_fonts(self):
        self.font_title = QFont()
        self.font_title.setPointSize(14)
        self.font_title.setBold(True)

    def _add_label(self):
        label_title = QLabel()
        label_title.setObjectName("ParametersTitle")
        label_title.setText("PARAMETERS")
        label_title.setStyleSheet(
            """border-top: 0px solid black; border-bottom: 2px solid black; padding: 8px"""
        )
        label_title.setFont(self.font_title)
        label_title.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        label_title.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.layout.addWidget(label_title, 0, 0, 1, 1)

    def _add_background(self):
        vline1 = QFrame()
        vline1.setFrameShape(QFrame.VLine)
        vline1.setFrameShadow(QFrame.Sunken)

        vline2 = QFrame()
        vline2.setFrameShape(QFrame.VLine)
        vline2.setFrameShadow(QFrame.Sunken)

        self.layout.addWidget(vline1, 1, 1, 1, 1)
        self.layout.addWidget(vline2, 1, 3, 1, 1)
