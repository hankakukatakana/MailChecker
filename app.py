from flask import Flask, render_template, request, jsonify
import socket
import dns.resolver

class DNSChecker:
    def get_ip_using_socket(self, domain):
        try:
            # IP addressを取得
            ip_address = socket.gethostbyname(domain)
            return ip_address
        except socket.gaierror:
            return "ドメインが解決できません"

    def check_a_record(self, domain):
        try:
            # Aレコードを取得
            a_records = dns.resolver.resolve(domain, 'A')
            return [str(record) for record in a_records]
        except dns.resolver.NXDOMAIN:
            return "ドメインが存在しません"
        except dns.resolver.NoAnswer:
            return "Aレコードが見つかりません"

    def check_aaaa_record(self, domain):
        try:
            # AAAAレコードを取得
            aaaa_records = dns.resolver.resolve(domain, 'AAAA')
            return [str(record) for record in aaaa_records]
        except dns.resolver.NXDOMAIN:
            return "ドメインが存在しません"
        except dns.resolver.NoAnswer:
            return "AAAAレコードが見つかりません"

    def check_cname_record(self, domain):
        try:
            # CNAMEレコードを取得
            cname_records = dns.resolver.resolve(domain, 'CNAME')
            return [str(record) for record in cname_records]
        except dns.resolver.NXDOMAIN:
            return "ドメインが存在しません"
        except dns.resolver.NoAnswer:
            return "CNAMEレコードが見つかりません"

    def check_mx_records(self, domain):
        try:
            # MXレコードを取得
            cname_records = dns.resolver.resolve(domain, 'MX')
            return [str(record) for record in cname_records]
        except dns.resolver.NXDOMAIN:
            return "ドメインが存在しません"
        except dns.resolver.NoAnswer:
            return "MXレコードが見つかりません"

    def check_ns_record(self, domain):
        try:
            # NSレコードを取得
            ns_records = dns.resolver.resolve(domain, 'NS')
            return [str(record) for record in ns_records]
        except dns.resolver.NXDOMAIN:
            return "ドメインが存在しません"
        except dns.resolver.NoAnswer:
            return "NSレコードが見つかりません"

    def check_ptr_record(self, ip_address_to_check):
        try:
            # PTRレコードを取得
            ptr_record = dns.resolver.resolve(dns.reversename.from_address(ip_address_to_check), 'PTR')
            return [str(record) for record in ptr_record]
        except dns.resolver.NXDOMAIN:
            return "PTRレコードが見つかりません"
        except dns.resolver.NoAnswer:
            return "PTRレコードが見つかりません"

    def check_txt_record(self, domain):
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

    def check_soa_record(self, domain):
        try:
            # SOAレコードを取得
            soa_records = dns.resolver.resolve(domain, 'SOA')
            return [str(record) for record in soa_records]
        except dns.resolver.NXDOMAIN:
            return "ドメインが存在しません"
        except dns.resolver.NoAnswer:
            return "SOAレコードが見つかりません"

app = Flask(__name__)
dns_checker = DNSChecker()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_dns():
    domain = request.form['domain']
    ip_address = dns_checker.get_ip_using_socket(domain)
    a_records = dns_checker.check_a_record(domain)
    aaaa_records = dns_checker.check_aaaa_record(domain)
    cname_records = dns_checker.check_cname_record(domain)
    mx_records = dns_checker.check_mx_records(domain)
    ns_records = dns_checker.check_ns_record(domain)
    ptr_records = dns_checker.check_ptr_record(ip_address)
    txt_records = dns_checker.check_txt_record(domain)
    soa_records = dns_checker.check_soa_record(domain)

    result = {
        'domain': domain,
        'ip_address': ip_address,
        'a_records': a_records,
        'aaaa_records': aaaa_records,
        'cname_records': cname_records,
        'mx_records': mx_records,
        'ns_records': ns_records,
        'ptr_records': ptr_records,
        'txt_records': txt_records,
        'soa_records': soa_records
    }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)