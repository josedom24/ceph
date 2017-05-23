# ceph

En el master:

	sudo apt-get install ceph-deploy

Instalamos los paquetes en el nodo admin:

	ceph-deploy install nodo-1

Indicamos que el nodo-1 va a ser el monitor:

	ceph-deploy mon create nodo-1

Instalamos los OSD:

	ceph-deploy install nodo-2 nodo-3 nodo-4

