import dpkt 
import re 
import os 
from prettytable import PrettyTable
"""function to find all the file directories of files sent. Also return the filename without the directory"""
def extract_urls(packets: list[dpkt.Packet]): 
    web_requests = []
    file_path = [] 
    remove = ['GET', 'HTTP']
    for pack in packets:  
        """regular expression to find any file directories in the packet"""
        url = re.search(r'GET (.+?\.((jpg)|(jpeg)|(gif)|(png)|(PNG)|(GIF)|(JPG)|(JPEG))) HTTP',repr(pack.data))

        if url:  
            """if a match is found add the drectory into a list """
            web_requests.append(url.group()) 
            
        else: 
            pass 
    for request in web_requests: 
        for word in remove:  
            """removes the words GET and HTTP from regex match and writes new string into list called file_path"""
            request = request.replace(word, '') 
        file_path.append(request) 
    print("URLs found\n")
    print("File Directories\n") 
    file_name = []
    for path in file_path:    
        """used os library to extract base filename"""    
        file_name.append(os.path.basename(path))  
    print("file names found\n") 
    """print file directory and filename as a table loop through two lists to fill it out """
    col_names = ['directory', 'file name']
    file_table = PrettyTable(col_names) 
    for i in zip(file_path, file_name): 
        
        file_table.add_row(i)  
    print(file_table)
    print("\n")