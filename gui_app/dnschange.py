import win32com.client
import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("管理者権限で実行してください.")
    sys.exit()


def set_dns_servers(interface_name, dns_servers):
    objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    objSWbemServices = objWMIService.ConnectServer(".", "root\cimv2")
    colItems = objSWbemServices.ExecQuery(f"SELECT * FROM Win32_NetworkAdapterConfiguration WHERE Description = '{interface_name}'")

    for objItem in colItems:
        objItem.SetDNSServerSearchOrder(dns_servers)

# DNSをCloudflareのDNSに切り替える
cloudflare_dns_servers = ["1.1.1.1", "1.0.0.1"]
set_dns_servers("Ethernet", cloudflare_dns_servers)

# DNSをGoogleのDNSに切り替える
google_dns_servers = ["8.8.8.8", "8.8.4.4"]
set_dns_servers("Ethernet", google_dns_servers)
