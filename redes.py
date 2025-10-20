class IPAddress: #IMCOMPLETO
    def __init__(self, Ipv4:str, mascara:str):
        self.Ipv4 = Ipv4
        self.mascara = mascara

    def converter_bit(self):
        #para converter o string em inteiro

    def set_ip(self, Ipv4):
        self.ip_bit = list(map(int, self.Ipv4.split('.')))        
        if self.Ipv4 < 0 or self.Ipv4 > 255:
            raise ValueError("Erro: IP inválido")
        else:
            self.Ipv4 = Ipv4

    def set_mascara(self, mascara):
        self.converter_bit() #analisar sobre essa parte
        if self.mascara < 0 or self.mascara > 255:
            raise ValueError("Erro: Máscara inválida")
        else:
            self.mascara = mascara

    def calc_bit(self):
        self.converter_bit()
        self.rede_bit = [self.ip_bit[i] & self.mask_bit[i] for i in range(4)] #analisar sobre essa parte
        self.rede = '.'.join(map(str, self.rede_bit))
        return self.rede

    def get_ip(self):
        return self.Ipv4

    def get_mascara(self):
        return self.mascara


    def pertence_a_rede(self, IP):
        self.endereco = str(print(input()))


        if self.endereco == self.Ipv4: #analisar sobre essa parte
            return True
        return False

    def __str__(self):#analisar sobre essa parte
        return f""

ip = IPAddress()



