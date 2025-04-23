import dpkt 
import ipaddress 
import networkx as nx 
import matplotlib.pyplot as plt 
"""function to create a network graph of allpacket routes """
def network_graph(packets: list[dpkt.Packet]): 
    graph = nx.DiGraph()  
    """create a list for ip addresses aswell as when the ip was a source and destination""" 
    source_ip = [] 
    destination_ip = []
    ip_addresses = [] 
    for pack in packets: 
        source = ipaddress.IPv4Address(pack.data.src) 
        destination = ipaddress.IPv4Address(pack.data.dst) 
        source_ip.append(source) 
        destination_ip.append(destination)  
        """extract all source and destination IPs and if it isn't currently, add it to the ip_addresses list"""
        if source not in ip_addresses: 
            ip_addresses.append(source)
        if destination not in ip_addresses: 
            ip_addresses.append(destination)     
    for ip in ip_addresses:  
        """add all ip addresses as nodes in the graph"""
        graph.add_node(ip)
    for i in range(len(source_ip)): 
        occurence = 0
        for x in range(len(source_ip)): 
            if source_ip[i] == source_ip[x] and destination_ip[i] == destination_ip[x]:  
                """create two loops that loop over the same two lists. This checks how many times two ip addresses appear on the two lists at the same index"""
                occurence = occurence + 1 
        graph.add_edge(source_ip[i], destination_ip[i], weight=occurence) 
        """add or overwrite the two ip addresses to the graph as edges with occurences being the weight"""
    pos = nx.spring_layout(graph, k=20) 
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_color="black", font_weight="bold", arrowsize=10, connectionstyle="arc3,rad=0.1", edgecolors="black", arrowstyle='fancy',)
    edge_labels = {(u, v): f"{d['weight']}" for u, v, d in graph.edges(data=True)}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels) 
    print("Network graph generated\n")
    plt.savefig("network_graph.png", format="PNG")
    plt.show()