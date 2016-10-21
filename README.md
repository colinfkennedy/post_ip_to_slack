<h1>Install instructions</h1>
* Set up a [Slack Incoming Web](https://api.slack.com/incoming-webhooks) Hook and note the URL.
* Copy post_ip_to_slack.py onto your RPi.
* Edit the file and replace <Your_Slack_Hook_URL> with your Slack Hook URL.
* Copy the contents of the rc.local.txt and paste them into your /etc/rc.local script on your RPi.
* Change the <your_script_location> to where you have saved the post_ip_to_slack.py
