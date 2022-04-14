import argparse
import subprocess
import ipwhois
import re
import json
from urllib.request import urlopen


# Через ipinfo.io берем провайдера по ip
def find_provider(ip):
    url = f'http://ipinfo.io/{ ip }/json'
    response = urlopen(url)
    res = json.load(response)
    return res['org'].split()[1] + res['org'].split()[2]


# Берем ASN + страну через ipwhois.IPWhois по ip и добовляем провайдера
def get_ASN_info(ip):
    obj = ipwhois.IPWhois(ip)
    res = obj.lookup_whois()
    return f'{ res["asn"] }\tCOUNTRY:{ str(res["nets"][0]["country"]) }\tPROVIDER:{ find_provider(ip) }'


# Декадируем полученное из запроса "tracert" в консоли, строим и отдаем в удобоваримом виде
def build_line_bebroid(line_for_bebroid):
    decoded_line = line_for_bebroid.decode('CP866')
    match_local_ip = re.findall(r"192\.168\.\d{1,3}\.\d{1,3}", decoded_line)
    match_ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", decoded_line)
    match_miss_ip = re.findall(r"\* {8}\* {8}\*", decoded_line)
    if match_local_ip:
        return f"IP: { match_ip[0] }\t\t ASN: Local"
    elif match_ip:
        return f"IP: {match_ip[-1]}\t ASN: { get_ASN_info(match_ip[-1]) }"
    elif match_miss_ip:
        return f"*\t*\t*"


# Обращаемся в консольку за инфой
def tracer(address):
    data = False
    try:
        data = subprocess.check_output(
            ["tracert", address]).splitlines()
    except subprocess.CalledProcessError:
        print(f'Error for address: "{address}"')
        exit(0)
    for line in data[2:]:
        bebroided_line = build_line_bebroid(line)
        if bebroided_line is not None:
            print(bebroided_line)
    return


# Ну main есть main
def baza():
    parser = argparse.ArgumentParser(description="Task1_trace_router_bebroid")
    parser.add_argument("address", help="IP-address or domain_name")
    args = parser.parse_args()
    return tracer(args.address)


if __name__ == '__main__':
    baza()

