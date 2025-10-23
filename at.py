class IPAddress: #RESPOSTA FINAL
    def __init__(self, Ipv4, mascara):
        self.Ipv4 = Ipv4
        self.mascara = mascara
        self.xor_universal = 4294967295

    def set_ip(self):
        self.ip_bit = list(map(int, self.Ipv4.split('.')))
        for i in range(4):      
            if self.ip_bit[i] < 0 or self.ip_bit[i] > 255:
                raise ValueError("Erro: IP inválido")
        return self.ip_bit 

    def set_mascara(self):
        self.mask_bit = list(map(int, self.mascara.split('.'))) 
        for i in range(4):
            if self.mask_bit[i] in (255, 254, 252, 248, 240, 224, 192, 128, 0):
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
            self.binario_ip.append(format(octeto, '08b'))
        self.verdadeiromask = ''.join(self.binario_ip)
        return self.verdadeiromask

    def calc_conversor_bitmask(self):
        self.verdadeiromask = []
        for octeto in self.mask_bit:
            self.verdadeiromask.append(format(octeto, '08b'))
        return ''.join(self.verdadeiromask)

    def calc_conversor_bitxor(self):
        self.xor_bit_universal = []
        for octeto in self.xor_vai: 
            self.xor_bit_universal.append(format(octeto, '08b'))
        return ''.join(self.xor_bit_universal)

    def calc_cidr(self):
        self.cidr = 0
        mask_bin = self.calc_conversor_bitmask()
        for bit in mask_bin:
            if bit == '1':
                self.cidr += 1
        return self.cidr

    def calc_xor_mask(self):
        self.xor_mask = []  
        self.xor_mask.append(self.calc_conversor_bitxor())
        self.xor_mask.append(self.calc_conversor_bitmask())
        return self.xor_mask

    def calc_rede(self):
        self.rede = []
        for i in range(4):
            self.rede.append(self.ip_bit[i] & self.mask_bit[i])
        return self.rede

    def calc_broadcast(self): 
        self.broadcast = []
        for i in range(4):
            self.broadcast.append(self.ip_bit[i] | (255 - self.mask_bit[i]))
        return self.broadcast

    def calc_conversor_decimal_rede(self):
        self.rede_decimal = []
        for octeto in self.calc_rede():
            self.rede_decimal.append(str(octeto))
        return '.'.join(self.rede_decimal) 

    def calc_conversor_decimal_broadcast(self):
        self.broadcast_decimal = []
        for octeto in self.calc_broadcast(): 
            self.broadcast_decimal.append(str(octeto))
        return '.'.join(self.broadcast_decimal)

    def __str__(self):
        return f"{self.Ipv4}/{self.calc_cidr()}"  

    def verificar(self):
        ip_novo = input('Digite um IP para verificar: ')
        self.ip_novo_bit = list(map(int, ip_novo.split('.')))
        rede = self.calc_rede()
        broadcast = self.calc_broadcast()
        for i in range(4):
            if self.ip_novo_bit[i] <= rede[i] or self.ip_novo_bit[i] >= broadcast[i]:
                return 'IP inválido para a rede'
        return 'IP válido para a rede'


class UI: 
    def menu(): 
        ip = IPAddress(input('Digite o IP: '), input('Digite a máscara: ')) 
        ip.set_ip()
        ip.set_mascara()
        ip.set_xor()

        print(ip)

        print(ip.calc_conversor_decimal_broadcast())
        print(ip.calc_conversor_decimal_rede()) 

        print(ip.verificar())
        print(ip.verificar()) 

UI.menu()

