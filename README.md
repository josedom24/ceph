# ceph

En el master:

	sudo apt-get install ceph-deploy

Instalamos los paquetes en el nodo admin:

	ceph-deploy install nodo-1

Indicamos que el nodo-1 va a ser el monitor:

	ceph-deploy mon create nodo-1

Instalamos los OSD:

	ceph-deploy install nodo-2 nodo-3 nodo-4

Creamos las credenciales:

	ceph-deploy mon create-initial

A continuación para cada unode los nodos vamos a preparar los discos (para cada uno de los nodos):

	ceph-deploy disk list nodo-2
	ceph-deploy disk zap nodo-2:vdb nodo-3:vdb nodo-4:vdb

Preparo los discos

	ceph-deploy  osd prepare nodo-2:vsb nodo-3:vdb nodo-4:vdb

	ceph-deploy osd activate nodo-2:vsb1 nodo-3:vdb1 nodo-4:vdb1

copy the configuration file and admin key to your admin node and your Ceph Nodes

	ceph-deploy admin nodo-1 nodo-2 nodo-3 nodo-4

Finalmente desde el monitor:

	sudo ceph status
	    cluster ac45c1a3-b34c-4f2a-9ac9-e455809e66f1
	     health HEALTH_OK
	     monmap e1: 1 mons at {nodo-1=10.0.1.3:6789/0}
	            election epoch 3, quorum 0 nodo-1
	     osdmap e15: 3 osds: 3 up, 3 in
	            flags sortbitwise,require_jewel_osds
	      pgmap v46: 64 pgs, 1 pools, 0 bytes data, 0 objects
	            100 MB used, 15226 MB / 15326 MB avail
	                  64 active+clean
