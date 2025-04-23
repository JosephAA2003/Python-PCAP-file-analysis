import readparse
import packet_table
import packet_ips 
import find_emails 
import extract_urls 
import network_graph 
import line_graph   

def main(): 
    """main function to process packets"""   
    """have a list for the packets themselves and the timestamps for each packets which are needed for the packet_table and line_graph function"""
    packets = []
    file_name = "evidence-packet-analysis.pcap" 
    packet_ts = []
    packets, packet_ts = readparse.readparse(file_name) 
    packet_table.packet_table(packets, packet_ts) 
    packet_ips.packet_ips(packets)  
    find_emails.find_emails(packets)
    extract_urls.extract_urls(packets)
    network_graph.network_graph(packets)
    line_graph.line_graph(packet_ts)


if __name__ == "__main__": 
    main()










        


    
    
        


