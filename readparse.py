import dpkt

def readparse(file_path: str)-> list[dpkt.Packet]: 
    """function to read and parse the PCAP file"""
    packets = [] 
    packet_ts = []
    try:    
        with open(file_path, 'rb') as file: 
            pcap = dpkt.pcap.Reader(file)  
            print("File okay")
            for timestamp, buf in pcap: 
                pack = dpkt.ethernet.Ethernet(buf) 
                packets.append(pack)  
                packet_ts.append(timestamp)
            return packets, packet_ts 
        """above code creates two lists one for the packets and one for the timestamps of the packets """
    except FileNotFoundError: 
        print(f"file {file_path} not found") 
        exit(0)