"""
f = lambda value: twos_complement(value)
instruction_set = dict([('noop', [1, '11001', '0', f]),
                        ('poop', [1, '11001', '0', f])])

def twos_complement(value):
    if value >= 0 & value <= 127:
        complement = format(value, 'b').rjust(8, "0")

    elif value <= 0 & value >= -128:
        complement = format(value, 'b').rjust(8, "0")
        for x in range(8):
            if complement[x] == "1":
                complement = complement[:x] + "0" + complement[x + 1:]
            else:
                complement = complement[:x] + "1" + complement[x + 1:]
        complement = format(int(complement, 2) + 1, 'b')
    else:
        complement = "OUT OF RANGE"
        print("out of range!")

    return complement


print(instruction_set['noop'][3](10))
"""

from source.assembler import Assembler
from source.assembler import twos_complement

basictest = Assembler("test1.s", "out1.o")
basictest.parse_assembly()

"""print("1111111111111111111111\n" + twos_complement(69) +"\n")
print(bin(69))
"""