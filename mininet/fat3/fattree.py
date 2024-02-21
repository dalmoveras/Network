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
        self.addLink('SE1','H1')
        self.addLink('SE1','H2')
        self.addLink('SE2','H3')
        self.addLink('SE2','H4')
        self.addLink('SE3','H5')
        self.addLink('SE3','H6')
        self.addLink('SE4','H7')
        self.addLink('SE4','H8')
        self.addLink('SE5','H9')
        self.addLink('SE5','H10')
        self.addLink('SE6','H11')
        self.addLink('SE6','H12')
        self.addLink('SE7','H13')
        self.addLink('SE7','H14')
        self.addLink('SE8','H15')
        self.addLink('SE8','H16')
        #edge_switches = list(map(lambda x: 'SE'+str(x), range(1, self.total_edge_switches+1)))
        #hosts = list(map(lambda x: 'H'+str(x), range(1, self.total_hosts+1)))
        #index = 0
        #for sw in edge_switches:
        #    self.addLink(sw,hosts[index])
        #    self.addLink(sw,hosts[index+1])
        #    index+=2

topos = {'fat3': (lambda: Fat3(4, 2))}
