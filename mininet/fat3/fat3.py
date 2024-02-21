from mininet.topo import Topo
import logging
import os
import sys

LAYERS = {
    'CORE': '1',
    'AGGREGATION': '2',
    'EDGE': '3'
}


class Fat3(Topo):
    """
    Overall number of core switches: (k/2) *(k/2) = (k/2)^2
    Overall number of servers: k *(k/2)* (k/2)= (k^3)/4
    Overall number of switches: k* k + (k/2)^2= ( k^2)*5/4
    Overall number of links : k* (k/2)* k + k* (k/2)^2 = (k^3)*3/4
    """

    def __init__(self, k: int, fanout: int):
        self.number_of_pods = int(k)
        self.total_core_switches = int((k/2)**2)
        self.total_aggregation_switches = int(k*k/2)
        self.total_edge_switches = int(k*k/2)
        self.total_hosts = int(fanout * self.total_edge_switches)
        self.core_layer = list(
            map(lambda x: 'SC'+str(x), range(1, self.total_core_switches+1)))
        self.aggregation_layer = list(
            map(lambda x: 'SA'+str(x), range(1, self.total_aggregation_switches+1)))
        self.edge_layer = list(
            map(lambda x: 'SE'+str(x), range(1, self.total_edge_switches+1)))
        self.host_layer = list(map(lambda x: 'H'+str(x), range(1,self.total_hosts+1))) 

        Topo.__init__(self)

        self._create_nodes()
        self._connect()

    def _create_nodes(self):  
        list(map(lambda x: self.addHost(x),self.host_layer))
        list(map(lambda x: self.addSwitch(x),self.core_layer))
        list(map(lambda x: self.addSwitch(x),self.aggregation_layer))
        list(map(lambda x: self.addSwitch(x),self.edge_layer))


    def _connect(self):
        self._connect_core_to_aggregation()
        self._connect_aggregation_to_edge()
        self._connect_edge_to_hosts()

    def _connect_core_to_aggregation(self):
        even = ['SA2', 'SA4', 'SA6', 'SA8']
        odd = ['SA1', 'SA3', 'SA5', 'SA7']
        list(map(lambda x: self.addLink('SC1', x), odd))
        list(map(lambda x: self.addLink('SC2', x), odd))
        list(map(lambda x: self.addLink('SC3', x), even))
        list(map(lambda x: self.addLink('SC4', x), even))

    def _connect_aggregation_to_edge(self):
        index = 0
        for i in range(0, self.total_aggregation_switches, 2):
            self.addLink(self.aggregation_layer[i], self.edge_layer[index])
            self.addLink(self.aggregation_layer[i], self.edge_layer[index+1])
            self.addLink(self.aggregation_layer[i+1], self.edge_layer[index])
            self.addLink(self.aggregation_layer[i+1], self.edge_layer[index+1])
            index += 2

    def _connect_edge_to_hosts(self):
        hosts = list(map(lambda x: 'H'+str(x), range(1, self.total_hosts+1)))
        index = 0
        for sw in self.edge_layer:
            self.addLink(sw, hosts[index])
            self.addLink(sw, hosts[index+1])
            index += 2


topos = {'fat3': (lambda: Fat3(4, 2))}
