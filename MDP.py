import sys

def oya_tsumo_1(sc):
  base = [1500, 2100, 2400, 3000, 3600]
  tsu_p = [scs * 4 / 3 for scs in base]
  fu = ["30", "40", "50", "60", "70"]
  for i in range(5):
    if tsu_p[i] >= sc:
      return "{}(1飜{}符)".format(base[i], fu[i])

def oya_tsumo_2(sc):
  base = [2100, 2400, 3000, 3900, 4800, 6000, 6900]
  tsu_p = [scs * 4 / 3 for scs in base]
  fu = ["20", "25", "30", "40", "50", "60", "70"]
  for i in range(7):
    if tsu_p[i] >= sc:
      return "{}(2飜{}符)".format(base[i], fu[i])

def oya_tsumo_3(sc):
  base = [3900, 4800, 6000, 7800, 9600, 11700]
  tsu_p = [scs * 4 / 3 for scs in base]
  fu = ["20", "25", "30", "40", "50", "60"]
  for i in range(6):
    if tsu_p[i] >= sc:
      return "{}(3飜{}符)".format(base[i], fu[i])
  
def oya_tsumo_4(sc):
  base = [7800, 9600, 11700]
  tsu_p = [scs * 4 / 3 for scs in base]
  fu = ["20", "25", "30"]
  for i in range(3):
    if tsu_p[i] >= sc:
      return "{}(4飜{}符)".format(base[i], fu[i])

def oya_tsumo_ov5(sc):
  base = [12000, 18000, 24000, 36000, 48000, 96000]
  tsu_p = [scs * 4 / 3 for scs in base]
  fu = ["満貫", "跳満", "倍満", "三倍満", "役満", "二倍役満"]
  for i in range(6):
    if tsu_p[i] >= sc:
      return fu[i]

def oya_tyoku_1(sc):
  base = [1500, 1600, 2000, 2400, 2900, 3400]	
  tyo_p = [scs * 2 for scs in base]
  fu = ["30", "40", "50", "60", "70"]
  for i in range(5):
    if tyo_p[i] >= sc:
      return "{}(1飜{}符)".format(base[i], fu[i])

def oya_tyoku_2(sc):
  base = [2000, 2400, 2900, 3900, 4800, 5800, 6800]
  tyo_p = [scs * 2 for scs in base]
  fu = ["20", "25", "30", "40", "50", "60", "70"]
  for i in range(7):
    if tyo_p[i] >= sc:
      return "{}(2飜{}符)".format(base[i], fu[i])

def oya_tyoku_3(sc):
  base = [3900, 4800, 5800, 7700, 9600, 11600]
  tyo_p = [scs * 2 for scs in base]
  fu = ["20", "25", "30", "40", "50", "60"]
  for i in range(6):
    if tyo_p[i] >= sc:
      return "{}(3飜{}符)".format(base[i], fu[i])

def oya_tyoku_4(sc):
  base = [7700, 9600, 11600]
  tyo_p = [scs * 2 for scs in base]
  fu = ["20", "25", "30"]
  for i in range(3):
    if tyo_p[i] >= sc:
      return "{}(4飜{}符)".format(base[i], fu[i])

def oya_tyoku_ov5(sc):
  base = [12000, 18000, 24000, 36000, 48000, 96000]
  tyo_p = [scs * 2 for scs in base]
  fu = ["満貫", "跳満", "倍満", "三倍満", "役満", "二倍役満"]
  for i in range(6):
    if tyo_p[i] >= sc:
      return fu[i]

def oya_ron_1(sc):
  base = [1500, 1600, 2000, 2400, 2900, 3400]	
  fu = ["30", "40", "50", "60", "70"]
  for i in range(5):
    if base[i] >= sc:
      return "{}(1飜{}符)".format(base[i], fu[i])

def oya_ron_2(sc):
  base = [2000, 2400, 2900, 3900, 4800, 5800, 6800]
  fu = ["20", "25", "30", "40", "50", "60", "70"]
  for i in range(7):
    if base[i] >= sc:
      return "{}(2飜{}符)".format(base[i], fu[i])

def oya_ron_3(sc):
  base = [3900, 4800, 5800, 7700, 9600, 11600]
  fu = ["20", "25", "30", "40", "50", "60"]
  for i in range(6):
    if base[i] >= sc:
      return "{}(3飜{}符)".format(base[i], fu[i])

def oya_ron_4(sc):
  base = [7700, 9600, 11600]
  fu = ["20", "25", "30"]
  for i in range(3):
    if base[i] >= sc:
      return "{}(4飜{}符)".format(base[i], fu[i])

