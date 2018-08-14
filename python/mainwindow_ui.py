# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(872, 311)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.note1 = QtWidgets.QPushButton(self.centralWidget)
        self.note1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.note1.sizePolicy().hasHeightForWidth())
        self.note1.setSizePolicy(sizePolicy)
        self.note1.setObjectName("note1")
        self.verticalLayout_2.addWidget(self.note1)
        self.note2 = QtWidgets.QPushButton(self.centralWidget)
        self.note2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.note2.sizePolicy().hasHeightForWidth())
        self.note2.setSizePolicy(sizePolicy)
        self.note2.setObjectName("note2")
        self.verticalLayout_2.addWidget(self.note2)
        self.note3 = QtWidgets.QPushButton(self.centralWidget)
        self.note3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.note3.sizePolicy().hasHeightForWidth())
        self.note3.setSizePolicy(sizePolicy)
        self.note3.setObjectName("note3")
        self.verticalLayout_2.addWidget(self.note3)
        self.random_note = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.random_note.sizePolicy().hasHeightForWidth())
        self.random_note.setSizePolicy(sizePolicy)
        self.random_note.setObjectName("random_note")
        self.verticalLayout_2.addWidget(self.random_note)
        self.custom_note = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.custom_note.sizePolicy().hasHeightForWidth())
        self.custom_note.setSizePolicy(sizePolicy)
        self.custom_note.setInputMask("")
        self.custom_note.setObjectName("custom_note")
        self.verticalLayout_2.addWidget(self.custom_note)
        self.custom_btn = QtWidgets.QPushButton(self.centralWidget)
        self.custom_btn.setObjectName("custom_btn")
        self.verticalLayout_2.addWidget(self.custom_btn)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.track = QtWidgets.QVBoxLayout()
        self.track.setSpacing(6)
        self.track.setObjectName("track")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.track.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.track.addItem(spacerItem)
        self.verticalLayout.addLayout(self.track)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_3.addWidget(self.playButton)
        self.pauseButton = QtWidgets.QPushButton(self.centralWidget)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_3.addWidget(self.pauseButton)
        self.timeSlider = QtWidgets.QSlider(self.centralWidget)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.horizontalLayout_3.addWidget(self.timeSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.add_track_btn = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_track_btn.sizePolicy().hasHeightForWidth())
        self.add_track_btn.setSizePolicy(sizePolicy)
        self.add_track_btn.setObjectName("add_track_btn")
        self.verticalLayout.addWidget(self.add_track_btn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 872, 22))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setObjectName("menuBar")
        self.menuMirror = QtWidgets.QMenu(self.menuBar)
        self.menuMirror.setObjectName("menuMirror")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOptions = QtWidgets.QAction(MainWindow)
        self.actionOptions.setObjectName("actionOptions")
        self.menuMirror.addAction(self.actionOptions)
        self.menuBar.addAction(self.menuMirror.menuAction())

        self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.note1.setText(_translate("MainWindow", "Possible Note 1"))
        self.note2.setText(_translate("MainWindow", "Possible Note 2"))
        self.note3.setText(_translate("MainWindow", "Possible Note 3"))
        self.random_note.setText(_translate("MainWindow", "Random Note"))
        self.custom_note.setText(_translate("MainWindow", "Custom"))
        self.custom_btn.setText(_translate("MainWindow", "Add Custom Note"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.add_track_btn.setText(_translate("MainWindow", "Add Track"))
        self.menuMirror.setTitle(_translate("MainWindow", "Mirror"))
        self.actionOptions.setText(_translate("MainWindow", "options"))

