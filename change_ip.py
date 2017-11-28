import wmi
import os

print('�޸�ip�У����ĺ���')

wmiService = wmi.WMI()

colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled = True)

if len(colNicConfigs) < 1:
    print('û���ҵ����õ�����������')
    os.system("pause")
    exit()

# ��ȡ��һ������������������
objNicConfig = colNicConfigs[0]
#д���Լ���IP��ַ
arrIPAddresses = ['172.20.77.156']
arrSubnetMasks = ['255.255.0.0']
arrDefaultGateways = ['172.20.77.254']
arrGatewayCostMetrics = [1]
#����DNS
arrDNSServers = ['114.114.114.114', '202.193.160.34', '202.193.160.34']
intReboot = 0

returnValue = objNicConfig.EnableStatic(IPAddress = arrIPAddresses, SubnetMask = arrSubnetMasks)
if returnValue[0] == 0:
    print('  ����IP ok��')
elif returnValue[0] == 1:
    print('  ����IP ok��')
    intReboot += 1
else:
    print('�ҿ���������')
    print(returnValue)
    os.system("pause")
    exit()

returnValue = objNicConfig.SetGateways(DefaultIPGateway = arrDefaultGateways, GatewayCostMetric = arrGatewayCostMetrics)
if returnValue[0] == 0:
    print(' ����������')
elif returnValue[0] == 1:
    print('����������')
    intReboot += 1
else:
    print('�ҿ���������')
    os.system("pause")
    exit()

returnValue = objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder = arrDNSServers)
if returnValue[0] == 0:
    print('  �ɹ�����DNS')
elif returnValue[0] == 1:
    print('  �ɹ�����DNS')
    intReboot += 1
else:
    print('�ҿ���������')
    os.system("pause")
    exit()

if intReboot > 0:
    print('�������������')
else:
    print('')
    print('  �޸ĺ������Ϊ��')
    print('  IP: ', ', '.join(objNicConfig.IPAddress))
    print('  ����:', ', '.join(objNicConfig.IPSubnet))
    print('  ����:', ', '.join(objNicConfig.DefaultIPGateway))
    print('  DNS:', ', '.join(objNicConfig.DNSServerSearchOrder))


print('�չ�')
os.system("pause")