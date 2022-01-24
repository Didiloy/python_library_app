# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftPanel = QtWidgets.QWidget(self.centralwidget)
        self.leftPanel.setMinimumSize(QtCore.QSize(210, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.leftPanel.setFont(font)
        self.leftPanel.setStyleSheet("")
        self.leftPanel.setObjectName("leftPanel")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftPanel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frameLeftPanel = QtWidgets.QFrame(self.leftPanel)
        self.frameLeftPanel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLeftPanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLeftPanel.setObjectName("frameLeftPanel")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameLeftPanel)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.leftPanelButtonSearch = QtWidgets.QPushButton(self.frameLeftPanel)
        self.leftPanelButtonSearch.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.leftPanelButtonSearch.setFont(font)
        self.leftPanelButtonSearch.setObjectName("leftPanelButtonSearch")
        self.verticalLayout_2.addWidget(self.leftPanelButtonSearch)
        self.leftPanelButtonHome = QtWidgets.QPushButton(self.frameLeftPanel)
        self.leftPanelButtonHome.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.leftPanelButtonHome.setFont(font)
        self.leftPanelButtonHome.setObjectName("leftPanelButtonHome")
        self.verticalLayout_2.addWidget(self.leftPanelButtonHome)
        self.leftPanelButtonBibliotheque = QtWidgets.QPushButton(self.frameLeftPanel)
        self.leftPanelButtonBibliotheque.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.leftPanelButtonBibliotheque.setFont(font)
        self.leftPanelButtonBibliotheque.setObjectName("leftPanelButtonBibliotheque")
        self.verticalLayout_2.addWidget(self.leftPanelButtonBibliotheque)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frameLeftPanel)
        self.horizontalLayout.addWidget(self.leftPanel)
        self.centerPanel = QtWidgets.QVBoxLayout()
        self.centerPanel.setObjectName("centerPanel")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.searchWidget = QtWidgets.QWidget()
        self.searchWidget.setStyleSheet("")
        self.searchWidget.setObjectName("searchWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.searchWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayoutSearchWidget = QtWidgets.QGridLayout()
        self.gridLayoutSearchWidget.setObjectName("gridLayoutSearchWidget")
        self.gridLayoutSearchBar = QtWidgets.QGridLayout()
        self.gridLayoutSearchBar.setContentsMargins(-1, 20, -1, 20)
        self.gridLayoutSearchBar.setObjectName("gridLayoutSearchBar")
        self.searchButton = QtWidgets.QPushButton(self.searchWidget)
        self.searchButton.setObjectName("searchButton")
        self.gridLayoutSearchBar.addWidget(self.searchButton, 0, 3, 1, 1)
        self.searchLineEdit = QtWidgets.QLineEdit(self.searchWidget)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.gridLayoutSearchBar.addWidget(self.searchLineEdit, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutSearchBar.addItem(spacerItem2, 0, 0, 1, 1)
        self.searchLabel = QtWidgets.QLabel(self.searchWidget)
        self.searchLabel.setObjectName("searchLabel")
        self.gridLayoutSearchBar.addWidget(self.searchLabel, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutSearchBar.addItem(spacerItem3, 0, 4, 1, 1)
        self.gridLayoutSearchWidget.addLayout(self.gridLayoutSearchBar, 0, 0, 1, 1)
        self.scrollAreaSearch = QtWidgets.QScrollArea(self.searchWidget)
        self.scrollAreaSearch.setWidgetResizable(True)
        self.scrollAreaSearch.setObjectName("scrollAreaSearch")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 842, 587))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelRechercheEnCours = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRechercheEnCours.sizePolicy().hasHeightForWidth())
        self.labelRechercheEnCours.setSizePolicy(sizePolicy)
        self.labelRechercheEnCours.setMinimumSize(QtCore.QSize(300, 20))
        self.labelRechercheEnCours.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelRechercheEnCours.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelRechercheEnCours.setText("")
        self.labelRechercheEnCours.setObjectName("labelRechercheEnCours")
        self.verticalLayout_5.addWidget(self.labelRechercheEnCours, 0, QtCore.Qt.AlignHCenter)
        self.widgetScrollAreaSearchAnswer = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widgetScrollAreaSearchAnswer.setObjectName("widgetScrollAreaSearchAnswer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widgetScrollAreaSearchAnswer)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widgetWidgetScrollAreaSearchAnswer = QtWidgets.QWidget(self.widgetScrollAreaSearchAnswer)
        self.widgetWidgetScrollAreaSearchAnswer.setObjectName("widgetWidgetScrollAreaSearchAnswer")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widgetWidgetScrollAreaSearchAnswer)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_2.addWidget(self.widgetWidgetScrollAreaSearchAnswer, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.widgetScrollAreaSearchAnswer)
        self.scrollAreaSearch.setWidget(self.scrollAreaWidgetContents)
        self.gridLayoutSearchWidget.addWidget(self.scrollAreaSearch, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayoutSearchWidget)
        self.stackedWidget.addWidget(self.searchWidget)
        self.bookDetailWidget = QtWidgets.QWidget()
        self.bookDetailWidget.setObjectName("bookDetailWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.bookDetailWidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.bookDetailCoverWidget = QtWidgets.QWidget(self.bookDetailWidget)
        self.bookDetailCoverWidget.setObjectName("bookDetailCoverWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.bookDetailCoverWidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.bookDetailCoverLabel = QtWidgets.QLabel(self.bookDetailCoverWidget)
        self.bookDetailCoverLabel.setMinimumSize(QtCore.QSize(200, 260))
        self.bookDetailCoverLabel.setText("")
        self.bookDetailCoverLabel.setObjectName("bookDetailCoverLabel")
        self.verticalLayout_8.addWidget(self.bookDetailCoverLabel, 0, QtCore.Qt.AlignHCenter)
        self.bookDetailTitleLabel = QtWidgets.QLabel(self.bookDetailCoverWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bookDetailTitleLabel.setFont(font)
        self.bookDetailTitleLabel.setText("")
        self.bookDetailTitleLabel.setObjectName("bookDetailTitleLabel")
        self.verticalLayout_8.addWidget(self.bookDetailTitleLabel, 0, QtCore.Qt.AlignLeft)
        self.bookDetailAuthorLabel = QtWidgets.QLabel(self.bookDetailCoverWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bookDetailAuthorLabel.setFont(font)
        self.bookDetailAuthorLabel.setText("")
        self.bookDetailAuthorLabel.setObjectName("bookDetailAuthorLabel")
        self.verticalLayout_8.addWidget(self.bookDetailAuthorLabel)
        self.verticalLayout_7.addWidget(self.bookDetailCoverWidget)
        self.bookDetailDescriptionWidget = QtWidgets.QWidget(self.bookDetailWidget)
        self.bookDetailDescriptionWidget.setObjectName("bookDetailDescriptionWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.bookDetailDescriptionWidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.bookDetailDescriptionLabel = QtWidgets.QLabel(self.bookDetailDescriptionWidget)
        self.bookDetailDescriptionLabel.setText("")
        self.bookDetailDescriptionLabel.setWordWrap(True)
        self.bookDetailDescriptionLabel.setObjectName("bookDetailDescriptionLabel")
        self.verticalLayout_9.addWidget(self.bookDetailDescriptionLabel)
        self.bookDetaillRetourButton = QtWidgets.QPushButton(self.bookDetailDescriptionWidget)
        self.bookDetaillRetourButton.setObjectName("bookDetaillRetourButton")
        self.verticalLayout_9.addWidget(self.bookDetaillRetourButton)
        self.verticalLayout_7.addWidget(self.bookDetailDescriptionWidget)
        self.stackedWidget.addWidget(self.bookDetailWidget)
        self.homeWidget = QtWidgets.QWidget()
        self.homeWidget.setStyleSheet("")
        self.homeWidget.setObjectName("homeWidget")
        self.homeLabel = QtWidgets.QLabel(self.homeWidget)
        self.homeLabel.setGeometry(QtCore.QRect(380, 130, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.homeLabel.setFont(font)
        self.homeLabel.setStyleSheet("")
        self.homeLabel.setObjectName("homeLabel")
        self.stackedWidget.addWidget(self.homeWidget)
        self.bibliothequeWidget = QtWidgets.QWidget()
        self.bibliothequeWidget.setStyleSheet("")
        self.bibliothequeWidget.setObjectName("bibliothequeWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.bibliothequeWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bibliothequeLabel = QtWidgets.QLabel(self.bibliothequeWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.bibliothequeLabel.setFont(font)
        self.bibliothequeLabel.setStyleSheet("")
        self.bibliothequeLabel.setObjectName("bibliothequeLabel")
        self.verticalLayout_3.addWidget(self.bibliothequeLabel, 0, QtCore.Qt.AlignHCenter)
        self.scrollAreaBibliotheque = QtWidgets.QScrollArea(self.bibliothequeWidget)
        self.scrollAreaBibliotheque.setWidgetResizable(True)
        self.scrollAreaBibliotheque.setObjectName("scrollAreaBibliotheque")
        self.scrollAreaBibliothequeWidgetContent = QtWidgets.QWidget()
        self.scrollAreaBibliothequeWidgetContent.setGeometry(QtCore.QRect(0, 0, 66, 38))
        self.scrollAreaBibliothequeWidgetContent.setObjectName("scrollAreaBibliothequeWidgetContent")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaBibliothequeWidgetContent)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.scrollAreaBibliothequeWidgetContent)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        self.scrollAreaBibliotheque.setWidget(self.scrollAreaBibliothequeWidgetContent)
        self.verticalLayout_3.addWidget(self.scrollAreaBibliotheque)
        self.stackedWidget.addWidget(self.bibliothequeWidget)
        self.centerPanel.addWidget(self.stackedWidget)
        self.horizontalLayout.addLayout(self.centerPanel)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.leftPanelButtonSearch.setText(_translate("MainWindow", "Rechercher"))
        self.leftPanelButtonHome.setText(_translate("MainWindow", "Recommendations"))
        self.leftPanelButtonBibliotheque.setText(_translate("MainWindow", "Bibliothèque"))
        self.searchButton.setText(_translate("MainWindow", "Rechercher"))
        self.searchLineEdit.setPlaceholderText(_translate("MainWindow", "Tapez un nom de livre ici..."))
        self.searchLabel.setText(_translate("MainWindow", "Rechercher"))
        self.bookDetaillRetourButton.setText(_translate("MainWindow", "Retour"))
        self.homeLabel.setText(_translate("MainWindow", "HOME"))
        self.bibliothequeLabel.setText(_translate("MainWindow", "BIBLIOTHEQUE"))
