from prettytable import PrettyTable
import dpkt
import re

"""function to find out all the protocols used in the packets, how many occurences per protocol, the first and last timestamp of each protocol and the average packet length for each protocol"""
def packet_table(packets: list[dpkt.Packet],packet_ts): 
    col_names = ["Protocol", "amount", "avg len", "first TS", "last TS"] 
    protocol_list = [] 
    protocol_count = [] 
    protocol_length = [] 
    protocol_avg_length = []     
    """lists that hold the details for each field in the table""" 
    protocol_first_ts = [] 
    protocol_last_ts = []
    ts_index = 0 
    count = 0
    for pack in packets:      
        """regular expresson searches for the protocol in the packet by looking at the characters after data="""   
        protocol = re.search(r'data=(.*?)(?=\()', repr(pack.data)).group(1) 
        """removes any non alpha numeric characters from protocol name"""
        protocol_alpha = "".join(c for c in protocol if c.isalnum()) 
        if protocol_alpha not in protocol_list:  
            """if the protocol is not in the list it appends the list with the protocol name and also appends the other lists """
            protocol_list.append(protocol_alpha) 
            protocol_count.append(0) 
            protocol_length.append(0) 
            protocol_avg_length.append(0)  
            protocol_first_ts.append(0) 
            protocol_last_ts.append(0)
            index = protocol_list.index(protocol_alpha)  
            """modifies the other lists by using the index of the protocol name since all fields for that protocol will be at the same index in their respective lists"""
            protocol_count[index] = protocol_count[index] + 1
            protocol_length[index] = protocol_length[index] + len(repr(pack)) 
            protocol_first_ts[index] = packet_ts[ts_index] 
            protocol_last_ts[index] = packet_ts[ts_index]
        else:  
            """if protocol is already in the list then see above doc string"""
            index = protocol_list.index(protocol_alpha) 
            protocol_count[index] = protocol_count[index] + 1
            protocol_length[index] = protocol_length[index] + len(repr(pack)) 
            protocol_last_ts[index] = packet_ts[ts_index]
        ts_index = ts_index + 1  
        """uses the packet timestamps list to determine the first and last timestamp of the packet. Since the packet list and timestamp list are the same length just create a variable called ts_index and increment it by one when it loops through a different packet """
        count = count + 1       
    print("Packets processed by protocol, number of occurences and first and last timestamp\n")
    for proc in protocol_list: 
        index = protocol_list.index(proc) 
        protocol_avg_length[index] = protocol_length[index] / protocol_count[index] 
    print("Average length per protocol calculated\n")
    table = PrettyTable(col_names) 
    for proc in zip(protocol_list, protocol_count, protocol_avg_length, protocol_first_ts, protocol_last_ts): 
        table.add_row(proc)  
    print(table) 
    print("\n")
    