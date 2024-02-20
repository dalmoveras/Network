import mininet
import logging
import os
import sys


logging.basicConfig(filename='./logs/fat3.log', level=logging.INFO)
logger = logging.getLogger(__name__)

LAYERS = {
    'CORE': '1',
    'AGGREGATION': '2',
    'EDGE': '3'
}


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

    def __init__(self, k: int, fanout: int):
        logger.debug("Fat3 Topology Bootstrapping ...")
        self.number_of_pods = int(k)
        self.total_core_switches = int((k/2)**2)
        self.total_aggregation_switches = int(k*k/2)
        self.total_edge_switches = int(k*k/2)
        self.density = fanout
        self.total_hosts = int(fanout * self.total_edge_switches)
     
        mininet.topo.Topo.__init__(self)

        self.build()

    def build(self):
        self._core_init(self.total_core_switches)
        self._aggregation_init(self.total_aggregation_switches)
        self._edge_init(self.total_edge_switches)
        self._host_init(self.total_hosts)
        self._connect()

    def add_switch(self, LAYER, total) -> list:
        layer = None
        if LAYER == 'CORE':
            list(map(lambda x: self.addSwitch('SC'+str(x)),range(1,total+1)))
        elif LAYER == 'AGGREGATION':
            list(map(lambda x: self.addSwitch('SA'+str(x)), range(1, total+1)))
        else:  
            list(map(lambda x: self.addSwitch('SE'+str(x)), range(1, total+1)))

    def _core_init(self, total):
        logger.debug("[%] Core layer init [%]")
        self.add_switch('CORE', total)

    def _aggregation_init(self, total):
        logger.debug("[%] Aggregation layer init [%]")
        self.add_switch('AGGREGATION', total)

    def _edge_init(self, total):
        logger.debug("[%] Edge layer init [%]")
        self.add_switch('EDGE', total)

    def _host_init(self, total):
        logger.debug("[%] Hosts init [%]")
        list(map(lambda x: self.host_layer.append(
            'h'+str(x)), range(1, self.total_hosts+1)))
        list(map(lambda x: self.addHost(x), self.host_layer))   
    
    def _connect(self):
        self._connect_core_to_aggregation()
        self._connect_aggregation_to_edge()
        self._connect_edge_to_hosts()

    def _connect_core_to_aggregation(self):
        even = ['SA2','SA4','SA6','SA8']
        odd = ['SA1','SA3','SA5','SA7']
        list(map(lambda x: self.addLink('SC1',x), odd))       
        list(map(lambda x: self.addLink('SC2',x), odd))       
        list(map(lambda x: self.addLink('SC3',x), even))       
        list(map(lambda x: self.addLink('SC4',x), even))       

    def _connect_aggregation_to_edge(self):
        pass

    def _connect_edge_to_hosts(self):
        pass
topos = {'fat3': (lambda: Fat3(4, 2))}
