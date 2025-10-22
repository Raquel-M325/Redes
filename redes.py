class IPAddress:
    def __init__(self, Ipv4:str, mascara:str):
        self.Ipv4 = Ipv4
        self.mascara = mascara

    def converter_bit(self):
        #para converter o string em inteiro
        pass

    def set_ip(self, Ipv4):
        self.ip_bit = list(map(int, self.Ipv4.split('.')))      
        if self.Ipv4 < 0 or self.Ipv4 > 255:
            raise ValueError("Erro: IP inválido")
        else:
            self.Ipv4 = Ipv4

    def set_mascara(self, mascara):
        self.mask_bit = list(map(int, self.mascara.split('.'))) 
        if self.mascara < 0 or self.mascara > 255:
            raise ValueError("Erro: Máscara inválida")
        else:
            self.mascara = mascara

    def conversor_bitip(self):
        self.binario_ip = []
        for octeto in self.ip_bit:
            self.binario_ip.append(bin(octeto))

        for b in self.binario_ip:
            self.verdadeiromask = format(binario_ip, '08b')
        return self.verdadeiromask

    def conversor_bitmask(self):
        self.verdadeiromask = []
        for octeto in self.mask_bit:
            self.binario_mask.append(bin(octeto))
        
        for b in self.verdadeiromask:        
            self.verdadeiromask = format(binario_mask, '08b')
        return self.verdadeiromask


    def get_ip(self):
        return self.Ipv4

    def get_mascara(self):
        return self.mascara

    def pertence_a_rede(self, IP):
        self.endereco = str(print(input()))

        if self.endereco == self.Ipv4: #analisar sobre essa parte
            return True
        return False

    def __str__(self): # analisar sobre essa parte
        return f""

ip = IPAddress()
