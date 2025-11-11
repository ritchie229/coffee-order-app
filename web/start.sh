#!/bin/bash



#mv node_exporter /usr/bin/
#useradd -rs /bin/false node_exporter
#chown node_exporter:node_exporter /usr/bin/node_exporter


#cat <<EOF> /etc/systemd/system/node_exporter.service
#[Unit]
#Description=Prometheus Node Exporter
#After=network.target
 
#[Service]
#User=node_exporter
#Group=node_exporter
#Type=simple
#Restart=on-failure
#ExecStart=/usr/bin/node_exporter
 
#[Install]
#WantedBy=multi-user.target
#EOF

#systemctl daemon-reload
#systemctl start node_exporter
#systemctl enable node_exporter
#systemctl status node_exporter
#node_exporter --version

python app.py &
./node_exporter


