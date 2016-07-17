
#!/usr/bin/bash
RAM=`echo $2 | awk '{print $1}'`
CPU=`echo $3 | awk '{print $1}'`

VBoxManage createvm --name $1 --register
VBoxManage modifyvm $1 --vram $RAM --cpus $CPU
VBoxManage modifyvm $1 --nic1 bridged --bridgeadapter1 e1000g0

echo "Creada!!!"
