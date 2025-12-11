from core.utils import *
from core.ip import Ip
from core.output_string import *

IP_MASK_FORMAT = 'x.x.x.x'


def main():
    while True:
        ip_address = input(f"Enter an IP address in this format ({IP_MASK_FORMAT}): ")
        if Validation.ip_validate(ip_address):
            break
        else:
            print("Invalid ip address!!!")

    while True:
        subnet_mask = input(f"Enter the subnet mask in this format ({IP_MASK_FORMAT}): ")
        if Validation.mask_validate(subnet_mask):
            break
        else:
            print("Invalid subnet mask!!!")
    ip = Ip(ip_address, subnet_mask)
    with open(f"subnet_info_{ip_address}_313344376.txt", 'a') as f:
        f.write(format_input_ip(ip.get_ip_address_str()) +
                format_subnet_mask(ip.get_subnet_mask_str()) +
                format_classful_status(ip.get_ip_class()) +
                format_network_address(ip.get_network_address_str()) +
                format_broadcast_address(ip.get_broadcast_str()) +
                format_num_hosts(ip.calculate_number_of_hosts()) +
                format_cidr_mask(ip.get_cidr_mask()))


if __name__ == "__main__":
    main()
