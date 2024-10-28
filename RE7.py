def remove_leading_zeros(ip_address):
  return ".".join([str(int(octet)) for octet in ip_address.split(".")])


ip_address = "216.08.094.196"
print(remove_leading_zeros(ip_address))