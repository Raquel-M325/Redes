class IPAddress:
    def __init__(self, Ipv4, mascara):
        self.Ipv4 = Ipv4
        self.mascara = mascara
        self.xor_universal = 4294967295

    def set_ip(self):
        self.ip_bit = list(map(int, self.Ipv4.split('.')))
        for i in range(4):      
            if self.Ipv4 < 0 or self.Ipv4 > 255:
                raise ValueError("Erro: IP inválido")
        return self.ip_bit 

    def set_mascara(self):
        self.mask_bit = list(map(int, self.mascara.split('.'))) 
        for i in range(4):
            if self.mask_bit[i] == 255 or self.mask_bit[i] == 254 or self.mask_bit[i] == 252 or self.mask_bit[i] == 248 or self.mask_bit[i] == 240 or self.mask_bit[i] == 224 or self.mask_bit[i] == 192 or self.mask_bit[i] == 128 or self.mask_bit[i] == 0:
                continue
            else:
                raise ValueError("Erro: Máscara inválida")
        return self.mascara

    def set_xor(self):
        self.xor_vai = list(map(int, self.Ipv4.split('.')))
        return self.xor_vai

    def get_ip(self):
        return self.Ipv4

    def get_mascara(self):
        return self.mascara
        
    def get_xor(self):
        return self.xor_vai

    def calc_conversor_bitip(self):
        self.binario_ip = []
        for octeto in self.ip_bit:
            self.binario_ip.append(bin(octeto))

        for b in self.binario_ip:
            self.verdadeiromask = format(binario_ip, '08b') #correção
        return self.verdadeiromask

    def calc_conversor_bitmask(self):
        self.verdadeiromask = []
        for octeto in self.mask_bit:
            self.verdadeiromask.append(bin(octeto))
        
        for b in self.verdadeiromask:        
            self.verdadeiromask = format(verdadeiromask, '08b') #correção
        return self.verdadeiromask

    def calc_conversor_bitxor(self):
        self.xor_bit_universal = []
        for octeto in self.xor_vai: 
            self.xor_bit_universal.append(bin(octeto))  

        for b in self.xor_bit_universal:        
            self.xor_bit_universal = format(self.xor_bit_universal, '08b') #correção  
        return self.xor_bit_universal   

    def calc_cidr(self):
        self.cidr = 0
        for i in range(len(self.mascara)):
            if self.mascara[i] == 1:
                self.cidr += 1
            else:
                self.cidr += 0
        return self.cidr

    def calc_xor_mask(self):
        self.xor.mask = []  
        return self.xor_mask.append(self.calc_conversor_bitxor() ^ self.calc_conversor_bitmask()) 

    def calc_rede(self):
        self.rede = []
        return self.rede.append(self.Ipv4 & self.calc_conversor_bitxor())

    def calc_broadcast(self): 
        self.broadcast = []
        return self.broadcast.append(self.Ipv4 | self.calc_conversor_bitxor())


    def calc_conversor_decimal_rede(self):
        self.rede_decimal = []
        for octeto in self.rede:
            self.rede_decimal.append(int(octeto, 2))
        return self.rede_decimal.split('.') 

    def calc_conversor_decimal_broadcast(self):
        self.broadcast_decimal = []
        for octeto in self.calc_broadcast(): 
            self.broadcast_decimal.append(int(octeto, 2))
        return self.broadcast_decimal.split('.')

    def __str__(self):
        return f"{self.Ipv4}/{self.calc_cidr()}"  

    def verificar(self, UI):
        self.ip_novo_bit = UI.set_ip_novo()
        if self.ip_novo_bit <= self.rede_decimal or self.ip_novo_bit >= self.broadcast_decimal:
            return 'IP inválido para a rede'
        return 'IP válido para a rede'

class UI: 
    def menu(): 
        ip = IPAddress(input('Digite o IP: '), input('Digite a máscara: ')) 
        print(ip)

        print(ip.calc_conversor_decimal_broadcast())
        print(ip.calc_conversor_decimal_rede()) 

        print(ip.verificar())
        print(ip.verificar()) 

UI.menu() 



