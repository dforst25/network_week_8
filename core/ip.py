from .utils import BinaryConverter
from functools import reduce


class Ip:
    def __init__(self, ip_address: str | None = None, mask: str | None = None):
        if ip_address:
            self.set_ip_address(ip_address)
        else:
            self.octet_list: list[int] | None = ip_address

        if mask:
            self.set_mask(mask)
        else:
            self.subnet_mask_list: list[int] | None = mask

    def set_ip_address(self, ip_address: str):
        self.octet_list = list(map(int, ip_address.split('.')))

    def set_mask(self, mask: str):
        self.subnet_mask_list = list(map(int, mask.split('.')))

    def get_ip_address_str(self) -> str | None:
        if self.octet_list is None:
            return None
        else:
            return '.'.join(map(str, self.octet_list))

    def get_subnet_mask_str(self) -> str | None:
        if self.subnet_mask_list is None:
            return None
        else:
            return '.'.join(map(str, self.subnet_mask_list))

    def get_network_address_str(self) -> str | None:
        if self.octet_list is None or self.subnet_mask_list is None:
            return None
        network_list = [self.octet_list[i] & self.subnet_mask_list[i] for i in range(4)]
        return '.'.join(map(str, network_list))

    def get_broadcast_str(self) -> str | None:
        if self.octet_list is None or self.subnet_mask_list is None:
            return None
        broadcast_list = [self.octet_list[i] | (~self.subnet_mask_list[i]) & 0xFF for i in range(4)]
        return '.'.join(map(str, broadcast_list))

    def get_cidr_mask(self) -> int | None:
        if self.octet_list is None or self.subnet_mask_list is None:
            return None
        # for example binary_mask = '11111111'+'11111000'+'00000000'+'00000000'
        binary_mask = reduce(lambda x1, x2: x1 + BinaryConverter.decimal_to_binary(x2, 8), self.subnet_mask_list, '')
        return binary_mask.count('1')

    def calculate_number_of_hosts(self) -> int | None:
        if self.octet_list is None or self.subnet_mask_list is None:
            return None
        power = 32 - self.get_cidr_mask()
        return 2 ** power - 2

    def get_ip_class(self) -> str | None:
        if self.octet_list is None or self.subnet_mask_list is None:
            return None
        cidr = self.get_cidr_mask()
        match cidr:
            case 8:
                if self.octet_list[0] < 128:
                    return "Class A"
                else:
                    return "Classless"
            case 16:
                if 128 <= self.octet_list[0] < 192:
                    return "Class B"
                else:
                    return "Classless"
            case 24:
                if 192 <= self.octet_list[0] < 224:
                    return "Class C"
                else:
                    return "Classless"
            case _:
                return "Classless"
