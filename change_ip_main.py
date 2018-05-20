# -*- coding: utf-8 -*-
import wmi
import os
import sys
import change_ip_gui
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
filename = 'ccav.txt'  # txt文件和当前脚本在同一目录下，所以不用写具体路径

def modify_ip(self):
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

    # 从EditLine 获取文本
    arrIPAddresses.append(self.IPAdress_1.text())
    arrSubnetMasks.append(self.arrSubnetMasks_1.text())
    arrDefaultGateways.append(self.arrDefaultGateways_1.text())
    arrDNSServers = self.arrDNSServers_1.text().split(',')
    arrGatewayCostMetrics = [1]

    # save ip
    with open(filename, 'w') as file:
        text = self.IPAdress_1.text()
        file.write(self.IPAdress_1.text())
        file.write(self.arrSubnetMasks_1.text())
        file.write(self.arrDefaultGateways_1.text())
        file.write(self.arrDNSServers_1.text())

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


    print('收工')

    os.system("pause")
    print('ccav')

def get_ip(self):
    with open(filename, 'r') as file_to_read:
        lines = file_to_read.readlines()
        self.IPAdress_1.setText(lines[0])
        self.arrSubnetMasks_1.setText(lines[1])
        self.arrDefaultGateways_1.setText(lines[2])
        self.arrDNSServers_1.setText(lines[3])

if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = change_ip_gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