def oya_ron_ov5(sc):
  base = [12000, 18000, 24000, 36000, 48000, 96000]
  fu = ["満貫", "跳満", "倍満", "三倍満", "役満", "二倍役満"]
  for i in range(6):
    if base[i] >= sc:
      return fu[i]

def ko_tsumo_kaburi_1(sc):
  base = [1100, 1500, 1600, 2000, 2400]
  tsu = [500, 700, 800, 1000, 1200]
  tsu_p = [base[i] + tsu[i] for i in range(5)]
  fu = ["30", "40", "50", "60", "70"]
  for i in range(5):
    if tsu_p[i] >= sc:
      return "{}(1飜{}符)".format(base[i], fu[i])

def ko_tsumo_kaburi_2(sc):
  base = [1500, 1600, 2000, 2700, 3200, 4000, 4700]
  tsu = [700, 800, 1000, 1300, 1600, 2000, 2300]
  tsu_p = [base[i] + tsu[i] for i in range(7)]
  fu = ["20", "25", "30", "40", "50", "60", "70"]
  for i in range(7):
    if tsu_p[i] >= sc:
      return "{}(2飜{}符)".format(base[i], fu[i])

def ko_tsumo_kaburi_3(sc):
  base = [2700, 3200, 4000, 5200, 6400, 7900]
  tsu = [1300, 1600, 2000, 2600, 3200, 3900]
  tsu_p = [base[i] + tsu[i] for i in range(6)]
  fu = ["20", "25", "30", "40", "50", "60"]
  for i in range(6):
    if tsu_p[i] >= sc:
      return "{}(3飜{}符)".format(base[i], fu[i])

def ko_tsumo_kaburi_4(sc):
  base = [5200, 6400, 7900]
  tsu = [2600, 3200, 3900]
  tsu_p = [base[i] + tsu[i] for i in range(3)]
  fu = ["20", "25", "30"]
  for i in range(3):
    if tsu_p[i] >= sc:
      return "{}(4飜{}符)".format(base[i], fu[i])

def ko_tsumo_kaburi_ov5(sc):
  base = [8000, 12000, 16000, 24000, 32000, 64000]
  tsu_p = [scs * 3 / 2 for scs in base]
  fu = ["満貫", "跳満", "倍満", "三倍満", "役満", "二倍役満"]
  for i in range(6):
    if tsu_p[i] >= sc:
      return fu[i]

def ko_tsumo_notk_1(sc):
  base = [1100, 1500, 1600, 2000, 2400]
  tsu = [300, 400, 400, 500, 600]
  tsu_p = [base[i] + tsu[i] for i in range(5)]
  fu = ["30", "40", "50", "60", "70"]
  for i in range(5):
    if tsu_p[i] >= sc:
      return "{}(1飜{}符)".format(base[i], fu[i])

def ko_tsumo_notk_2(sc):
  base = [1500, 1600, 2000, 2700, 3200, 4000, 4700]
  tsu = [400, 400, 500, 700, 800, 1000, 1200]
  tsu_p = [base[i] + tsu[i] for i in range(7)]
  fu = ["20", "25", "30", "40", "50", "60", "70"]
  for i in range(7):
    if tsu_p[i] >= sc:
      return "{}(2飜{}符)".format(base[i], fu[i])

def ko_tsumo_notk_3(sc):
  base = [2700, 3200, 4000, 5200, 6400, 7900]
  tsu = [700, 800, 1000, 1300, 1600, 2000]
  tsu_p = [base[i] + tsu[i] for i in range(6)]
  fu = ["20", "25", "30", "40", "50", "60"]
  for i in range(6):
    if tsu_p[i] >= sc:
      return "{}(3飜{}符)".format(base[i], fu[i])

def ko_tsumo_notk_4(sc):
  base = [5200, 6400, 7900]
  tsu = [1300, 1600, 2000]
  tsu_p = [base[i] + tsu[i] for i in range(3)]
  fu = ["20", "25", "30"]
  for i in range(3):
    if tsu_p[i] >= sc:
      return "{}(4飜{}符)".format(base[i], fu[i])

def ko_tsumo_notk_ov5(sc):
  base = [8000, 12000, 16000, 24000, 32000, 64000]
  tsu_p = [scs * 5 / 4 for scs in base]
  fu = ["満貫", "跳満", "倍満", "三倍満", "役満", "二倍役満"]
  for i in range(6):
    if tsu_p[i] >= sc:
      return fu[i]

