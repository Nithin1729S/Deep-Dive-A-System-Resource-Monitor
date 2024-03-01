from PyQt5.QtWidgets import QWidget

from sources.widgets.lgptwdgt.interface import Ui_lgptwdgt


class LgPtWdgt(QWidget, Ui_lgptwdgt):
    def __init__(
        self,
        parent=None,
        lgptdevc="Unavailable",
        lgptfutl={
            "free": "000.00XB",
            "used": "000.00XB",
            "comp": "000.00XB",
            "perc": 0.0,
        },
        lgptfsys={"mtpt": "Unavailable", "fsys": "Unavailable"},
    ):
        super(LgPtWdgt, self).__init__(parent)
        self.setupUi(self)
        self.handle_elements(lgptdevc, lgptfutl, lgptfsys)

    def handle_elements(self, lgptdevc, lgptfutl, lgptfsys):
        self.lgptdvce.setText(str(lgptdevc))
        self.lgptfrtx.setText(lgptfutl["free"])
        self.lgptustx.setText(lgptfutl["used"])
        self.lgptsmtx.setText(lgptfutl["comp"])
        self.lgptpgbr.setValue(int(lgptfutl["perc"]))
        self.lgptfsys.setText("<b>%s</b> (%s)" % (lgptfsys["mtpt"], lgptfsys["fsys"]))

    def modify_attributes(self, lgptdevc, lgptfutl, lgptfsys):
        self.lgptfrtx.setText(lgptfutl["free"])
        self.lgptustx.setText(lgptfutl["used"])
        self.lgptsmtx.setText(lgptfutl["comp"])
        self.lgptpgbr.setValue(int(lgptfutl["perc"]))
        self.lgptfsys.setText("<b>%s</b> (%s)" % (lgptfsys["mtpt"], lgptfsys["fsys"]))
