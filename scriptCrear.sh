
#!/usr/bin/bash
VBoxManage createvm --name $1 --register
VBoxManage modifyvm $1 --vram $2 --cpus $3