def ko_tyoku_1(sc):
  base = [1000, 1300, 1600, 2000, 2300]
  tsu_p = [scs * 2 for scs in base]
  fu = ["30", "40", "50", "60", "70"]
  for i in range(5):
    if tsu_p[i] >= sc:
      return "{}(1飜{}符)".format(base[i], fu[i])

def ko_tyoku_2(sc):
  base = [1300, 1600, 2000, 2600, 3200, 3900, 4500]
  tsu_p = [scs * 2 for scs in base]
  fu = ["20", "25", "30", "40", "50", "60", "70"]
  for i in range(7):
    if tsu_p[i] >= sc:
      return "{}(2飜{}符)".format(base[i], fu[i])

def ko_tyoku_3(sc):
  base = [2600, 3200, 3900, 5200, 6400, 7700]
  tsu_p = [scs * 2 for scs in base]
  fu = ["20", "25", "30", "40", "50", "60"]
  for i in range(6):
    if tsu_p[i] >= sc:
      return "{}(3飜{}符)".format(base[i], fu[i])

def ko_tyoku_4(sc):
  base = [5200, 6400, 7700]
  tsu_p = [scs * 2 for scs in base]
  fu = ["20", "25", "30"]
  for i in range(3):
    if tsu_p[i] >= sc:
      return "{}(4飜{}符)".format(base[i], fu[i])

def ko_tyoku_ov5(sc):
  base = [8000, 12000, 16000, 24000, 32000, 64000]
  tsu_p = [scs * 2 for scs in base]
  fu = ["満貫", "跳満", "倍満", "三倍満", "役満", "二倍役満"]
  for i in range(6):
    if tsu_p[i] >= sc:
      return fu[i]

def ko_ron_1(sc):
  base = [1000, 1300, 1600, 2000, 2300]
  fu = ["30", "40", "50", "60", "70"]
  for i in range(5):
    if base[i] >= sc:
      return "{}(1飜{}符)".format(base[i], fu[i])

def ko_ron_2(sc):
  base = [1300, 1600, 2000, 2600, 3200, 3900, 4500]
  fu = ["20", "25", "30", "40", "50", "60", "70"]
  for i in range(7):
    if base[i] >= sc:
      return "{}(2飜{}符)".format(base[i], fu[i])

def ko_ron_3(sc):
  base = [2600, 3200, 3900, 5200, 6400, 7700]
  fu = ["20", "25", "30", "40", "50", "60"]
  for i in range(6):
    if base[i] >= sc:
      return "{}(3飜{}符)".format(base[i], fu[i])

def ko_ron_4(sc):
  base = [5200, 6400, 7700]
  fu = ["20", "25", "30"]
  for i in range(3):
    if base[i] >= sc:
      return "{}(4飜{}符)".format(base[i], fu[i])

def ko_ron_ov5(sc):
  base = [8000, 12000, 16000, 24000, 32000, 64000]
  fu = ["満貫", "跳満", "倍満", "三倍満", "役満", "二倍役満"]
  for i in range(6):
    if base[i] >= sc:
      return fu[i]


def tsumo(sc_h, sc_l):
  x = sc_h - sc_l
  x -= (300 * tsumi + 1000 * ri_chi)
  x -= 100 * tsumi
  return x

def tyoku(sc_h, sc_l):
  x = sc_h - sc_l
  x -= (300 * tsumi + 1000 * ri_chi)
  x -= 300 * tsumi
  return x

def ron(sc_h, sc_l):
  x = sc_h - sc_l
  x -= (300 * tsumi + 1000 * ri_chi)
  return x

def display(func, sub, list):
  if func[0](sub) != None:
    list.append(func[0](sub))
  if func[1](sub) != None:
    if func[0](sub) != "1飜30符":
      list.append(func[1](sub))
  if func[2](sub) != None:      
    if func[1](sub) != "2飜20符":
      list.append(func[2](sub))
  if func[3](sub) != None:
    if func[2](sub) != "3飜20符":
      list.append(func[3](sub))
  if func[3](sub) == None:
    list.append(func[4](sub))

def oya():
  display(o_ts, sub_ts, list_ts)
  display(o_ty, sub_ty, list_ty)
  display(o_ro, sub_ro, list_ro)

def kaburi():
  display(k_ts_k, sub_ts, list_ts)
  display(k_ty, sub_ty, list_ty)
  display(k_ro, sub_ro, list_ro)

