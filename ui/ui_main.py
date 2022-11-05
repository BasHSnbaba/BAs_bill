# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(689, 761)
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_nowTime = QLabel(Form)
        self.label_nowTime.setObjectName(u"label_nowTime")
        self.label_nowTime.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_nowTime)

        self.nowTime = QLabel(Form)
        self.nowTime.setObjectName(u"nowTime")
        self.nowTime.setTextFormat(Qt.AutoText)
        self.nowTime.setMargin(0)

        self.horizontalLayout.addWidget(self.nowTime)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_setting = QPushButton(Form)
        self.pushButton_setting.setObjectName(u"pushButton_setting")

        self.horizontalLayout.addWidget(self.pushButton_setting)

        self.pushButton_ex = QPushButton(Form)
        self.pushButton_ex.setObjectName(u"pushButton_ex")

        self.horizontalLayout.addWidget(self.pushButton_ex)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.groupBox_main = QGroupBox(Form)
        self.groupBox_main.setObjectName(u"groupBox_main")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_main)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_timeID = QVBoxLayout()
        self.verticalLayout_timeID.setObjectName(u"verticalLayout_timeID")
        self.tableWidget = QTableWidget(self.groupBox_main)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget.rowCount() < 200):
            self.tableWidget.setRowCount(200)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(200)

        self.verticalLayout_timeID.addWidget(self.tableWidget)

        self.horizontalLayout_timeID = QHBoxLayout()
        self.horizontalLayout_timeID.setObjectName(u"horizontalLayout_timeID")
        self.label_timeID = QLabel(self.groupBox_main)
        self.label_timeID.setObjectName(u"label_timeID")

        self.horizontalLayout_timeID.addWidget(self.label_timeID)

        self.lineEdit_timeID = QLineEdit(self.groupBox_main)
        self.lineEdit_timeID.setObjectName(u"lineEdit_timeID")

        self.horizontalLayout_timeID.addWidget(self.lineEdit_timeID)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_timeID.addItem(self.horizontalSpacer_2)

        self.pushButton_timeIDadd = QPushButton(self.groupBox_main)
        self.pushButton_timeIDadd.setObjectName(u"pushButton_timeIDadd")

        self.horizontalLayout_timeID.addWidget(self.pushButton_timeIDadd)

        self.pushButton_timeIDstop = QPushButton(self.groupBox_main)
        self.pushButton_timeIDstop.setObjectName(u"pushButton_timeIDstop")

        self.horizontalLayout_timeID.addWidget(self.pushButton_timeIDstop)

        self.pushButton_timeIDdel = QPushButton(self.groupBox_main)
        self.pushButton_timeIDdel.setObjectName(u"pushButton_timeIDdel")

        self.horizontalLayout_timeID.addWidget(self.pushButton_timeIDdel)


        self.verticalLayout_timeID.addLayout(self.horizontalLayout_timeID)

        self.groupBox = QGroupBox(self.groupBox_main)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.comboBox_c = QComboBox(self.groupBox)
        self.comboBox_c.addItem("")
        self.comboBox_c.addItem("")
        self.comboBox_c.addItem("")
        self.comboBox_c.addItem("")
        self.comboBox_c.setObjectName(u"comboBox_c")

        self.horizontalLayout_2.addWidget(self.comboBox_c)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_p = QLineEdit(self.groupBox)
        self.lineEdit_p.setObjectName(u"lineEdit_p")

        self.horizontalLayout_2.addWidget(self.lineEdit_p)

        self.pushButton_addItem = QPushButton(self.groupBox)
        self.pushButton_addItem.setObjectName(u"pushButton_addItem")

        self.horizontalLayout_2.addWidget(self.pushButton_addItem)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 2)
        self.horizontalLayout_2.setStretch(4, 2)

        self.verticalLayout_timeID.addWidget(self.groupBox)


        self.horizontalLayout_8.addLayout(self.verticalLayout_timeID)

        self.horizontalLayout_8.setStretch(0, 7)

        self.verticalLayout_5.addWidget(self.groupBox_main)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 20)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8d26\u5355\u7ba1\u7406\u7cfb\u7edf", None))
        self.label_nowTime.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u65f6\u95f4:", None))
        self.nowTime.setText("")
        self.pushButton_setting.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.pushButton_ex.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa\u8d26\u5355", None))
        self.groupBox_main.setTitle(QCoreApplication.translate("Form", u"\u64cd\u4f5c\u9762\u677f", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u9879\u76eeid", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u9879\u76ee\u7c7b\u522b", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u9879\u76ee\u5b9e\u4f53id", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u65f6\u95f4", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u7ed3\u675f\u65f6\u95f4", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u91d1\u989d", None));
        self.label_timeID.setText(QCoreApplication.translate("Form", u"\u8bf7\u5148\u8f93\u5165\u5b9e\u4f53\u9879\u76ee\u7f16\u53f7:", None))
        self.pushButton_timeIDadd.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u8ba1\u65f6\u9879\u76ee", None))
        self.pushButton_timeIDstop.setText(QCoreApplication.translate("Form", u"\u7ed3\u675f\u8ba1\u65f6\u9879\u76ee", None))
        self.pushButton_timeIDdel.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u8ba1\u65f6\u9879\u76ee", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u5546\u54c1\u6dfb\u52a0", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5546\u54c1\u7c7b\u522b:", None))
        self.comboBox_c.setItemText(0, QCoreApplication.translate("Form", u"\u6e9c\u51b0", None))
        self.comboBox_c.setItemText(1, QCoreApplication.translate("Form", u"\u996e\u6599", None))
        self.comboBox_c.setItemText(2, QCoreApplication.translate("Form", u"\u98df\u7269", None))
        self.comboBox_c.setItemText(3, QCoreApplication.translate("Form", u"\u6742\u9879", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"\u5546\u54c1\u4ef7\u683c:", None))
        self.pushButton_addItem.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u5546\u54c1", None))
    # retranslateUi

