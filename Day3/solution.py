'''
Created on Dec 3, 2022

@author: cmg1229
'''


LOWER_VALUE = 96
UPPER_VALUE = 38

def get_priority(c):
    '''
    Returns the priority of the character in question
    '''
    if c.isupper():
        return ord(c) - UPPER_VALUE
    else:
        return ord(c) - LOWER_VALUE


class Rucksack():
    '''
    Contains the contents of a single rucksack
    @param istring(str): line from input file
    @property stotal(str): Total Sack Contents
    @property s1(str): Contents of Compartment One
    @property s2(str): Contents of Compartment Two
    @property commons(list): Common Contents between the 2 compartments
    '''
    def __init__(self, istring):
        half = int(len(istring) / 2)
        self.stotal = istring
        self.s1 = istring[0:half]
        self.s2 = istring[half:]
        self.commons = []
        for i in self.s1:
            if i in self.s2 and i not in self.commons:
                self.commons.append(i)
    
    def get_total_common_priority(self):
        '''
        Returns the summed priorities of all of the common contents
        of the rucksack
        @return int
        '''
        total = 0
        for i in self.commons:
            total += get_priority(i)
        return total


class Group():
    '''
    Contains a list of three rucksacks, defines a badge and priority 
    between them.
    @property sacks(list:Rucksacks)
    @property badge(char): Common content among all three rucksacks (None until find_badge is called
    @property priority(int): Priority of the badge above (0 until find_badge is called)
    '''
    def __init__(self):
        self.sacks = []
        self.badge = None
        self.priority = 0
        
    def add_sack(self, sack:Rucksack):
        self.sacks.append(sack)
        
    def find_badge(self):
        s1 = self.sacks[0].stotal
        s2 = self.sacks[1].stotal
        s3 = self.sacks[2].stotal
        for i in s1:
            if i in s2 and i in s3:
                self.badge = i
                self.priority = get_priority(i)
    

def parse_input(input_file = 'input.txt'):
    '''
    Parses the input file and returns a list of Rucksacks as well as a
    list of groups
    @param input_file(str): Location of the input file, default is input.txt
    @return sacks(list): List of Rucksacks
    @return groups(list): List of Groups
    '''
    sacks = []
    groups = []
    with open(input_file) as ifile:
        i = 0
        group = Group()
        for line in ifile.readlines():
            sack = Rucksack(line.strip())
            sacks.append(sack)
            group.add_sack(sack)
            i = i+1
            if i % 3 == 0:
                groups.append(group)
                group = Group()
    return sacks, groups

def p1_solve(sacks:list):
    grand_total_priority = 0
    for sack in sacks:
        grand_total_priority += sack.get_total_common_priority()
    print('P1 Solution: {0}'.format(grand_total_priority))

def p2_solve(groups:list):
    total_group_priority = 0
    for g in groups:
        g.find_badge()
        total_group_priority += g.priority
    print('P2 Solution: {0}'.format(total_group_priority))

if __name__ == '__main__':
    sacks, groups = parse_input()
    p1_solve(sacks)
    p2_solve(groups)
        
        
        