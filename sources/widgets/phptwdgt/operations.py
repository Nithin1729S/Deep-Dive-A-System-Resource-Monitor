from PyQt5.QtWidgets import QWidget

from sources.widgets.phptwdgt.interface import Ui_phptwdgt


class PhPtWdgt(QWidget, Ui_phptwdgt):
    def __init__(
        self,
        parent=None,
        phptdevc="Unavailable",
        phptfutl={
            "free": "000.00XB",
            "used": "000.00XB",
            "comp": "000.00XB",
            "perc": 0.0,
        },
        phptfsys={"mtpt": "Unavailable", "fsys": "Unavailable"},
    ):
        super(PhPtWdgt, self).__init__(parent)
        self.setupUi(self)
        self.handle_elements(phptdevc, phptfutl, phptfsys)

    def handle_elements(self, phptdevc, phptfutl, phptfsys):
        self.phptdvce.setText(str(phptdevc))
        self.phptfrtx.setText(phptfutl["free"])
        self.phptustx.setText(phptfutl["used"])
        self.phptsmtx.setText(phptfutl["comp"])
        self.phptpgbr.setValue(int(phptfutl["perc"]))
        self.phptfsys.setText("<b>%s</b> (%s)" % (phptfsys["mtpt"], phptfsys["fsys"]))

    def modify_attributes(self, phptdevc, phptfutl, phptfsys):
        self.phptfrtx.setText(phptfutl["free"])
        self.phptustx.setText(phptfutl["used"])
        self.phptsmtx.setText(phptfutl["comp"])
        self.phptpgbr.setValue(int(phptfutl["perc"]))
        self.phptfsys.setText("<b>%s</b> (%s)" % (phptfsys["mtpt"], phptfsys["fsys"]))
