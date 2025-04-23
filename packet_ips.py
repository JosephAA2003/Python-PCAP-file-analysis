import dpkt 
import ipaddress
"""function to find out all the packet routes and how often one IP address sends a packet to another"""
def packet_ips(packets: list[dpkt.Packet]):  
    ip_dict = {} 
    for pack in packets: 
        source_ip = ipaddress.IPv4Address(pack.data.src) 
        """ipaddress library extracts source and destination IP from each packet and adds it to a dictionary with the value being the number of occurences """
        dest_ip = ipaddress.IPv4Address(pack.data.dst) 
        route = str(source_ip) + " to " + str(dest_ip)  
        """below if statement checks if the route is already a dictionary key and if it is it appends the value by 1"""
        if route not in ip_dict:  
            ip_dict[route] = 1 
        else: 
            ip_dict[route] += 1  
    """sorts the dictionary by most common traffic firstS"""
    sorted_ip_dict = dict(sorted(ip_dict.items(), key=lambda item: item[1], reverse=True))  
    print("Number of packets transfered between different IP addresses calculated\n")
    print("IP traffic route\n") 
    
    for key, value in sorted_ip_dict.items():
        print(f"{key}: {value}")
    print("\n")