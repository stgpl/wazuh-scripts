#!/var/ossec/framework/python/bin/python3
"""
The above code is a Python script that reads an alert file, processes the alert, generates a
message, and sends the message to a webhook.

:param args: The `args` parameter is a list of command-line arguments passed to the script. In this
script, it is expected to have at least 4 arguments:
:return: The code is not returning anything. It is a script that performs some actions but does not
have a return statement.
"""
import sys
import json
import os
import time

try:
    import requests
except Exception as e:
    print("No module 'requests' found. Install: pip install requests")
    sys.exit(1)

# Global vars
debug_enabled = False
pwd = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
json_alert = {}
now = time.strftime("%a %b %d %H:%M:%S %Z %Y")

# Set paths
log_file = '{0}/logs/integrations.log'.format(pwd)

try:
    with open("/tmp/transceiver.txt", "w+") as tmp:
        tmp.write("Script started")
except:
    pass

def main(args):
    debug("# Starting")

    # Read args
    alert_file_location = args[1]
    webhook = args[3]

    debug("# Webhook")
    debug(webhook)

    debug("# File location")
    debug(alert_file_location)

    # Load alert. Parse JSON object.
    try:
        with open(alert_file_location) as alert_file:
            json_alert = json.load(alert_file)
    except:
        debug("# Alert file %s doesn't exist" % alert_file_location)

    debug("# Processing alert")

    try:
        debug(json_alert)
    except Exception as e:
        debug("Failed getting json_alert %s" % e)
        sys.exit(1)

    debug("# Generating message")
    msg = generate_msg(json_alert)
    if isinstance(msg, str):
        if len(msg) == 0:
            return
    debug(msg)

    debug("# Sending message")
    try:
        with open("/tmp/tranceiver_end.txt", "w+") as tmp:
            tmp.write("Script done pre-msg sending")
    except:
        pass
    send_msg(msg, webhook)

def debug(msg):
    if debug_enabled:
        msg = "{0}: {1}\n".format(now, msg)
        print(msg)
        f = open(log_file, "a")
        f.write(msg)
        f.close()

def send_msg(msg, url):
    headers = { "content-type": "application/json" }
    res = requests.post(url, data=msg, headers=headers, verify=False)

def generate_msg(alert):
    level = alert['rule']['level']
    msg, wazuh_rule, agent = {}, {}, {}

    if (level >= WAZUH_LEVEL):
        msg['timestamp'] = alert["timestamp"]
        msg["all_fields"] = alert

        wazuh_rule['id'] = alert['rule']['id']
        wazuh_rule['description'] = alert['rule']['description']
        wazuh_rule['level'] = alert['rule']['level']
        wazuh_rule['groups'] = alert['rule']['groups']
        msg['wazuh_rule'] = wazuh_rule

        agent['id'] = alert['agent']['id']
        agent['name'] = alert['agent']['name']
        msg['agent'] = agent

    return json.dumps(msg)

if __name__ == "__main__":
    try:
        # Read arguments
        bad_arguments = False
        if len(sys.argv) >= 4:
            msg = '{0} {1} {2} {3} {4}'.format(
                now,
                sys.argv[1],
                sys.argv[2],
                sys.argv[3],
                sys.argv[4] if len(sys.argv) > 4 else '',
            )
            #debug_enabled = (len(sys.argv) > 4 and sys.argv[4] == 'debug')
            debug_enabled = True
        else:
            msg = '{0} Wrong arguments'.format(now)
            bad_arguments = True

        # Logging the call
        try:
            f = open(log_file, 'a')
        except:
            f = open(log_file, 'w+')
            f.write("")
            f.close()

        f = open(log_file, 'a')
        f.write(msg + '\n')
        f.close()

        if bad_arguments:
            debug("# Exiting: Bad arguments. Inputted: %s" % sys.argv)
            sys.exit(1)

        # Main function
        main(sys.argv)
    except Exception as e:
        debug(str(e))
        raise