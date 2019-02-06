file = open("running-config.cfg","r")

def mylist(fin):
  list1 = []
  list2 = []
  list3 = []
  for line in fin:
    if "access-list" in line:
      if "transit_access_in" in line:
        list1.append(line)
  
      elif "fw-management_access_in" in line:
        list2.append(line)
  
      else:
        "global_access" in line
        list3.append(line)
 
  print(list1)
  print(list2)
  print(list3)

(mylist(file)) 
