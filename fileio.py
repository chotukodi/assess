# This program reads a file and print the content

v_file = open('data.txt','rt')

def state_check(xline, state):
    if xline[0:2] == state:
       print(xline)

def get_code(xline, state):
    if xline[0:2] == state:
       c = xline[8:12]
       return c

v_reg_num = []

for eachline in v_file:
    #state_check(eachline, 'KA')
    #state_check(eachline, 'TN')
    # if eachline[0:4] == 'KA01':
    #    print(eachline)
    c = get_code(eachline, 'TN')
    v_reg_num.append(c)
    #print(c)

for x in v_reg_num:
    print(x)

v_reg_num.sort()
print(v_reg_num)