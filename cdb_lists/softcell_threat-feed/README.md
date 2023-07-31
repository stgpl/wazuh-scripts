# Softcell Threat Feed

This script helps you to integrate (*Softcell*)'s Threat Intel feed with your (*Wazuh*) manager to enrich CDB list. You may need to create account on [Softcell Threat Intel](https://threat-feeds.softcell.com) platform.

### Table of Contents
**[How it Works](#how-it-works)**<br>
**[Configuration](#tags-explanation)**<br>
**[Feedback](#feedback)**<br>

### How it Works

We can use CRONTAB to schedule of fetching threat feeds from Softcell Threat Intel platform and enriches CDB list file. You may need to restart wazuh-manager service to update (*Wazuh*) to use updated CDB list.

Make sure you change below mentioned variables of file ip-feed.py before using it

  - api_url: Softcell Threat Intel platform ("https://threat-feeds.softcell.com/api/v1/feeds/ip/")
  - auth_email: Login email on Softcell Threat Intel platform
  - auth_key: API key respective to the login
  - dst_file: CDB file location

*Note:* This script overwrites the CDB list file given.


### Configuration

Request you to download this repository and follow below mentioned commands to integrate (*Softcell*) SOAR platform.

```bash
cd /opt
git clone https://github.com/stgpl/wazuh-scripts.git
cd cdb_lists/softcell_threat-feed

# update the variables with respective values

chmod +x ip-feed.py

# add appropriate CRONJOB to fetch feeds
```


### Feedback

All bugs, feature requests, pull requests, feedback, etc., are welcome. [Create an issue](https://github.com/stgpl/wazuh-scripts/issues).