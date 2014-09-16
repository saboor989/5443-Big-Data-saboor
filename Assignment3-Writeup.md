 
 
 Assignment 3
==============

Pic of Where is Hadoop and JPS.

![whereishadoop](https://cloud.githubusercontent.com/assets/8570076/4262606/f3f2f802-3bac-11e4-97c7-6f96163935b1.png)

* The Addition of the Nodes to the cluster,
 
  The nodes are the machine which will be able to reach each other over the network. The easiest is to put both machines   in the same network with regard to hardware and software configuration, Like connecting both machines via a single hub   and configure the network interfaces to use a common network.
  
  List all slave hostnames or IP addresses in your conf/slaves file, one per line.
  Like :
  * 192.168.0.1    master
  * 192.168.0.2    slave
  
  In order to connect to the slave machine the master public ssh keys to added to the authorized keys of the hadoop user   slave($HOME/.ssh/authorized_keys).
  Distributing the SSH public key of hadoopuser@master using 
  hduser@master:~$ ssh-copy-id -i $HOME/.ssh/id_rsa.pub hduser@slave
  this will prompt for the pwd of the slave , copy the public SSH key , and creating directory and fixing the
  permissions.

  Testing the connection by command $ ssh master

  prompts:for example :(The authenticity of host 'master (192.168.0.1)' can't be established.
  RSA key fingerprint is 3b:21:b3:c0:21:5c:7c:54:2f:1e:2d:96:79:eb:7f:95.
  Are you sure you want to continue connecting (yes/no)? yes
  Warning: Permanently added 'master' (RSA) to the list of known hosts.
  Linux master 2.6.20-16-386 #2 Thu Jun 7 20:16:13 UTC 2007 i686)
  
  from master to slave.$ ssh slave
  prompts:for example (The authenticity of host 'slave (192.168.0.2)' can't be established.
  RSA key fingerprint is 74:d7:61:86:db:86:8f:31:90:9c:68:b0:13:88:52:72.
  Are you sure you want to continue connecting (yes/no)? yes
  Warning: Permanently added 'slave' (RSA) to the list of known hosts.
  Ubuntu 10.04
 
*
 
