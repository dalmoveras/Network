import mininet
import logging
import os

logging.basicConfig(filename='./fat3.log', level=logging.INFO)
logger = logging.getLogger(__name__)


class Switch():
    def __init__():
        if type == 'core':
            pass
        elif type == 'aggregation':
            pass
        elif type == 'edge':
            pass


class Pod():
    def __init__(self,index, k, hosts):
        self.pod_index = index
        self.number_of_hosts = k
        self.hosts = hosts

    def _hosts_descriptions():
        pass#return list(map(lambda host: print(f"Host ==> {host.name}"),self.hosts ))

    def __str__(self):
        return f"[-] ==================== [-]\n \
        Pod: {self.index}\n \
        Total Hosts: {self.number_of_hosts}\
        Hosts: "

class Host():
    def __init__(self, name):
        pass

class Fat3(mininet.topo.Topo):
    """
    Overall number of core switches: (k/2) *(k/2) = (k/2)^2
    Overall number of servers: k *(k/2)* (k/2)= (k^3)/4
    Overall number of switches: k* k + (k/2)^2= ( k^2)*5/4
    Overall number of links : k* (k/2)* k + k* (k/2)^2 = (k^3)*3/4
    """
    core_layer = []
    aggregation_layer = []
    edge_layer = []
    host_layer = []

    def __init__(self, k, fanout):
        logger.debug("Fat3 Topology Bootstrapping ...")
        self.number_of_pods = k
        self.total_core_switches = (k/2)**2
        self.total_aggregation_switches = k*k/2
        self.total_edge_switches = k*k/2
        self.density = fanout
        self.total_hosts = fanout * total_edge_switches

        mininet.topo.Topo.__init__(self)    
