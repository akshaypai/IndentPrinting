import os
def full_print (my_list,numb=0):
  for each_item in my_list:
    if isinstance(each_item,list):
      full_print(each_item,numb+1)
    else:
                        for num in range(numb):
                                print("\t", end='')
                        print(each_item)
