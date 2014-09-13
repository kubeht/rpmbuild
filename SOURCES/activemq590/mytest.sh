sudo /etc/init.d/ht-activemq  stop

export PACKAGE=activemq-5.9.0-HT.1.0.1
export DEFAULT_CONFIG=activemqconfig-default-5.9.0-HT.1.0.3
export HSA_CONFIG=activemqconfig-hsa-5.9.0-HT.1.0.3
export CONFIG=${HSA_CONFIG}
##export CONFIG=activemqconfig-default-5.9.0-HT.1.0.0


export PACKAGE_RPM=/data/RPMS/x86_64/${PACKAGE}.x86_64.rpm
export DEFAULT_CONFIG_RPM=/data/RPMS/x86_64/${DEFAULT_CONFIG}.x86_64.rpm
export HSA_CONFIG_RPM=/data/RPMS/x86_64/${HSA_CONFIG}.x86_64.rpm
export CONFIG_RPM=${HSA_CONFIG_RPM}
##export CONFIG_RPM=/data/RPMS/x86_64/activemqconfig-default-5.9.0-HT.1.0.0.x86_64.rpm

echo "=====================> uninstalling"
sudo rpm -ev $PACKAGE  
sudo rpm -ev $HSA_CONFIG 
sudo rpm -ev $DEFAULT_CONFIG 


echo "=====================> checking leftover"
sudo ls -R /opt/activemq

##sudo rm -rf /opt/activemq


echo "=====================> installing" 
sudo rpm -ivh $PACKAGE_RPM $CONFIG_RPM 


echo "====================> $PACKAGE files"
sudo rpm -vV $PACKAGE  | grep "\(conf\|bin\|data\)"
echo "====================> $CONFIG files"
sudo rpm -vV $CONFIG  | grep "\(conf\|bin\|data\|init\)"


sudo /etc/init.d/ht-activemq  start
sudo /etc/init.d/ht-activemq  status


ps -ef | grep java

sudo grep -r "multicast" /opt/activemq/bin/linux-x86-64/wrapper.conf

sleep 3

sudo tail -f /opt/activemq/data/activemq.log

