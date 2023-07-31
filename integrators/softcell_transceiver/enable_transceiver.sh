#!/usr/bin/env bash

echo -n "enter account identifier fetched from system: "
read CUSTOMERNAME

echo -n "enter the level to alert: "
read WAZUH_LEVEL

function ossec_conf()
{
    additional_file=ossec_integration.conf
    ossec_conf=/var/ossec/etc/ossec.conf

    sed -i "s/WAZUH_LEVEL/$1/g" ${additional_file}
    sed -i "s/CUSTOMERNAME/$1/g" ${additional_file}

    cp ${ossec_conf} ${ossec_conf}_`date +'%Y%m%d_%H%M'`
    cat ${additional_file} >> ${ossec_conf}
    echo "integration configuration is ready..."
}

function copy_files()
{
    integration_dst=/var/ossec/integrations
    tranceiver_file=custom-transceiver.py

    sed -i "s/WAZUH_LEVEL/$1/g" ${tranceiver_file}

    cp ${tranceiver_file} ${integration_dst}
    echo "integration file has been copied successfully..."
}

ossec_conf $WAZUH_LEVEL "$CUSTOMERNAME"
copy_files $WAZUH_LEVEL

systemctl restart wazuh-manager && echo "recycled the wazuh-manager service successfully..." && echo "integration is successful"