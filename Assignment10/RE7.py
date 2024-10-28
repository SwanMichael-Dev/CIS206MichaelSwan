import re

def remove_leading_zeros(ip_address):
  
    cleaned_ip_address = re.sub(r'\b(0+)(\d)', r'\2', ip_address)
    return cleaned_ip_address


ip_address = "216.08.094.196"
cleaned_ip_address = remove_leading_zeros(ip_address)
print(cleaned_ip_address)
