# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ccav.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
import os
import wmi

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(851, 834)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 841, 811))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.IPAdress_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.IPAdress_1.setObjectName("IPAdress_1")
        self.verticalLayout_2.addWidget(self.IPAdress_1)
        self.arrSubnetMasks_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.arrSubnetMasks_1.setObjectName("arrSubnetMasks_1")
        self.verticalLayout_2.addWidget(self.arrSubnetMasks_1)
        self.arrDefaultGateways_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.arrDefaultGateways_1.setObjectName("arrDefaultGateways_1")
        self.verticalLayout_2.addWidget(self.arrDefaultGateways_1)
        self.arrDNSServers_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.arrDNSServers_1.setObjectName("arrDNSServers_1")
        self.verticalLayout_2.addWidget(self.arrDNSServers_1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_10.addWidget(self.line)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.IPAdress_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.IPAdress_2.setObjectName("IPAdress_2")
        self.verticalLayout_6.addWidget(self.IPAdress_2)
        self.arrSubnetMasks_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.arrSubnetMasks_2.setObjectName("arrSubnetMasks_2")
        self.verticalLayout_6.addWidget(self.arrSubnetMasks_2)
        self.arrDefaultGateways_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.arrDefaultGateways_2.setObjectName("arrDefaultGateways_2")
        self.verticalLayout_6.addWidget(self.arrDefaultGateways_2)
        self.arrDNSServers_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.arrDNSServers_2.setObjectName("arrDNSServers_2")
        self.verticalLayout_6.addWidget(self.arrDNSServers_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_10.addWidget(self.line_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.IPAdress_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.IPAdress_3.setObjectName("IPAdress_3")
        self.verticalLayout_9.addWidget(self.IPAdress_3)
        self.arrSubnetMasks_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.arrSubnetMasks_3.setObjectName("arrSubnetMasks_3")
        self.verticalLayout_9.addWidget(self.arrSubnetMasks_3)
        self.arrDefaultGateways_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.arrDefaultGateways_3.setObjectName("arrDefaultGateways_3")
        self.verticalLayout_9.addWidget(self.arrDefaultGateways_3)
        self.arrDNSServers_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.arrDNSServers_3.setObjectName("arrDNSServers_3")
        self.verticalLayout_9.addWidget(self.arrDNSServers_3)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked['bool'].connect(self.set_first)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "arrIPAddresses "))
        self.label_2.setText(_translate("MainWindow", "arrSubnetMasks"))
        self.label_3.setText(_translate("MainWindow", "arrDefaultGateways"))
        self.label_4.setText(_translate("MainWindow", "arrDNSServers"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label_5.setText(_translate("MainWindow", "arrIPAddresses "))
        self.label_6.setText(_translate("MainWindow", "arrSubnetMasks"))
        self.label_7.setText(_translate("MainWindow", "arrDefaultGateways"))
        self.label_8.setText(_translate("MainWindow", "arrDNSServers"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.label_9.setText(_translate("MainWindow", "arrIPAddresses "))
        self.label_10.setText(_translate("MainWindow", "arrSubnetMasks"))
        self.label_11.setText(_translate("MainWindow", "arrDefaultGateways"))
        self.label_12.setText(_translate("MainWindow", "arrDNSServers"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))

        filename = 'ccav.txt'  # txt文件和当前脚本在同一目录下，所以不用写具体路径
        pos = []
        Efield = []
        lines = []
        with open(filename, 'r') as file_to_read:
            while True:
                if len(file_to_read.readline()):
                    lines.append(file_to_read.readline())# 整行读取数据
                else:
                    break
            self.IPAdress_1.setText(lines[0])
            self.arrSubnetMasks_1.setText(lines[2])

    def set_first(self):

        # QMessageBox.information('no proper adator')
        print(self.IPAdress_1.text())

        wmiService = wmi.WMI()
        colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)

        if len(colNicConfigs) < 1:
            QMessageBox.information('没有找到可用的网络适配器')
            print('没有找到可用的网络适配器')
            os.system("pause")
            exit()

        # 获取第一个网络适配器的设置
        objNicConfig = colNicConfigs[0]
        # 写入自己的IP地址
        # arrIPAddresses = ['172.20.77.156']
        # arrSubnetMasks = ['255.255.0.0']
        # arrDefaultGateways = ['172.20.77.254']
        # 设置DNS
        # arrDNSServers = ['114.114.114.114', '202.193.160.34', '202.193.160.34']

        arrIPAddresses = []
        arrSubnetMasks = []
        arrDNSServers = []
        arrDefaultGateways = []

        arrIPAddresses.append(self.IPAdress_1.text())
        arrSubnetMasks.append(self.arrSubnetMasks_1.text())
        arrDefaultGateways.append(self.arrDefaultGateways_1.text())
        arrDNSServers=self.arrDNSServers_1.text().split(',')
        arrGatewayCostMetrics = [1]

        intReboot = 0

        returnValue = objNicConfig.EnableStatic(IPAddress=arrIPAddresses, SubnetMask=arrSubnetMasks)
        if returnValue[0] == 0:
            print('  设置IP ok了')
        elif returnValue[0] == 1:
            print('  设置IP ok了')
            intReboot += 1
        else:

            print('我靠，出错了')
            print(returnValue)
            os.system("pause")
            exit()

        returnValue = objNicConfig.SetGateways(DefaultIPGateway=arrDefaultGateways,
                                               GatewayCostMetric=arrGatewayCostMetrics)
        if returnValue[0] == 0:
            print(' 网关任务达成')
        elif returnValue[0] == 1:
            print('网关任务达成')
            intReboot += 1
        else:

            print('我靠，出错了')
            os.system("pause")
            exit()

        returnValue = objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder=arrDNSServers)
        if returnValue[0] == 0:
            print('  成功设置DNS')
        elif returnValue[0] == 1:
            print('  成功设置DNS')
            intReboot += 1
        else:
            print('我靠，出错了')
            os.system("pause")
            exit()

        if intReboot > 0:
            print('重新启动计算机')
        else:
            print('')
            print('  修改后的配置为：')
            print('  IP: ', ', '.join(objNicConfig.IPAddress))
            print('  掩码:', ', '.join(objNicConfig.IPSubnet))
            print('  网关:', ', '.join(objNicConfig.DefaultIPGateway))
            print('  DNS:', ', '.join(objNicConfig.DNSServerSearchOrder))

        QMessageBox.information('收工')
        print('收工')

        os.system("pause")
        print('ccav')



