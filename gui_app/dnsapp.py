
import socket
import dns.resolver

def get_ip_using_socket(domain):
    try:
        # IP addressを取得
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "ドメインが解決できません"

def check_a_record(domain):
    try:
        # Aレコードを取得
        a_records = dns.resolver.resolve(domain, 'A')
        return [str(record) for record in a_records]
    except dns.resolver.NXDOMAIN:
        return "ドメインが存在しません"
    except dns.resolver.NoAnswer:
        return "Aレコードが見つかりません"

def check_aaaa_record(domain):
    try:
        # AAAAレコードを取得
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        return [str(record) for record in aaaa_records]
    except dns.resolver.NXDOMAIN:
        return "ドメインが存在しません"
    except dns.resolver.NoAnswer:
        return "AAAAレコードが見つかりません"

def check_cname_record(domain):
    try:
        # CNAMEレコードを取得
        cname_records = dns.resolver.resolve(domain, 'CNAME')
        return [str(record) for record in cname_records]
    except dns.resolver.NXDOMAIN:
        return "ドメインが存在しません"
    except dns.resolver.NoAnswer:
        return "CNAMEレコードが見つかりません"

def check_mx_records(domain):
    try:
        # MXレコードを取得
        cname_records = dns.resolver.resolve(domain, 'MX')
        return [str(record) for record in cname_records]
    except dns.resolver.NXDOMAIN:
        return "ドメインが存在しません"
    except dns.resolver.NoAnswer:
        return "MXレコードが見つかりません"

def check_ns_record(domain):
    try:
        # NSレコードを取得
        ns_records = dns.resolver.resolve(domain, 'NS')
        return [str(record) for record in ns_records]
    except dns.resolver.NXDOMAIN:
        return "ドメインが存在しません"
    except dns.resolver.NoAnswer:
        return "NSレコードが見つかりません"

def check_ptr_record(ip_address_to_check):
    try:
        # PTRレコードを取得
        ptr_record = dns.resolver.resolve(dns.reversename.from_address(ip_address_to_check), 'PTR')
        return [str(record) for record in ptr_record]
    except dns.resolver.NXDOMAIN:
        return "PTRレコードが見つかりません"
    except dns.resolver.NoAnswer:
        return "PTRレコードが見つかりません"

def check_txt_record(domain):
    try:
        # アダプターのDNSによって出てこないことがある
        # TXTレコードを取得 (タイムアウト 10秒)
        txt_records = dns.resolver.resolve(domain, 'TXT', lifetime=10.0)
        return [str(record) for record in txt_records]
    except dns.resolver.NXDOMAIN:
        return "ドメインが存在しません"
    except dns.resolver.NoAnswer:
        return "TXTレコードが見つかりません"
    except dns.resolver.LifetimeTimeout:
        return "タイムアウト: DNSサーバーが応答しないか、遅い可能性があります"

def check_soa_record(domain):
    try:
        # SOAレコードを取得
        soa_records = dns.resolver.resolve(domain, 'SOA')
        return [str(record) for record in soa_records]
    except dns.resolver.NXDOMAIN:
        return "ドメインが存在しません"
    except dns.resolver.NoAnswer:
        return "SOAレコードが見つかりません"

domain_to_check = "e-seibu.co.jp"

ip_address_to_check = get_ip_using_socket(domain_to_check)

print(f"{domain_to_check} のIPアドレス: {ip_address_to_check}")
print(f"Aレコード: {check_a_record(domain_to_check)}")
print(f"AAAAレコード: {check_aaaa_record(domain_to_check)}")
print(f"CNAMEレコード: {check_cname_record(domain_to_check)}")
print(f"MXレコード: {check_mx_records(domain_to_check)}")
print(f"NSレコード: {check_ns_record(domain_to_check)}")
print(f"PTRレコード: {check_ptr_record(ip_address_to_check)}")
print(f"TXTレコード: {check_txt_record(domain_to_check)}")
print(f"SOAレコード: {check_soa_record(domain_to_check)}")