OCTET_MASK_OPTIONS = {0, 128, 192, 224, 240, 252, 254, 255}


class BinaryConverter:
    @staticmethod
    def decimal_to_binary(dec_num: int, length: int = 8) -> str:
        if dec_num < 0:
            raise ValueError("Not support negative numbers!!!")
        max_num = 2 ** length - 1
        if dec_num > max_num:
            raise AttributeError(f"Can't represent {dec_num} in {length} bits")
        binary = ""
        for i in range(length)[::-1]:
            if dec_num >= 2 ** i:
                binary += "1"
                dec_num -= 2 ** i
            else:
                binary += "0"
        return binary


class Validation:
    @staticmethod
    def mask_validate(mask: str) -> bool:
        subnet_mask_list = list(map(int, mask.split('.')))
        if len(subnet_mask_list) != 4:
            return False
        # check each octet
        is_zero_next_octet = False
        for octet in subnet_mask_list:
            if is_zero_next_octet and octet != 0:
                return False
            elif octet not in OCTET_MASK_OPTIONS:  # make shore 1*0* in bits
                return False
            elif octet != 255:
                is_zero_next_octet = True
        return True

    @staticmethod
    def ip_validate(ip: str) -> bool:
        octet_list = list(map(int, ip.split('.')))
        if len(octet_list) != 4:
            return False
        # check each octet
        return all(map(lambda x: 0 <= x <= 255, octet_list))
