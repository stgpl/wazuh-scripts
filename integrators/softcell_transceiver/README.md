# Softcell Transceiver

This repository helps you integrate your (*Wazuh*) manager with (*Softcell's*) Transceiver platform. You may need to create account on Softcell Transceiver platform.

Softcell Transceiver is an API which accepts threat/attack information happened on your network then helps us to report the same with CERTIN through dashboard.

### Table of Contents
**[How it Works](#how-it-works)**<br>
**[Configuration](#tags-explanation)**<br>
**[Feedback](#feedback)**<br>

### How it Works

We are using (*Wazuh*) integrator functionality to push threat information into (*Softcell*) Transceiver API which in turns provides dashboard to categorise and report with CERTIN.


### Configuration

Request you to download this repository and follow below mentioned commands to integrate (*Softcell*) Transceiver platform

```bash
git clone https://github.com/stgpl/wazuh-scripts.git
cd wazuh-scripts/integrators/softcell_transceiver
bash enable_transceiver.sh
```

### Feedback

All bugs, feature requests, pull requests, feedback, etc., are welcome. [Create an issue](https://github.com/stgpl/wazuh-scripts/issues).