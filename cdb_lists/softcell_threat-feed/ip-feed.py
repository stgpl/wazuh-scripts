#!/usr/bin/env python3
"""
The above Python script retrieves IP addresses from an API, validates them, and writes them to a
file.

:param ip_str: The `ip_str` parameter is a string that represents an IP address. It is used in the
`validate_ip_address` function to check if the IP address is valid and whether it is an IPv4 or IPv6
address
:return: The code is making a GET request to an API endpoint specified by `api_url` and retrieving a
list of IP addresses. It then validates each IP address using the `validate_ip_address` function. If
the IP address is valid, it is written to a file specified by `dst_file`. The code returns the
message "[api_url] -> [dst_file]" if the operation is successful.
"""
# -*- coding: utf-8 -*--
import re
from sys import exit, argv
try:
    import requests
except Exception as e:
    print("No module 'requests' found. Install: pip install requests")
    exit(1)

api_url = "https://threat-feeds.softcell.com/api/v1/feeds/ip/"
auth_email = "AUTH_EMAIL"
auth_key = "API_KEY"

dst_file = "/tmp/softcell-feed"


def validate_ip_address(ip_str:str):
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    ipv6_pattern = r'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4})|(([0-9a-fA-F]{1,4}:){1,6}:)|(:(:[0-9a-fA-F]{1,4}){1,6})|(([0-9a-fA-F]{1,4}:){1,5}:[0-9a-fA-F]{1,4})|(:(([0-9a-fA-F]{1,4}:){1,4})[0-9a-fA-F]{1,4})|((([0-9a-fA-F]{1,4}:){1,3}[0-9a-fA-F]{1,4}:){1,2}[0-9a-fA-F]{1,4})|(:((([0-9a-fA-F]{1,4}:){1,3}[0-9a-fA-F]{1,4}:){1,3})[0-9a-fA-F]{1,4})|((([0-9a-fA-F]{1,4}:){1,4}[0-9a-fA-F]{1,4}){1,2}:)|((([0-9a-fA-F]{1,4}:){1,5}[0-9a-fA-F]{1,4}):)|((([0-9a-fA-F]{1,4}:){1,6}[0-9a-fA-F]{1,4})|(:(([0-9a-fA-F]{1,4}:){1,7}|:))|:|:)$'
    if re.match(ipv4_pattern, ip_str):
        return "IPv4"
    if re.match(ipv6_pattern, ip_str):
        return "IPv6"
    return "Invalid"


try:
    first_time = True
    fo = open(dst_file, 'w')
    headers = {
            'X-Auth-Key': auth_key,
            'X-Auth-Email': auth_email
        }
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    for line in response.iter_lines(decode_unicode=True):
        match = validate_ip_address(line.decode())
        if match == "Invalid":
            continue
        elif match == "IPv4":
            ip = line.decode() + ":"
        elif match == "IPv6":
            ip = f'"{line.decode()}":'
        else:
            continue
        if first_time:
            fo.write(ip)
            first_time = False
        else:
            fo.write("\n" + ip)
    fo.close()
    print("[{0}] -> [{1}]".format(api_url, dst_file))
except requests.exceptions.RequestException as e:
    print(f"Error calling the API: {e}")
    exit(1)
except Exception as e:
    print("Error:\n{0}\nExiting".format(e))
    exit(1)