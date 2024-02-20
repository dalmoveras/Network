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
     
        Topo.__init__(self)

        self.build()

    def build(self):

        list(map(lambda x: self.addSwitch('SC'+str(x)),range(1,self.total_core_switches+1)))
        list(map(lambda x: self.addSwitch('SA'+str(x)),range(1,self.total_aggregation_switches+1)))
        list(map(lambda x: self.addSwitch('SE'+str(x)),range(1,self.total_edge_switches+1)))       
        list(map(lambda x: self.addHost('H'+str(x)), range(1,self.total_hosts+1)))   
        
        self._connect()

    def _connect(self):
        #self._connect_core_to_aggregation()
        #self._connect_aggregation_to_edge()
        self._connect_edge_to_hosts()

    def _connect_core_to_aggregation(self):
        even = ['SA2','SA4','SA6','SA8']
        odd = ['SA1','SA3','SA5','SA7']
        list(map(lambda x: self.addLink('SC1',x), odd))       
        list(map(lambda x: self.addLink('SC2',x), odd))       
        list(map(lambda x: self.addLink('SC3',x), even))       
        list(map(lambda x: self.addLink('SC4',x), even))       

    def _connect_aggregation_to_edge(self):
        for pod in self.pods:
            self.addLink(pod[0],pod[2])
            self.addLink(pod[0],pod[3])
            self.addLink(pod[1],pod[2])
            self.addLink(pod[1],pod[3])
  
    def _connect_edge_to_hosts(self):
        import pdb;pdb.set_trace()
        for i in range(1, self.total_edge_switches+1):
            self.addLink('SE'+str(i),'H'+str(i) )
            self.addLink('SE'+str(i),'H'+str(i+1) )

topos = {'fat3': (lambda: Fat3(4, 2))}
