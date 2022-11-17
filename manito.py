import random


def main():
    name_list = ['A','B','C','D','E']
    result = []

    total_list = []

    for i in range(len(name_list)):
        temp = random.randrange(0,len(name_list))

        while i == temp or temp in result:
            temp = random.randrange(0,len(name_list))

            if i == len(name_list) - 1 and i not in result:
                return True, total_list

        result.append(temp)

        ins_list = [name_list[i], name_list[result[i]]]

        total_list.append(ins_list)

    return False, total_list

  
if __name__ == '__main__':
  n = True

  while n:
      n, total_list = main()

  print(total_list)
