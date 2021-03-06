import netifaces as ni
import slackweb
slack = slackweb.Slack(url="<Your_Slack_Hook_URL>")
message = "RPi has started up. Ip addresses:\n"

print "Finding IP addresses"

for interface in ni.interfaces():
    addresses = ni.ifaddresses(interface)
    internet_addresses = addresses.get(ni.AF_INET)
    if internet_addresses is not None:
        message += 'Interface: ' + interface + ":\n"
        for internet_address in internet_addresses:
            ip = internet_address.get('addr')
            if ip is not None:
                message += ip + '\n'
        message +='\n'

print "Sending message to slack: "
print message

slack.notify(text=message)
