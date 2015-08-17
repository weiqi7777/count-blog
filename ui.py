# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jiemian.ui'
#
# Created: Fri Aug 14 12:18:28 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from excel_generate import *
from seek_file import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setEnabled(True)
        Form.resize(837, 713)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 70, 61, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 70, 261, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(460, 70, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(610, 110, 160, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout.addWidget(self.radioButton_2)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 150, 48, 78))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 180, 161, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(100, 320, 471, 192))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(5)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 250, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 540, 371, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(140, 590, 31, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_4 = QtGui.QLineEdit(Form)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 590, 371, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 530, 31, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        #for i in range(5):
            #item = QtGui.QTableWidgetItem()
            #self.tableWidget.setItem(i,0,item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(500)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),Form.tongji)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL(_fromUtf8("cellClicked(int,int)")), Form.cellclicked)   
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.excel_gen)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "博客目录", None))
        self.pushButton.setText(_translate("Form", "浏览", None))
        self.radioButton.setText(_translate("Form", ".pdf", None))
        self.radioButton_2.setText(_translate("Form", ".docx", None))
        self.label_2.setText(_translate("Form", "博文总数", None))     
        self.pushButton_2.setText(_translate("Form", "生成excel", None))
        self.label_4.setText(_translate("Form", "目录", None))
        self.label_3.setText(_translate("Form", "博文", None)) 
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "文章", None))
        #stem.setTextAlignment()

        #for i in range(5):
            #item = self.tableWidget.item(i,0)
            #item.setText(_translate("Form", str(i), None))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def cellclicked(self,row,col):
        #print(row+1,col+1)
        item = self.tableWidget.item(row,col)
        file_name = item.text()
        try:
            dic = self.file_dict[file_name]
            self.lineEdit_3.setText(file_name)
            self.lineEdit_4.setText(dic)
        except:
            print('error')
    
    def tongji(self):
        directory = diropenbox('','请选择一个目录',default='G:\\博客文章')
        if self.radioButton.isChecked():
            leixing = '.pdf'
        else:
            leixing = '.docx'
        #print(leixing)
        self.file_dict = dict_file(directory,leixing)
        self.file_list = list_file(directory,leixing)
        #print(file_list)
        number = len(self.file_list)
        self.lineEdit.setText(directory)
        self.lineEdit_2.setText(str(number))
        self.tableWidget.setRowCount(number)
        for i in range(number):
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(i,0,item)
        for i in range(number):
            item = self.tableWidget.item(i,0)
            item.setText(_translate("Form", self.file_list[i], None))
        self.pushButton_2.setEnabled(True)

    def excel_gen(self):
        #print('excel gen')
        excel_generate(self.file_list,self.file_dict,'.pdf')
