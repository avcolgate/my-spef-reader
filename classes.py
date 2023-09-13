from typing import List

class Net:
    def __init__(self, name: str='', alias: str='', distance: int=-1):
        self.name = name
        self.alias = alias
        self.distance = distance
        self.capacitance = Cap()
    
    def disp_info(self):
        print(f"alias:\t{self.alias}\nname:\t{self.name}\ndist:\t{self.distance}\ntotal:\t{self.capacitance.total}\ncap1:\t{self.capacitance.cap1}\ncap2:\t{self.capacitance.cap2}\ncc:\t{self.capacitance.cc}\n\n")

class Cap:
    def __init__(self, total: float=-1, cap1: float=-1, cap2: float=-1, cc:float = -1):
        self.total = round(total, 5)
        self.cap1 =  round(cap1,  5)
        self.cap2 =  round(cap2,  5)
        self.cc =    round(cc,    5)

class Metal:
    def __init__(self, num: int, inner_num: int) -> None:
        self.num = num
        self.inner_num = inner_num

    def disp_nets(self, net_list: List[Net()]):
        for net in net_list:
            if int(net.name[-1]) == self.inner_num:
                print(f"metal{self.num}\n{net.alias}\n \
                    net:\t{net.name}\n \
                    dist:\t{net.distance}\n \
                    total:\t{net.capacitance.total}\n \
                    cap1:\t{net.capacitance.cap1}\n \
                    cap2:\t{net.capacitance.cap2}\n \
                    cc:\t{net.capacitance.cc}\n")
