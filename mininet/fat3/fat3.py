import mininet
import logging
import os
import sys


logging.basicConfig(filename='./fat3.log', level=logging.INFO)
logger = logging.getLogger(__name__)

LAYERS = {
    'CORE':1,
    'AGGREGATION':2,
    'EDGE':3
}

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
        return list(map(lambda host: print(f"Host ==> {host.name}"),self.hosts ))

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
    
    def build(self):
        self._core_init(self.total_core_switches)
        self._aggregation_init(self.total_aggregation_switches)
        self._edge_init(self.total_edges_switches)
        self._host_init(total_hosts)
    
    def _add_switch(self, LAYER, total)-> list:
        return list(map(lambda x: self.core_layer.append('s'+str(LAYER)+'0'+str(x)), range(0,total)))

    def _core_init(self, total):
        logger.debug("[%] Core layer init [%]") 
        self._add_switch(self, LAYERS['CORE'], total)

    def _aggregation_init(self, total):
        logger.debug("[%] Aggregation layer init [%]") 
        self._add_switch(self, LAYERS['AGGREGATION'], total)
        
    def _edge_init(self, total):
        logger.debug("[%] Edge layer init [%]") 
        self._add_switch(self, LAYERS['EDGE'], total)   

    def _hosts_init(self, total):
        logger.debug("[%] Hosts init [%]")
        self.host_layer = list(map(lambda x:self.host_layer.append('h0'+str(x)),range(0,total)))

def main(number_of_pods: int, fanout: int, ip: str, port:int, bandwith=15, delay=1.0):
    topology = Fat3(number_of_pods, fanout)
    topology.build()


if __name__== '__main__':
    if os.getuid() == 0:
        main(4,2)
    else:
        logger.debug("Lack of privileges. Try again using sudo.\n")
        sys.exit(1)

