#!/usr/bin/env bash

echo -n "enter account identifier fetched from SOAR: "
read CUSTOMERNAME

echo -n "enter email address which used to login into SOAR: "
read AUTHEMAIL

echo -n "enter SOAR API key respective to the email address: "
read APIKEY

function ossec_conf()
{
    additional_file=ossec_integration.conf
    ossec_conf=/var/ossec/etc/ossec.conf

    sed -i "s/CUSTOMERNAME/$1/g" ${additional_file}
    sed -i "s/APIKEY/$2/g" ${additional_file}

    cp ${ossec_conf} ${ossec_conf}_`date +'%Y%m%d_%H%M'`
    cat ${additional_file} >> ${ossec_conf}
    echo "integration configuration is ready..."
}

function copy_files()
{
    integration_dst=/var/ossec/integrations
    soar_file=custom-soar.py

    sed -i "s/AUTHEMAIL/$1/g" ${soar_file}
    sed -i "s/APIKEY/$2/g" ${soar_file}

    cp ${soar_file} ${integration_dst}
    echo "integration file has been copied successfully..."
}

ossec_conf $CUSTOMERNAME $APIKEY
copy_files $AUTHEMAIL $APIKEY

systemctl restart wazuh-manager && echo "recycled the wazuh-manager service successfully..." && echo "integration is successful"