sudo ovs-ofctl del-flows SE1
sudo ovs-ofctl del-flows SA1
sudo ovs-ofctl del-flows SE2
sudo ovs-ofctl del-flows SA2
sudo ovs-ofctl del-flows SC4
sudo ovs-ofctl del-flows SA8
sudo ovs-ofctl del-flows SE8
sudo ovs-ofctl del-flows SE3
sudo ovs-ofctl del-flows SA4
sudo ovs-ofctl del-flows SC3
sudo ovs-ofctl del-flows SA6
sudo ovs-ofctl del-flows SE5
sudo ovs-ofctl del-flows SE7
sudo ovs-ofctl del-flows SA7

#orange_path 
sudo ovs-ofctl  add-flow SE1 in_port=1,action:output=3  
sudo ovs-ofctl  add-flow SE1 in_port=3,action:output=1  
sudo ovs-ofctl  add-flow SA1 in_port=3,action:output=4   
sudo ovs-ofctl  add-flow SA1 in_port=4,action:output=3  
sudo ovs-ofctl  add-flow SE2 in_port=1,action:output=4   
sudo ovs-ofctl  add-flow SE2 in_port=4,action:output=1

#blue_path
sudo ovs-ofctl  add-flow SE2 in_port=3,action:output=2
sudo ovs-ofctl  add-flow SE2 in_port=2,action:output=3
sudo ovs-ofctl  add-flow SA2 in_port=4,action:output=2
sudo ovs-ofctl  add-flow SA2 in_port=2,action:output=4
sudo ovs-ofctl  add-flow SC4 in_port=1,action:output=4
sudo ovs-ofctl  add-flow SC4 in_port=4,action:output=1
sudo ovs-ofctl  add-flow SA8 in_port=2,action:output=4
sudo ovs-ofctl  add-flow SA8 in_port=4,action:output=2
sudo ovs-ofctl  add-flow SE8 in_port=2,action:output=4
sudo ovs-ofctl  add-flow SE8 in_port=4,action:output=2

#green_path
sudo ovs-ofctl  add-flow SE3 in_port=3,action:output=2
sudo ovs-ofctl  add-flow SE3 in_port=2,action:output=3
sudo ovs-ofctl  add-flow SA4 in_port=3,action:output=1
sudo ovs-ofctl  add-flow SA4 in_port=1,action:output=3
sudo ovs-ofctl  add-flow SC3 in_port=2,action:output=3
sudo ovs-ofctl  add-flow SC3 in_port=3,action:output=2
sudo ovs-ofctl  add-flow SA6 in_port=1,action:output=3
sudo ovs-ofctl  add-flow SA6 in_port=3,action:output=1
sudo ovs-ofctl  add-flow SE5 in_port=2,action:output=3
sudo ovs-ofctl  add-flow SE5 in_port=3,action:output=2

#red_path
sudo ovs-ofctl  add-flow SE7 in_port=3,action:output=1
sudo ovs-ofctl  add-flow SE7 in_port=1,action:output=3
sudo ovs-ofctl  add-flow SA7 in_port=3,action:output=4
sudo ovs-ofctl  add-flow SA7 in_port=4,action:output=3
sudo ovs-ofctl  add-flow SE8 in_port=1,action:output=3
sudo ovs-ofctl  add-flow SE8 in_port=3,action:output=1

