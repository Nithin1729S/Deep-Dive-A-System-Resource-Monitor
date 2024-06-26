from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_phptwdgt(object):
    def setupUi(self, phptwdgt):
        phptwdgt.setObjectName("phptwdgt")
        phptwdgt.resize(340, 115)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(phptwdgt.sizePolicy().hasHeightForWidth())
        phptwdgt.setSizePolicy(sizePolicy)
        phptwdgt.setMinimumSize(QtCore.QSize(340, 115))
        phptwdgt.setMaximumSize(QtCore.QSize(340, 115))
        self.phptfsys = QtWidgets.QLabel(phptwdgt)
        self.phptfsys.setGeometry(QtCore.QRect(5, 35, 330, 15))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phptfsys.sizePolicy().hasHeightForWidth())
        self.phptfsys.setSizePolicy(sizePolicy)
        self.phptfsys.setMinimumSize(QtCore.QSize(330, 15))
        self.phptfsys.setMaximumSize(QtCore.QSize(330, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.phptfsys.setFont(font)
        self.phptfsys.setStyleSheet('font: 10pt "Inter"; border: none;')
        self.phptfsys.setObjectName("phptfsys")
        self.phptfrlb = QtWidgets.QLabel(phptwdgt)
        self.phptfrlb.setGeometry(QtCore.QRect(5, 75, 110, 15))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phptfrlb.sizePolicy().hasHeightForWidth())
        self.phptfrlb.setSizePolicy(sizePolicy)
        self.phptfrlb.setMinimumSize(QtCore.QSize(110, 15))
        self.phptfrlb.setMaximumSize(QtCore.QSize(110, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.phptfrlb.setFont(font)
        self.phptfrlb.setStyleSheet('font: 600 10pt "Inter"; border: none;')
        self.phptfrlb.setObjectName("phptfrlb")
        self.phptpgbr = QtWidgets.QProgressBar(phptwdgt)
        self.phptpgbr.setGeometry(QtCore.QRect(5, 55, 330, 15))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phptpgbr.sizePolicy().hasHeightForWidth())
        self.phptpgbr.setSizePolicy(sizePolicy)
        self.phptpgbr.setMinimumSize(QtCore.QSize(330, 15))
        self.phptpgbr.setMaximumSize(QtCore.QSize(330, 15))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        self.phptpgbr.setFont(font)
        self.phptpgbr.setStyleSheet(
            'border: 1px solid #808080; border-radius: 0px; font: 8pt "Inter";'
        )
        self.phptpgbr.setProperty("value", 0)
        self.phptpgbr.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.phptpgbr.setTextVisible(True)
        self.phptpgbr.setInvertedAppearance(False)
        self.phptpgbr.setObjectName("phptpgbr")
        self.unitfrme = QtWidgets.QFrame(phptwdgt)
        self.unitfrme.setGeometry(QtCore.QRect(0, 0, 340, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unitfrme.sizePolicy().hasHeightForWidth())
        self.unitfrme.setSizePolicy(sizePolicy)
        self.unitfrme.setMinimumSize(QtCore.QSize(340, 30))
        self.unitfrme.setMaximumSize(QtCore.QSize(340, 30))
        self.unitfrme.setStyleSheet("background-color: rgba(128, 128, 128, 0.5); border: none;")
        self.unitfrme.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.unitfrme.setFrameShadow(QtWidgets.QFrame.Raised)
        self.unitfrme.setObjectName("unitfrme")
        self.phptdvce = QtWidgets.QLabel(self.unitfrme)
        self.phptdvce.setGeometry(QtCore.QRect(5, 5, 305, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phptdvce.sizePolicy().hasHeightForWidth())
        self.phptdvce.setSizePolicy(sizePolicy)
        self.phptdvce.setMinimumSize(QtCore.QSize(305, 20))
        self.phptdvce.setMaximumSize(QtCore.QSize(305, 20))
        self.phptdvce.setStyleSheet('font: 13pt "Barlow"; border: none; background: transparent;')
        self.phptdvce.setObjectName("phptdvce")
        self.phpticon = QtWidgets.QLabel(self.unitfrme)
        self.phpticon.setGeometry(QtCore.QRect(315, 5, 20, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phpticon.sizePolicy().hasHeightForWidth())
        self.phpticon.setSizePolicy(sizePolicy)
        self.phpticon.setMinimumSize(QtCore.QSize(20, 20))
        self.phpticon.setMaximumSize(QtCore.QSize(20, 20))
        self.phpticon.setStyleSheet(
            'font: 13pt "Font Awesome 5 Free"; border: none; background: transparent;'
        )
        self.phpticon.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.phpticon.setObjectName("phpticon")
        self.phptfrtx = QtWidgets.QLabel(phptwdgt)
        self.phptfrtx.setGeometry(QtCore.QRect(5, 90, 110, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phptfrtx.sizePolicy().hasHeightForWidth())
        self.phptfrtx.setSizePolicy(sizePolicy)
        self.phptfrtx.setMinimumSize(QtCore.QSize(110, 20))
        self.phptfrtx.setMaximumSize(QtCore.QSize(110, 20))
        self.phptfrtx.setStyleSheet('font: 13pt "Barlow"; border: none; background: transparent;')
        self.phptfrtx.setObjectName("phptfrtx")
        self.phptustx = QtWidgets.QLabel(phptwdgt)
        self.phptustx.setGeometry(QtCore.QRect(115, 90, 110, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phptustx.sizePolicy().hasHeightForWidth())
        self.phptustx.setSizePolicy(sizePolicy)
        self.phptustx.setMinimumSize(QtCore.QSize(110, 20))
        self.phptustx.setMaximumSize(QtCore.QSize(110, 20))
        self.phptustx.setStyleSheet('font: 13pt "Barlow"; border: none; background: transparent;')
        self.phptustx.setObjectName("phptustx")
        self.phptuslb = QtWidgets.QLabel(phptwdgt)
        self.phptuslb.setGeometry(QtCore.QRect(115, 75, 110, 15))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phptuslb.sizePolicy().hasHeightForWidth())
        self.phptuslb.setSizePolicy(sizePolicy)
        self.phptuslb.setMinimumSize(QtCore.QSize(110, 15))
        self.phptuslb.setMaximumSize(QtCore.QSize(110, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.phptuslb.setFont(font)
        self.phptuslb.setStyleSheet('font: 600 10pt "Inter"; border: none;')
        self.phptuslb.setObjectName("phptuslb")
        self.phptsmtx = QtWidgets.QLabel(phptwdgt)
        self.phptsmtx.setGeometry(QtCore.QRect(225, 90, 110, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phptsmtx.sizePolicy().hasHeightForWidth())
        self.phptsmtx.setSizePolicy(sizePolicy)
        self.phptsmtx.setMinimumSize(QtCore.QSize(110, 20))
        self.phptsmtx.setMaximumSize(QtCore.QSize(110, 20))
        self.phptsmtx.setStyleSheet('font: 13pt "Barlow"; border: none; background: transparent;')
        self.phptsmtx.setObjectName("phptsmtx")
        self.phptsmlb = QtWidgets.QLabel(phptwdgt)
        self.phptsmlb.setGeometry(QtCore.QRect(225, 75, 110, 15))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phptsmlb.sizePolicy().hasHeightForWidth())
        self.phptsmlb.setSizePolicy(sizePolicy)
        self.phptsmlb.setMinimumSize(QtCore.QSize(110, 15))
        self.phptsmlb.setMaximumSize(QtCore.QSize(110, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.phptsmlb.setFont(font)
        self.phptsmlb.setStyleSheet('font: 600 10pt "Inter"; border: none;')
        self.phptsmlb.setObjectName("phptsmlb")

        self.retranslateUi(phptwdgt)
        QtCore.QMetaObject.connectSlotsByName(phptwdgt)

    def retranslateUi(self, phptwdgt):
        _translate = QtCore.QCoreApplication.translate
        phptwdgt.setWindowTitle(_translate("phptwdgt", "Form"))
        self.phptfsys.setText(_translate("phptwdgt", "MOUNTPOINT (FILESYSTEM)"))
        self.phptfrlb.setText(_translate("phptwdgt", "FREE"))
        self.phptpgbr.setFormat(_translate("phptwdgt", "%p% "))
        self.phptdvce.setText(_translate("phptwdgt", "DEVICE"))
        self.phpticon.setText(_translate("phptwdgt", "compact-disc"))
        self.phptfrtx.setText(_translate("phptwdgt", "000.00XB"))
        self.phptustx.setText(_translate("phptwdgt", "000.00XB"))
        self.phptuslb.setText(_translate("phptwdgt", "USED"))
        self.phptsmtx.setText(_translate("phptwdgt", "000.00XB"))
        self.phptsmlb.setText(_translate("phptwdgt", "TOTAL"))
