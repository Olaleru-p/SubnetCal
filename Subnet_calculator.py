import ipaddress

# Function to determine IP Class
def get_ip_class(ip):
    "Determine the class of an IPv4 address using its first octet."
    first_octet = int(str(ip).split(".")[0])
    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 254:
        return "Class E (Experimental)"
    else:
        return "Invalid IP or Reserved IP"
    

# Function to return default subnet if /prefix is missing
def get_default_prefix(ip):
    """Assign default subnet mask prefix if user does not enter one."""
    ip_class = get_ip_class(ip)

    if ip_class == "Class A":
        return 8
    elif ip_class == "Class B":
        return 16
    elif ip_class == "Class C":
        return 24
    else:
        return 24
    

# Main subnet calculator logic
def subnet_calculator(ip_with_prefix):
    try:
        # If user didn’t add a /prefix;  add default prefix based on IP class
        if "/" not in ip_with_prefix:
            ip_only = ip_with_prefix.strip()
            prefix = get_default_prefix(ip_only)
            ip_with_prefix = f"{ip_only}/{prefix}"

        # Convert to IP network object
        network = ipaddress.ip_network(ip_with_prefix, strict=False)

        # Get IP class
        ip_class = get_ip_class(network.network_address)

        #Display subnet details
        print("\n")
        print(f" Input: {ip_with_prefix}")
        print("\n")
        print(f" IP Class          : {ip_class}")
        print(f" Network Address   : {network.network_address}")
        print(f" Broadcast Address : {network.broadcast_address}")
        valid_hosts = max(network.num_addresses - 2, 0)
        print(f" Valid Hosts       : {valid_hosts}")
        print(f" Wildcard Mask     : {ipaddress.IPv4Address(int(network.hostmask))}")
        print(f" CIDR Notation     : /{network.prefixlen}")
        print("\n")
                    
        return True  
    
    except ValueError as e:
        print(f" Invalid input '{ip_with_prefix}': {e}\n")
        return False 


# MAIN PROGRAM
def main():
    print("\n Subnet Calculator \n")

    while True:
        while True:
            u_input = input(" Enter an IP Address: ")

            if not u_input.strip():
                print("No input provided. Please try again.\n")
                continue

            if subnet_calculator(u_input):
                break

        again = input("Do you want to calculate another subnet? (yes/no): ").lower()
        if again != "yes":
            print("\n Thank you.\n")
            break


if __name__ == "__main__":
    main()
