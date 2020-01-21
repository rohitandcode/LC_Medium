class Codec:
    def __init__(self):
        self.dicto = {}
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        v = 0
        v += 1
        if longUrl not in self.dicto.values():
            self.dicto[v] = longUrl
            return v
        else:
            for key, val in self.dicto():
                if val == longUrl:
                    return key
        
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        if shortUrl in self.dicto:
            return self.dicto[shortUrl]
        else:
            return None
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
