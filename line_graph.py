import matplotlib.pyplot as plt 
import numpy as np
"""function to create a line graph of how many packets are in a 15 second time interval"""
def line_graph(packet_ts): 
    start_of_interval = [] 
    num_packets = [] 
    interval = 15
    """set the first timestamp as the current start of the first interval(intervals are 15 seconds long)"""
    current_start = min(packet_ts) 
    while current_start < max(packet_ts): 
        """while statement makes sure that an out of range error will not appear"""
        interval_end = current_start + interval  
        """the end of each interval is the current start + 15 seconds"""
        interval_fill = [] 
        """list above is to find out how many packets are in each interval"""
        for ts in packet_ts: 
            """line below checks to see if the packet timestamp occurs before the end of the interval. If it does it is added to the list""" 
            if current_start <= ts < interval_end: 
                interval_fill.append(ts)  
        start_of_interval.append(current_start) 
        """puts the current start of the interval in a list of interval starts """ 
        num_packets.append(len(interval_fill))  
        """The number of packets in an interval is discovered by finding out the length of the interval_fill list  """
        current_start = interval_end  
        """The current start of the interval is changed to the end of the last interval"""
    mean = np.mean(num_packets) 
    standard_deviations = np.std(num_packets)  
    """calculate the mean and standard deviation of the number of packets in each interval"""
    threshold = mean + (2 * standard_deviations)   
    """calculate the thresehold for heavy traffic"""
    plt.plot(start_of_interval, num_packets)  
    """plot the graph using the start of interval list and the num_packets list"""
    plt.axhline(y = threshold, linestyle='--', label='exception for heavy traffic')  
    """creates a line in the graph to show the thresehold for heavy traffic"""
    plt.xlabel('Intervals') 
    plt.ylabel('number of packets')
    plt.title('number of packets over interval of 15 seconds') 
    plt.legend()  
    print("Line graph generated\n")
    plt.savefig('packet_count.png', format='png')
    plt.show() 
    plt.close()
    