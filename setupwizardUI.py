# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setupwizardUI.ui'
#
# Created: Fri May 22 02:40:47 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_SetupWizard(object):
    def setupUi(self, SetupWizard):
        SetupWizard.setObjectName(_fromUtf8("SetupWizard"))
        SetupWizard.resize(554, 519)
        SetupWizard.setWizardStyle(QtGui.QWizard.ModernStyle)
        self.wizardPage1 = CustomQWizardPage()
        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.wizardPage1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.wizardPage1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        SetupWizard.addPage(self.wizardPage1)
        self.wizardPage2 = CustomQWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.wizardPage2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.wizardPage2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.wizardPage2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.wizardPage2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.wizardPage2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.operating_system = QtGui.QLabel(self.wizardPage2)
        self.operating_system.setObjectName(_fromUtf8("operating_system"))
        self.gridLayout.addWidget(self.operating_system, 0, 1, 1, 1)
        self.standard_path = QtGui.QLabel(self.wizardPage2)
        self.standard_path.setObjectName(_fromUtf8("standard_path"))
        self.gridLayout.addWidget(self.standard_path, 3, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.wizardPage2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.wizardPage2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.custom_path = QtGui.QLabel(self.wizardPage2)
        self.custom_path.setObjectName(_fromUtf8("custom_path"))
        self.gridLayout.addWidget(self.custom_path, 4, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.path_input = QtGui.QLineEdit(self.wizardPage2)
        self.path_input.setObjectName(_fromUtf8("path_input"))
        self.horizontalLayout.addWidget(self.path_input)
        self.browse_log_path = QtGui.QPushButton(self.wizardPage2)
        self.browse_log_path.setObjectName(_fromUtf8("browse_log_path"))
        self.horizontalLayout.addWidget(self.browse_log_path)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_6 = QtGui.QLabel(self.wizardPage2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_8.addWidget(self.label_6)
        self.valid_path = QtGui.QLabel(self.wizardPage2)
        self.valid_path.setObjectName(_fromUtf8("valid_path"))
        self.horizontalLayout_8.addWidget(self.valid_path)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        SetupWizard.addPage(self.wizardPage2)
        self.wizardPage3 = CustomQWizardPage()
        self.wizardPage3.setObjectName(_fromUtf8("wizardPage3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.wizardPage3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_11 = QtGui.QLabel(self.wizardPage3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_3.addWidget(self.label_11)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_12 = QtGui.QLabel(self.wizardPage3)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_2.addWidget(self.label_12)
        self.appconf_found = QtGui.QLabel(self.wizardPage3)
        self.appconf_found.setObjectName(_fromUtf8("appconf_found"))
        self.horizontalLayout_2.addWidget(self.appconf_found)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_14 = QtGui.QLabel(self.wizardPage3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_3.addWidget(self.label_14)
        self.verbose_enabled = QtGui.QLabel(self.wizardPage3)
        self.verbose_enabled.setObjectName(_fromUtf8("verbose_enabled"))
        self.horizontalLayout_3.addWidget(self.verbose_enabled)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verbose_button = QtGui.QPushButton(self.wizardPage3)
        self.verbose_button.setEnabled(False)
        self.verbose_button.setObjectName(_fromUtf8("verbose_button"))
        self.horizontalLayout_4.addWidget(self.verbose_button)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.label_16 = QtGui.QLabel(self.wizardPage3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setTextFormat(QtCore.Qt.RichText)
        self.label_16.setWordWrap(True)
        self.label_16.setOpenExternalLinks(True)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_3.addWidget(self.label_16)
        SetupWizard.addPage(self.wizardPage3)
        self.wizardPage4 = CustomQWizardPage()
        self.wizardPage4.setObjectName(_fromUtf8("wizardPage4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.wizardPage4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_17 = QtGui.QLabel(self.wizardPage4)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_4.addWidget(self.label_17)
        self.label_18 = QtGui.QLabel(self.wizardPage4)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_4.addWidget(self.label_18)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.screenshot_dir = QtGui.QLineEdit(self.wizardPage4)
        self.screenshot_dir.setObjectName(_fromUtf8("screenshot_dir"))
        self.horizontalLayout_5.addWidget(self.screenshot_dir)
        self.screenshot_dir_browse = QtGui.QPushButton(self.wizardPage4)
        self.screenshot_dir_browse.setObjectName(_fromUtf8("screenshot_dir_browse"))
        self.horizontalLayout_5.addWidget(self.screenshot_dir_browse)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.label_19 = QtGui.QLabel(self.wizardPage4)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_4.addWidget(self.label_19)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.export_dir = QtGui.QLineEdit(self.wizardPage4)
        self.export_dir.setObjectName(_fromUtf8("export_dir"))
        self.horizontalLayout_6.addWidget(self.export_dir)
        self.export_dir_browse = QtGui.QPushButton(self.wizardPage4)
        self.export_dir_browse.setObjectName(_fromUtf8("export_dir_browse"))
        self.horizontalLayout_6.addWidget(self.export_dir_browse)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        SetupWizard.addPage(self.wizardPage4)
        self.wizardPage5 = CustomQWizardPage()
        self.wizardPage5.setObjectName(_fromUtf8("wizardPage5"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.wizardPage5)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_23 = QtGui.QLabel(self.wizardPage5)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.verticalLayout_7.addWidget(self.label_23)
        self.summary = QtGui.QLabel(self.wizardPage5)
        self.summary.setText(_fromUtf8(""))
        self.summary.setWordWrap(True)
        self.summary.setObjectName(_fromUtf8("summary"))
        self.verticalLayout_7.addWidget(self.summary)
        SetupWizard.addPage(self.wizardPage5)

        self.retranslateUi(SetupWizard)
        QtCore.QMetaObject.connectSlotsByName(SetupWizard)

    def retranslateUi(self, SetupWizard):
        SetupWizard.setWindowTitle(_translate("SetupWizard", "EliteOCR Wizard", None))
        self.wizardPage1.setTitle(_translate("SetupWizard", "Setup Wizard", None))
        self.wizardPage1.setSubTitle(_translate("SetupWizard", "This wizard will help you set up EliteOCR to work properly with your Elite: Dangerous installation and market screenshots.", None))
        self.label.setText(_translate("SetupWizard", "Welcome to EliteOCR.\n"
"\n"
"This wizard will help with the following tasks:\n"
"- Set the log directory path for automatic system and station name retrieval\n"
"- Enable verbose logging in the games configuration\n"
"- Set the screenshot directory path for fast selection of files\n"
"- Set the export directory path\n"
"\n"
"Please read all the instructions very carefully. You can run this wizard at any time from the settings menu.", None))
        self.wizardPage2.setTitle(_translate("SetupWizard", "Setup Wizard", None))
        self.wizardPage2.setSubTitle(_translate("SetupWizard", "Log Path Setup", None))
        self.label_2.setText(_translate("SetupWizard", "In this step EliteOCR tries to find the location of your games log directory. If the path cannot be found automatically (e.g. network share) you can choose it manually. If you don\'t set this path EliteOCR will not be able to find the system name and you will need to fill it automatically.", None))
        self.label_3.setText(_translate("SetupWizard", "Location", None))
        self.label_4.setText(_translate("SetupWizard", "Found", None))
        self.label_5.setText(_translate("SetupWizard", "Standard Path", None))
        self.operating_system.setText(_translate("SetupWizard", "-", None))
        self.standard_path.setText(_translate("SetupWizard", "-", None))
        self.label_7.setText(_translate("SetupWizard", "Operating system:", None))
        self.label_9.setText(_translate("SetupWizard", "Custom Install Path", None))
        self.custom_path.setText(_translate("SetupWizard", "-", None))
        self.browse_log_path.setText(_translate("SetupWizard", "Choose location", None))
        self.label_6.setText(_translate("SetupWizard", "Valid path selected:", None))
        self.valid_path.setText(_translate("SetupWizard", "-", None))
        self.wizardPage3.setTitle(_translate("SetupWizard", "Setup Wizard", None))
        self.wizardPage3.setSubTitle(_translate("SetupWizard", "Verbose Logging", None))
        self.label_11.setText(_translate("SetupWizard", "In order to automatically receive system and station names it is necessary to enable verbose logging in games settings files.", None))
        self.label_12.setText(_translate("SetupWizard", "AppConfig.xml", None))
        self.appconf_found.setText(_translate("SetupWizard", "-", None))
        self.label_14.setText(_translate("SetupWizard", "Verbose Logging", None))
        self.verbose_enabled.setText(_translate("SetupWizard", "-", None))
        self.verbose_button.setText(_translate("SetupWizard", "Enable Verbose Logging", None))
        self.label_16.setText(_translate("SetupWizard", "<html><head/><body><p>After enabling verbose logging in ED <span style=\" font-weight:600; text-decoration: underline;\">restart the game</span> and make some good market screenshots for calibration. You make the screenshots by pressing F10 in the game. DO NOT use ALT+F10.<br/><br/>Exaple of a <a href=\"http://i.imgur.com/n2UPagt.jpg\"><span style=\" text-decoration: underline; color:#0000ff;\">good screenshot</span></a> and an exaple of a <a href=\"http://i.imgur.com/MZTmTON.jpg\"><span style=\" text-decoration: underline; color:#0000ff;\">bad screenshot</span></a>.<br/><br/>Please note the selected line and the glow on the top of the market frame. You have to make sure they are not present on your screenshots. You can achieve this by moving the mouse to the right on the field with commodity description or by pressing right on your jostick/gamepad until this field is selected.</p><p>(You can keep this wizard open while you make the screenshots.)</p></body></html>", None))
        self.wizardPage4.setTitle(_translate("SetupWizard", "Setup Wizard", None))
        self.wizardPage4.setSubTitle(_translate("SetupWizard", "Screenshot and Export paths", None))
        self.label_17.setText(_translate("SetupWizard", "In this step you choose where EliteOCR should look for screenshots and where you want it to export your results.", None))
        self.label_18.setText(_translate("SetupWizard", "Screenshot directory:", None))
        self.screenshot_dir_browse.setText(_translate("SetupWizard", "Browse", None))
        self.label_19.setText(_translate("SetupWizard", "Export directory:", None))
        self.export_dir_browse.setText(_translate("SetupWizard", "Browse", None))
        self.wizardPage5.setTitle(_translate("SetupWizard", "Setup Wizard", None))
        self.wizardPage5.setSubTitle(_translate("SetupWizard", "Results", None))
        self.label_23.setText(_translate("SetupWizard", "Setup Wizard finished with following results:", None))

from customqwizardpage import CustomQWizardPage
