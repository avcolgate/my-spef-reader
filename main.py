import os.path
import sys
import re
from classes import *

path = "src/ext_patterns_default_accuracy_rc_coupled_last_PDK.spef"

METAL_NUM_1 = 3              # number in technology
METAL_INNER_NUM_1 = 3        # number in SPEF naming

METAL_NUM_2 = 4              # number in technology
METAL_INNER_NUM_2 = 2        # number in SPEF naming

first_metal = Metal(METAL_NUM_1, METAL_INNER_NUM_1)
second_metal = Metal(METAL_NUM_2, METAL_INNER_NUM_2)

def get_template(first_metal: str, second_metal: str):
    return f"\*\d+ DU6_M{first_metal}uuM{second_metal}_W320W320_S\d\d\d\d\dS\d\d\d\d\d_\d"

def main():
    nets = list()
    is_d_net_section = False
    is_cap_section = False

    with open(file=path, mode='rt') as file:
        lines = file.read().split('\n')
        for line_num, line in enumerate(lines):
            if re.findall(get_template(first_metal=first_metal.num, second_metal=second_metal.num), line):
                alias, name = line.split()
                distance = int(name.split('_')[3].split('S')[1])
                net = Net(name, alias, distance)
                nets.append(net)
            if line.startswith("*PORTS"):
                break

        for net in nets:
            for line_num, line in enumerate(lines):
                if line.startswith(f"*D_NET {net.alias} ") and not is_d_net_section:
                    is_d_net_section = True
                    total = line.split(' ')[2]
                if line.startswith("*RES") and is_d_net_section:
                    is_d_net_section = False
                    is_cap_section = False
                    net.capacitance = Cap(float(total)*1000, float(cap1)*1000, float(cap2)*1000, float(cc)*1000)
                    total = 0
                    cap1 = 0
                    cap2 = 0
                    cc = 0
                    break
                if line.startswith("*CAP") and is_d_net_section:
                    is_cap_section = True
                if line.startswith("1") and is_cap_section:
                    cap1 = line.split(' ')[2]
                if line.startswith("2") and is_cap_section:
                    cap2 = line.split(' ')[2]
                if line.startswith("3") and is_cap_section:
                    cc = line.split(' ')[3]    
                    
            # net.disp_info()

    second_metal.disp_nets(net_list=nets)

    file.close()

if __name__ == "__main__":
    main()
