# validate ip - ipv4 or ipv6
class Sol(object):
    def validIPAddress(self, ip):
        """
        :type IP: str
        :rtype: str
        """
        def is_ipv4(ip):
            # 5 conditions -1. have 3 dots. 2. if 0 exists and preceeds digit, false, 3. less than 256 4. no alphabet
            splits = ip.split('.')
            if len(splits) != 4:
                return False
            for i in splits:
                if len(i) == 0:
                    return False
                if i.isdigit() == False:
                    return False
                if int(i) < 0 or int(i) > 255:
                    return False
                if int(i[0]) == 0 and len(i) > 1:
                    return False
            return True

        def is_ipv6(ip):
            # 3 condititions: 1. len of splits is 8. 2. has 4 hex digits but can have 0 3. only hex
            splits = ip.split(':')
            if len(splits) != 8:
                return False
            for i in splits:
                if len(i) > 4 or len(i) < 1:
                    return False
                for char in i:
                    if char not in string.hexdigits:
                        return False
            return True
        if is_ipv4(ip):
            return 'IPv4'
        if is_ipv6(ip):
            return 'IPv6'
        return 'Neither'
        
