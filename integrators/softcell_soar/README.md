# Softcell SOAR

This repository helps you integrate your (*Wazuh*) manager with (*Softcell's*) SOAR platform. You may need to create account on Softcell SOAR platform.

### Table of Contents
**[How it Works](#how-it-works)**<br>
**[Configuration](#tags-explanation)**<br>
**[Feedback](#feedback)**<br>

### How it Works

We are using (*Wazuh*) integrator functionality to push threat IP addresses into (*Softcell*) SOAR platform which in turns provide an API endpoint to integrate with your on-premises firewall through EDL functionality. Basic requirements to integrate Softcell SOAR are

  - Enriched [CDB lists](https://github.com/stgpl/wazuh-scripts) which contains threat IP addresses
  - EDL enabled firewall

### Configuration

Request you to download this repository and follow below mentioned commands to integrate (*Softcell*) SOAR platform.

```bash
git clone https://github.com/stgpl/wazuh-scripts.git
cd wazuh-scripts/integrators/softcell_soar
bash enable_soar.sh
```

Follow online instructions to complete the configurations.

### Feedback

All bugs, feature requests, pull requests, feedback, etc., are welcome. [Create an issue](https://github.com/stgpl/wazuh-scripts/issues).