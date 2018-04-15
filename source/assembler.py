
class Assembler(object):
  
    dec_to_const = lambda value: twos_complement(value)
    dec_to_rs = lambda value: decimal_to_rs(value)
    dec_to_addr = lambda value: decimal_to_addr(value)

    instruction_set = \
        dict([('load',    [2, '00000', '0', dec_to_addr]),
              ('loadi',   [2, '00000', '1', dec_to_const]),
              ('store',   [2, '00001', '1', dec_to_addr]),
              ('add',     [2, '00010', '0', dec_to_rs]),
              ('addi',    [2, '00010', '1', dec_to_const]),
              ('addc',    [2, '00011', '0', dec_to_rs]),
              ('addci',   [2, '00011', '1', dec_to_const]),
              ('sub',     [2, '00100', '0', dec_to_rs]),
              ('subi',    [2, '00100', '1', dec_to_const]),
              ('subc',    [2, '00101', '1', dec_to_rs]),
              ('subci',   [2, '00101', '1', dec_to_const]),
              ('and',     [2, '00110', '0', dec_to_rs]),
              ('andi',    [2, '00110', '1', dec_to_const]),
              ('xor',     [2, '00111', '0', dec_to_rs]),
              ('compl',   [1, '01000', '0', dec_to_rs]),
              ('shl',     [1, '01001', '0', dec_to_rs]),
              ('shla',    [1, '01010', '0']),
              ('shr',     [1, '01011', '0']),
              ('shra',    [1, '01100', '0']),
              ('compr',   [2, '01101', '0']),
              ('compri',  [2, '01101', '1']),
              ('getstat', [1, '01110', '0']),
              ('putstat', [1, '01111', '0']),
              ('jump',    [1, '10000', '1', dec_to_addr]),
              ('jumpl',   [1, '10001', '1', dec_to_addr]),
              ('jumpe',   [1, '10010', '1', dec_to_addr]),
              ('jumpg',   [1, '10011', '1', dec_to_addr]),
              ('call',    [1, '10100', '1', dec_to_addr]),
              ('return',  [0, '1010100000000000']),
              ('read',    [1, '10110', '0']),
              ('write',   [1, '10111', '0']),
              ('halt',    [0, '1100000000000000']),
              ('noop',    [0, '1100100000000000'])])

    def __init__(self, source_name, destination_name):
        self.assembly_program = open(source_name, 'r')
        self.object_program = open(destination_name, 'w')
        return

    def parse_assembly(self):

        for line in self.assembly_program:

            assembly_parse = line.split(" ")
            assembly_parse[0] = assembly_parse[0].replace("\n", "")

            inst_template = self.instruction_set[assembly_parse[0]]

            if inst_template[0] == 0:

                object_program_line = str(int(inst_template[1], 2)) + "\n"

            elif inst_template[0] == 1:

                if inst_template[2] == "0":

                    object_binary = inst_template[1] + \
                                    decimal_to_rd(assembly_parse[1]) + \
                                    inst_template[2] + "00000000"

                    object_program_line = str(int(object_binary, 2)) + "\n"

                else:

                    object_binary = inst_template[1] + \
                                    "00" + inst_template[2] + \
                                    inst_template[3](assembly_parse[1])

                    object_program_line = str(int(object_binary, 2)) + "\n"

            else:

                object_binary = inst_template[1] + \
                                decimal_to_rd(assembly_parse[1]) + \
                                inst_template[2] + \
                                inst_template[3](assembly_parse[2])

                object_program_line = str(int(object_binary, 2)) + "\n"

            self.object_program.write(object_program_line)


def twos_complement(value):
    value = int(value)
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


def decimal_to_rd(value):
    return bin(int(value))[2:].rjust(2, "0")


def decimal_to_rs(value):
    return bin(int(value))[2:].ljust(8, "0")


def decimal_to_addr(value):
    return bin(int(value))[2:].rjust(8, "0")
