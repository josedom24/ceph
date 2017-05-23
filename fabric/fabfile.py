# -*- coding: utf-8 -*-
from fabric.api import *
from fabric.contrib.files import exists
env.user   = "debian"
   

def main():
    # Configurar el /etc/hosts
    put('./hosts','/etc/hosts',use_sudo=True)

    sudo("apt-get install apt-transport-https -y --force-yes")

    #Repositorio ceph
    sudo("wget -q -O- 'https://download.ceph.com/keys/release.asc' | sudo apt-key add -")
    sudo("echo deb https://download.ceph.com/debian-kraken/ $(lsb_release -sc) main | sudo tee /etc/apt/sources.list.d/ceph.list")

	# Actualizar el sistema
    sudo("apt-get update")
    #sudo("apt-get -y upgrade")    

    # Copiar la clave ssh y configurar permisos:
    put('~/.ssh/id_rsa','~/.ssh/id_rsa', mode=0600)

    sudo("apt-get install ntp -y --force-yes")