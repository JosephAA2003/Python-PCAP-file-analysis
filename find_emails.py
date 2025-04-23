import dpkt 
import re

"""function to find out all emails in the to and from fields of certain packets"""
def find_emails(packets: list[dpkt.Packet]): 
    to_emails = [] 
    from_emails = []
    for pack in packets:  
        """regular expression to find email addresses that are in the TO field saves matches into a list """
        to_mail = re.findall(r'TO:.*?\<(.*?)\>', repr(pack.data))
        
        if to_mail:  
            if to_mail not in to_emails:
                to_emails.append(to_mail)
        """regular expression to find email addresses that are in the FROM field saves matches into a list """
        from_mail = re.findall(r'FROM:.*?\<(.*?)\>', repr(pack.data))

        if from_mail:  
            if from_mail not in from_emails:
                from_emails.append(from_mail)
    print("All emails found\n")
    print("Emails in the TO field: ") 
    for mail in to_emails: 
        print(mail)

    print("\n") 
    
    print("Emails in the FROM field: ")  
    
    for mail in from_emails: 
        print(mail)
    print("\n")