def notk():
  display(k_ts_n, sub_ts, list_ts)
  display(k_ty, sub_ty, list_ty)
  display(k_ro, sub_ro, list_ro)

def output():
  print("ツモ:", " or ".join(list_ts))
  print("直撃:", " or ".join(list_ty))
  print("ロン:", " or ".join(list_ro))

o_ts = [oya_tsumo_1, oya_tsumo_2, oya_tsumo_3, oya_tsumo_4, oya_tsumo_ov5]
o_ty = [oya_tyoku_1, oya_tyoku_2, oya_tyoku_3, oya_tyoku_4, oya_tyoku_ov5]
o_ro = [oya_ron_1, oya_ron_2, oya_ron_3, oya_ron_4, oya_ron_ov5]
k_ts_k = [ko_tsumo_kaburi_1, ko_tsumo_kaburi_2, ko_tsumo_kaburi_3, ko_tsumo_kaburi_4, ko_tsumo_kaburi_ov5]
k_ts_n = [ko_tsumo_notk_1, ko_tsumo_notk_2, ko_tsumo_notk_3, ko_tsumo_notk_4, ko_tsumo_notk_ov5]
k_ty = [ko_tyoku_1, ko_tyoku_2, ko_tyoku_3, ko_tyoku_4, ko_tyoku_ov5]
k_ro = [ko_ron_1, ko_ron_2, ko_ron_3, ko_ron_4, ko_ron_ov5]

print("""---------------
点数: 自分以上の分をスペースで区切って半角入力
親: 今何着目？
立直棒: 何本ある？
供託: 何本場？
---------------
ツモ: ツモ
直撃: 上の人直撃
ロン: 上の人以外からのロンアガり
---------------
""")

while 1:
  scores_r = list(input("点数: ").split())
  scores = list(map(int, scores_r))
  scores.sort(reverse=True)
  sit = {}
  for i in range(len(scores)):
    sit[i + 1] = int(scores[i])

  oya_ban = int(input("親: "))
  ri_chi = int(input("立直棒: "))
  tsumi = int(input("供託: "))
  
  list_ts = []
  list_ty = []
  list_ro = []
   
  print()
  
  if len(scores) == 1:
    print("トップだよ")
    sys.exit()


  if len(scores) == 2:
    if sit[1] == sit[2]:
      print("トップだよ")
      sys.exit()
    
    else:
      print("1位条件:")
      sub_ts = tsumo(sit[1], sit[2])
      sub_ty = tyoku(sit[1], sit[2])
      sub_ro = ron(sit[1], sit[2])
      
      if oya_ban == 1:
        kaburi() 
      elif oya_ban == 2:
        oya()
      else:
        notk()
      output()


  if len(scores) == 3:
    if sit[1] == sit[3]:
      print("トップだよ")
      sys.exit()
  
    else:
      print("1位条件:")
      sub_ts = tsumo(sit[1], sit[3])
      sub_ty = tyoku(sit[1], sit[3])
      sub_ro = ron(sit[1], sit[3])
      
      if oya_ban == 1:
        kaburi()
      elif oya_ban == 3:
        oya()
      else:
        notk()     
      output()


      print("2位条件:")
      sub_ts = tsumo(sit[2], sit[3])
      sub_ty = tyoku(sit[2], sit[3])
      sub_ro = ron(sit[2], sit[3])

      if oya_ban == 2:
        kaburi()
      elif oya_ban == 3:
        oya()
      else:
        notk()
      output()


  if len(scores) == 4:
    if sit[1] == sit[4]:
      print("トップだよ")
      sys.exit()
  
    else:
      print("1位条件:")
      sub_ts = tsumo(sit[1], sit[4])
      sub_ty = tyoku(sit[1], sit[4])
      sub_ro = ron(sit[1], sit[4])
      
      if oya_ban == 1:
        kaburi()      
      elif oya_ban == 4:
        oya()
      else:
        notk()      
      output()


      print("2位条件:")
      sub_ts = tsumo(sit[2], sit[4])
      sub_ty = tyoku(sit[2], sit[4])
      sub_ro = ron(sit[2], sit[4])
      
      if oya_ban == 2:
        kaburi() 
      elif oya_ban == 4:
        oya() 
      else:
        notk()        
      output()


      print("3位条件:")
      sub_ts = tsumo(sit[3], sit[4])
      sub_ty = tyoku(sit[3], sit[4])
      sub_ro = ron(sit[3], sit[4])
      
      if oya_ban == 3:
        kaburi()
      elif oya_ban == 4:
        oya()
      else:
        notk()
      output() 

  print("""
""")
