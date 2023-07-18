# This program reads a file and print the content

v_file = open('enquiry.csv','rt')

def state_check(xline, state):
    if xline[0:2] == state:
       print(xline)

def get_code(xline, state):
    if xline[0:2] == state:
       c = xline[8:12]
       return c

v_reg_num = []
v_enquiry = []
i=0
for eachline in v_file:
    #state_check(eachline, 'KA')
    #state_check(eachline, 'TN')
    # if eachline[0:4] == 'KA01':
    #    print(eachline)
    #c = get_code(eachline, 'TN')
    #v_reg_num.append(c)
    
    i=i+1
    if i == 2:
        print(eachline)
        v_enquiry = eachline
        break

# for x in v_reg_num:
#     print(x)

for x in v_enquiry:
    print(x)

# v_reg_num.sort()
# print(v_reg_num)


j=0
with open('enquiry.csv', 'r') as file:
    array = file.readlines()
    array = [row.split(',') for row in array]
    print(array)
    j-j+1;
    print(j)

j=0
print("**********************")
for xrow in array:
  #print(xrow)
  j=j+1;
  print(j)
 # if j==2:
  for x in xrow:
    print(x)
  print(xrow[5])
 #  break