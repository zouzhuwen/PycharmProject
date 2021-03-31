#coding=utf-8

def function(array):
    list = array
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j] < list[j+1]:
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp

    return list




if __name__ == '__main__':
      array = [2,1,35,5,44,66,22,3]
      print(len(array))
      list = function(array)
      print(list)