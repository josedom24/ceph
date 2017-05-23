# ceph

1. En el master:

	sudo apt-get install ceph-deploy

	$ ceph-deploy new nodo-1
	[ceph_deploy.conf][DEBUG ] found configuration file at: /home/debian/.cephdeploy.conf
	[ceph_deploy.cli][INFO  ] Invoked (1.5.37): /usr/bin/ceph-deploy new nodo-1
	[ceph_deploy.cli][INFO  ] ceph-deploy options:
	[ceph_deploy.cli][INFO  ]  username                      : None
	[ceph_deploy.cli][INFO  ]  verbose                       : False
	[ceph_deploy.cli][INFO  ]  overwrite_conf                : False
	[ceph_deploy.cli][INFO  ]  quiet                         : False
	[ceph_deploy.cli][INFO  ]  cd_conf                       : <ceph_deploy.conf.cephdeploy.Conf instance at 0x7fd716eeec68>
	[ceph_deploy.cli][INFO  ]  cluster                       : ceph
	[ceph_deploy.cli][INFO  ]  ssh_copykey                   : True
	[ceph_deploy.cli][INFO  ]  mon                           : ['nodo-1']
	[ceph_deploy.cli][INFO  ]  func                          : <function new at 0x7fd717377cf8>
	[ceph_deploy.cli][INFO  ]  public_network                : None
	[ceph_deploy.cli][INFO  ]  ceph_conf                     : None
	[ceph_deploy.cli][INFO  ]  cluster_network               : None
	[ceph_deploy.cli][INFO  ]  default_release               : False
	[ceph_deploy.cli][INFO  ]  fsid                          : None
	[ceph_deploy.new][DEBUG ] Creating new cluster named ceph
	[ceph_deploy.new][INFO  ] making sure passwordless SSH succeeds
	[nodo-1][DEBUG ] connection detected need for sudo
	[nodo-1][DEBUG ] connected to host: nodo-1 
	[nodo-1][DEBUG ] detect platform information from remote host
	[nodo-1][DEBUG ] detect machine type
	[nodo-1][DEBUG ] find the location of an executable
	[nodo-1][INFO  ] Running command: sudo /bin/ip link show
	[nodo-1][INFO  ] Running command: sudo /bin/ip addr show
	[nodo-1][DEBUG ] IP addresses found: [u'10.0.0.7', u'10.0.1.3']
	[ceph_deploy.new][DEBUG ] Resolving host nodo-1
	[ceph_deploy.new][DEBUG ] Monitor nodo-1 at 10.0.1.3
	[ceph_deploy.new][DEBUG ] Monitor initial members are ['nodo-1']
	[ceph_deploy.new][DEBUG ] Monitor addrs are ['10.0.1.3']
	[ceph_deploy.new][DEBUG ] Creating a random mon key...
	[ceph_deploy.new][DEBUG ] Writing monitor keyring to ceph.mon.keyring...
	[ceph_deploy.new][DEBUG ] Writing initial config to ceph.conf...	


Instalamos los paquetes en el nodo admin:

	ceph-deploy install nodo-1

Indicamos que el nodo-1 va a ser el monitor:

	ceph-deploy mon create nodo-1

Instalamos los OSD:

	ceph-deploy install nodo-2 nodo-3 nodo-4

