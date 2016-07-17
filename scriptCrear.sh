
#!/usr/bin/bash
VBoxManage createvm --name $1 --register
VBoxManage modifyvm $1 --vram $2 --cpus $3
VBoxManage modifyvm $1 --nic1 bridged --bridgeadapter1 e1000g0
