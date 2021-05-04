import copy

def men_4(x):

  men_pend = []
  
  if sum(x) % 3 != 0:
    return 0
  
  while x != []:
    try:
      y = x[0]
      if x.count(y) == 2:
        for i in range(2):
          men_pend.append([y, y + 1, y + 2])
          x.remove(y)
          x.remove(y + 1)
          x.remove(y + 2)
      elif x.count(y) == 1:
        men_pend.append([y, y + 1, y + 2])
        x.remove(y)
        x.remove(y + 1)
        x.remove(y + 2)
      elif x.count(y) >= 3:
        men_pend.append([y] * 3)
        for i in range(3):
          x.remove(y)
    except:
      return 0

  return len(men_pend)

def is_hora(te_hai):
  
  toi = []
  men = []
  pend = []
  
  te_hai.sort()
 
  if set(te_hai) == {"1m", "9m", "1p", "9p", "1s", "9s", "中", "北", "南", "東", "發", "白", "西"}:
  	return "国士無双形"
 
  if len(set(te_hai)) == 7:
    for i in range(7):
      if te_hai[2 * i] != te_hai[2 * i + 1]:
        break
    else:
      return "七対子or二盃口形"
 
  num_hai = []
  ji_hai = []
  for i in range(14):
    if len(te_hai[i]) == 2:
      num_hai.append(te_hai[i])
    else:
      ji_hai.append(te_hai[i])

  m = []
  p = []
  s = []
  ji_ko = []
  
  for ji in ji_hai:
    if ji_hai.count(ji) == 3:
      ji_ko.append([ji] * 3)
      for i in range(3):
        ji_hai.remove(ji)
    elif ji_hai.count(ji) == 2:
      toi.append(ji)
      for i in range(2):
        ji_hai.remove(ji)
    else:
      return 0
  
  for i in range(len(num_hai)):
    if num_hai[i][1] == "m":
      m.append(int(num_hai[i][0]))
    elif num_hai[i][1] == "p":
      p.append(int(num_hai[i][0]))
    else:
      s.append(int(num_hai[i][0]))
 
  len_num = [len(m), len(p), len(s), len(ji_hai)]
  
  if len(list(filter(lambda x: x % 3 != 0, len_num))) >= 2:
    return 0
  
  men_m = 0
  men_p = 0
  men_s = 0
  men_list = []
  toi_list = []
  pend = []

  if len(m) % 3 == 0:
    men_m += men_4(m)
  elif len(m) % 3 == 2:
    toi_raw = [i for i in m if m.count(i) >= 2]
    toi_list = list(set(toi_raw))
    for i in range(len(toi_list)):
      l1 = copy.copy(m)
      for j in range(2):
        l1.remove(toi_list[i])
      pend.append(l1)      
    
  else:
    return 0

  if len(p) % 3 == 0:
    men_p += men_4(p)
  elif len(p) % 3 == 2:
    toi_raw = [i for i in p if p.count(i) >= 2]
    toi_list = list(set(toi_raw))
    for i in range(len(toi_list)):
      l1 = copy.copy(p)
      for j in range(2):
        l1.remove(toi_list[i])
      pend.append(l1)
        
  else:
    return 0
  
  if len(s) % 3 == 0:
    men_s += men_4(s)
  elif len(s) % 3 == 2:
    toi_raw = [i for i in s if s.count(i) >= 2]
    toi_list = list(set(toi_raw))
    for i in range(len(toi_list)):
      l1 = copy.copy(s)
      for j in range(2):
        l1.remove(toi_list[i])
      pend.append(l1)
    
  else:
    return 0
  
  men_list = []
  for i in range(len(pend)):
    men_list.append(men_4(pend[i]))
    toi.append(toi_list[i])
  if men_list == []:
    men_list = [0]
  
  conf = len(ji_ko) + men_m + men_p + men_s  

  for i in range(len(men_list)):
    men_list[i] += conf
  
  for i in range(len(men_list)):
    if men_list[i] == 4:
      if len(toi) != 0:
        return "4面子形"
  else:
    return 0


hi_shu = []
for i in range(1, 10):
  hi_shu.append(str(i) + "m")
  hi_shu.append(str(i) + "p")
  hi_shu.append(str(i) + "s")
hi_shu.extend(["東", "南", "西", "北", "白", "發", "中"])

while 1:
  inp = list(input().split())
  mati = []
  for i in hi_shu:
    inlist = inp + [i]
    if is_hora(inlist) != 0:
      mati.append(i)
  print("待ち:",mati)
    
  print()
