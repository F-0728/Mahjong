import sys

def oya_tsumo_1(sc):
  base = [1500, 2100, 2400, 3000, 3600]
  tsu_p = [scs * 4 / 3 for scs in base]
  fu = ["30", "40", "50", "60", "70"]
  for i in range(5):
    if tsu_p[i] >= sc:
      return "1飜{}符".format(fu[i])

def oya_tsumo_2(sc):
  base = [2100, 3000, 3900, 4800, 6000, 6900]
  tsu_p = [scs * 4 / 3 for scs in base]
  fu = ["20", "30", "40", "50", "60", "70"]
  for i in range(6):
    if tsu_p[i] >= sc:
      return "2飜{}符".format(fu[i])

def oya_tsumo_3(sc):
  base = [3900, 6000, 7800, 9600, 11700]
  tsu_p = [scs * 4 / 3 for scs in base]
  fu = ["20", "30", "40", "50", "60"]
  for i in range(5):
    if tsu_p[i] >= sc:
      return "3飜{}符".format(fu[i])
  
def oya_tsumo_4(sc):
  base = [7800, 11700]
  tsu_p = [scs * 4 / 3 for scs in base]
  fu = ["20", "30"]
  for i in range(2):
    if tsu_p[i] >= sc:
      return "4飜{}符".format(fu[i])

def oya_tsumo_ov5(sc):
  base = [12000, 18000, 24000, 36000, 48000]
  tsu_p = [scs * 4 / 3 for scs in base]
  fu = ["満貫", "跳満", "倍満", "三倍満", "役満"]
  for i in range(5):
    if tsu_p[i] >= sc:
      return fu[i]

def oya_tyoku_1(sc):
  base = [1500, 2000, 2400, 2900, 3400]	
  tyo_p = [scs * 2 for scs in base]
  fu = ["30", "40", "50", "60", "70"]
  for i in range(5):
    if tyo_p[i] >= sc:
      return "1飜{}符".format(fu[i])

def oya_tyoku_2(sc):
  base = [2000, 2900, 3900, 4800, 5800, 6800]
  tyo_p = [scs * 2 for scs in base]
  fu = ["20", "30", "40", "50", "60", "70"]
  for i in range(6):
    if tyo_p[i] >= sc:
      return "2飜{}符".format(fu[i])

def oya_tyoku_3(sc):
  base = [3900, 5800, 7700, 9600, 11600]
  tyo_p = [scs * 2 for scs in base]
  fu = ["20", "30", "40", "50", "60"]
  for i in range(5):
    if tyo_p[i] >= sc:
      return "3飜{}符".format(fu[i])

def oya_tyoku_4(sc):
  base = [7700, 11600]
  tyo_p = [scs * 2 for scs in base]
  fu = ["20", "30"]
  for i in range(2):
    if tyo_p[i] >= sc:
      return "4飜{}符".format(fu[i])

def oya_tyoku_ov5(sc):
  base = [12000, 18000, 24000, 36000, 48000]
  tyo_p = [scs * 2 for scs in base]
  fu = ["満貫", "跳満", "倍満", "三倍満", "役満"]
  for i in range(5):
    if tyo_p[i] >= sc:
      return fu[i]

def oya_ron_1(sc):
  base = [1500, 2000, 2400, 2900, 3400]	
  fu = ["30", "40", "50", "60", "70"]
  for i in range(5):
    if base[i] >= sc:
      return "1飜{}符".format(fu[i])

def oya_ron_2(sc):
  base = [2000, 2900, 3900, 4800, 5800, 6800]
  fu = ["20", "30", "40", "50", "60", "70"]
  for i in range(6):
    if base[i] >= sc:
      return "2飜{}符".format(fu[i])

def oya_ron_3(sc):
  base = [3900, 5800, 7700, 9600, 11600]
  fu = ["20", "30", "40", "50", "60"]
  for i in range(5):
    if base[i] >= sc:
      return "3飜{}符".format(fu[i])

def oya_ron_4(sc):
  base = [7700, 11600]
  fu = ["20", "30"]
  for i in range(2):
    if base[i] >= sc:
      return "4飜{}符".format(fu[i])

def oya_ron_ov5(sc):
  base = [12000, 18000, 24000, 36000, 48000]
  fu = ["満貫", "跳満", "倍満", "三倍満", "役満"]
  for i in range(5):
    if base[i] >= sc:
      return fu[i]

def ko_tsumo_kaburi_1(sc):
  base = [1100, 1500, 1600, 2000, 2400]
  tsu = [500, 700, 800, 1000, 1200]
  tsu_p = [base[i] + tsu[i] for i in range(5)]
  fu = ["30", "40", "50", "60", "70"]
  for i in range(5):
    if tsu_p[i] >= sc:
      return "1飜{}符".format(fu[i])

def ko_tsumo_kaburi_2(sc):
  base = [1500, 2000, 2700, 3200, 4000, 4700]
  tsu = [700, 1000, 1300, 1600, 2000, 2300]
  tsu_p = [base[i] + tsu[i] for i in range(6)]
  fu = ["20", "30", "40", "50", "60", "70"]
  for i in range(6):
    if tsu_p[i] >= sc:
      return "2飜{}符".format(fu[i])

def ko_tsumo_kaburi_3(sc):
  base = [2700, 4000, 5200, 6400, 7900]
  tsu = [1300, 2000, 2600, 3200, 3900]
  tsu_p = [base[i] + tsu[i] for i in range(5)]
  fu = ["20", "30", "40", "50", "60"]
  for i in range(5):
    if tsu_p[i] >= sc:
      return "3飜{}符".format(fu[i])

def ko_tsumo_kaburi_4(sc):
  base = [5200, 7900]
  tsu = [2600, 3900]
  tsu_p = [base[i] + tsu[i] for i in range(2)]
  fu = ["20", "30"]
  for i in range(2):
    if tsu_p[i] >= sc:
      return "4飜{}符".format(fu[i])

def ko_tsumo_kaburi_ov5(sc):
  base = [8000, 12000, 16000, 24000, 32000]
  tsu_p = [scs * 3 / 2 for scs in base]
  fu = ["満貫", "跳満", "倍満", "三倍満", "役満"]
  for i in range(5):
    if tsu_p[i] >= sc:
      return fu[i]

def ko_tsumo_notk_1(sc):
  base = [1100, 1500, 1600, 2000, 2400]
  tsu = [300, 400, 400, 500, 600]
  tsu_p = [base[i] + tsu[i] for i in range(5)]
  fu = ["30", "40", "50", "60", "70"]
  for i in range(5):
    if tsu_p[i] >= sc:
      return "1飜{}符".format(fu[i])

def ko_tsumo_notk_2(sc):
  base = [1500, 2000, 2700, 3200, 4000, 4700]
  tsu = [400, 500, 700, 800, 1000, 1200]
  tsu_p = [base[i] + tsu[i] for i in range(6)]
  fu = ["20", "30", "40", "50", "60", "70"]
  for i in range(6):
    if tsu_p[i] >= sc:
      return "2飜{}符".format(fu[i])

def ko_tsumo_notk_3(sc):
  base = [2700, 4000, 5200, 6400, 7900]
  tsu = [700, 1000, 1300, 1600, 2000]
  tsu_p = [base[i] + tsu[i] for i in range(5)]
  fu = ["20", "30", "40", "50", "60"]
  for i in range(5):
    if tsu_p[i] >= sc:
      return "3飜{}符".format(fu[i])

def ko_tsumo_notk_4(sc):
  base = [5200, 7900]
  tsu = [1300, 2000]
  tsu_p = [base[i] + tsu[i] for i in range(2)]
  fu = ["20", "30"]
  for i in range(2):
    if tsu_p[i] >= sc:
      return "4飜{}符".format(fu[i])

def ko_tsumo_notk_ov5(sc):
  base = [8000, 12000, 16000, 24000, 32000]
  tsu_p = [scs * 5 / 4 for scs in base]
  fu = ["満貫", "跳満", "倍満", "三倍満", "役満"]
  for i in range(5):
    if tsu_p[i] >= sc:
      return fu[i]

def ko_tyoku_1(sc):
  base = [1000, 1300, 1600, 2000, 2300]
  tsu_p = [scs * 2 for scs in base]
  fu = ["30", "40", "50", "60", "70"]
  for i in range(5):
    if tsu_p[i] >= sc:
      return "1飜{}符".format(fu[i])

def ko_tyoku_2(sc):
  base = [1300, 2000, 2600, 3200, 3900, 4500]
  tsu_p = [scs * 2 for scs in base]
  fu = ["20", "30", "40", "50", "60", "70"]
  for i in range(6):
    if tsu_p[i] >= sc:
      return "2飜{}符".format(fu[i])

def ko_tyoku_3(sc):
  base = [2600, 3900, 5200, 6400, 7700]
  tsu_p = [scs * 2 for scs in base]
  fu = ["20", "30", "40", "50", "60"]
  for i in range(5):
    if tsu_p[i] >= sc:
      return "3飜{}符".format(fu[i])

def ko_tyoku_4(sc):
  base = [5200, 7700]
  tsu_p = [scs * 2 for scs in base]
  fu = ["20", "30"]
  for i in range(2):
    if tsu_p[i] >= sc:
      return "4飜{}符".format(fu[i])

def ko_tyoku_ov5(sc):
  base = [8000, 12000, 16000, 24000, 32000]
  tsu_p = [scs * 2 for scs in base]
  fu = ["満貫", "跳満", "倍満", "三倍満", "役満"]
  for i in range(5):
    if tsu_p[i] >= sc:
      return fu[i]

def ko_ron_1(sc):
  base = [1000, 1300, 1600, 2000, 2300]
  fu = ["30", "40", "50", "60", "70"]
  for i in range(5):
    if base[i] >= sc:
      return "1飜{}符".format(fu[i])

def ko_ron_2(sc):
  base = [1300, 2000, 2600, 3200, 3900, 4500]
  fu = ["20", "30", "40", "50", "60", "70"]
  for i in range(6):
    if base[i] >= sc:
      return "2飜{}符".format(fu[i])

def ko_ron_3(sc):
  base = [2600, 3900, 5200, 6400, 7700]
  fu = ["20", "30", "40", "50", "60"]
  for i in range(5):
    if base[i] >= sc:
      return "3飜{}符".format(fu[i])

def ko_ron_4(sc):
  base = [5200, 7700]
  fu = ["20", "30"]
  for i in range(2):
    if base[i] >= sc:
      return "4飜{}符".format(fu[i])

def ko_ron_ov5(sc):
  base = [8000, 12000, 16000, 24000, 32000]
  fu = ["満貫", "跳満", "倍満", "三倍満", "役満"]
  for i in range(5):
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

print("""---------------
点数: 自分以上の分をスペースで区切って半角入力
親: 今何着目？
立直棒: そのまま
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

  oya = int(input("親: "))
  ri_chi = int(input("立直棒: "))
  tsumi = int(input("供託: "))
  
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
      list_ts = []
      list_ty = []
      list_ro = []
      if oya == 1:
        if ko_tsumo_kaburi_1(sub_ts) != None:
          list_ts.append(ko_tsumo_kaburi_1(sub_ts))
        if ko_tsumo_kaburi_2(sub_ts) != None:
          if ko_tsumo_kaburi_1(sub_ts) != "1飜30符":
            list_ts.append(ko_tsumo_kaburi_2(sub_ts))
        if ko_tsumo_kaburi_3(sub_ts) != None:      
          if ko_tsumo_kaburi_2(sub_ts) != "2飜20符":
            list_ts.append(ko_tsumo_kaburi_3(sub_ts))
        if ko_tsumo_kaburi_4(sub_ts) != None:
            if ko_tsumo_kaburi_3(sub_ts) != "3飜20符":
              list_ts.append(ko_tsumo_kaburi_4(sub_ts))
        if ko_tsumo_kaburi_4(sub_ts) == None:
          list_ts.append(ko_tsumo_kaburi_ov5(sub_ts))
        
        if ko_tyoku_1(sub_ty) != None:
          list_ty.append(ko_tyoku_1(sub_ty))
        if ko_tyoku_2(sub_ty) != None:
          if ko_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(ko_tyoku_2(sub_ty))
        if ko_tyoku_3(sub_ty) != None:      
          if ko_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(ko_tyoku_3(sub_ty))
        if ko_tyoku_4(sub_ty) != None:
            if ko_tyoku_3(sub_ty) != "3飜20符":
              list_ty.append(ko_tyoku_4(sub_ty))
        if ko_tyoku_4(sub_ty) == None:
          list_ty.append(ko_tyoku_ov5(sub_ty))
        
        if ko_ron_1(sub_ro) != None:
          list_ro.append(ko_ron_1(sub_ro))
        if ko_ron_2(sub_ro) != None:
          if ko_ron_1(sub_ro) != "1飜30符":
            list_ro.append(ko_ron_2(sub_ro))
        if ko_ron_3(sub_ro) != None:      
          if ko_ron_2(sub_ro) != "2飜20符":
            list_ro.append(ko_ron_3(sub_ro))
        if ko_ron_4(sub_ro) != None:
            if ko_ron_3(sub_ro) != "3飜20符":
              list_ro.append(ko_ron_4(sub_ro))
        if ko_ron_4(sub_ro) == None:
          list_ro.append(ko_ron_ov5(sub_ro))
        
      elif oya == 2:
        if oya_tsumo_1(sub_ts) != None:
          list_ts.append(oya_tsumo_1(sub_ts))
        if oya_tsumo_2(sub_ts) != None:
          if oya_tsumo_1(sub_ts) != "1飜30符":
            list_ts.append(oya_tsumo_2(sub_ts))
        if oya_tsumo_3(sub_ts) != None:      
          if oya_tsumo_2(sub_ts) != "2飜20符":
            list_ts.append(oya_tsumo_3(sub_ts))
        if oya_tsumo_4(sub_ts) != None:
          if oya_tsumo_3(sub_ts) != "3飜20符":
            list_ts.append(oya_tsumo_4(sub_ts))
        if oya_tsumo_4(sub_ts) == None:
          list_ts.append(oya_tsumo_ov5(sub_ts))
        
        if oya_tyoku_1(sub_ty) != None:
          list_ty.append(oya_tyoku_1(sub_ty))
        if oya_tyoku_2(sub_ty) != None:
          if oya_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(oya_tyoku_2(sub_ty))
        if oya_tyoku_3(sub_ty) != None:      
          if oya_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(oya_tyoku_3(sub_ty))
        if oya_tyoku_4(sub_ty) != None:
          if oya_tyoku_3(sub_ty) != "3飜20符":
            list_ty.append(oya_tyoku_4(sub_ty))
        if oya_tyoku_4(sub_ty) == None:
          list_ty.append(oya_tyoku_ov5(sub_ty))
        
        if oya_ron_1(sub_ro) != None:
          list_ro.append(oya_ron_1(sub_ro))
        if oya_ron_2(sub_ro) != None:
          if oya_ron_1(sub_ro) != "1飜30符":
            list_ro.append(oya_ron_2(sub_ro))
        if oya_ron_3(sub_ro) != None:      
          if oya_ron_2(sub_ro) != "2飜20符":
            list_ro.append(oya_ron_3(sub_ro))
        if oya_ron_4(sub_ro) != None:
          if oya_ron_3(sub_ro) != "3飜20符":
            list_ro.append(oya_ron_4(sub_ro))
        if oya_ron_4(sub_ro) == None:
          list_ro.append(oya_ron_ov5(sub_ro))
     
      else:
        if ko_tsumo_notk_1(sub_ts) != None:
          list_ts.append(ko_tsumo_notk_1(sub_ts))
        if ko_tsumo_notk_2(sub_ts) != None:
          if ko_tsumo_notk_1(sub_ts) != "1飜30符":
            list_ts.append(ko_tsumo_notk_2(sub_ts))
        if ko_tsumo_notk_3(sub_ts) != None:      
          if ko_tsumo_notk_2(sub_ts) != "2飜20符":
            list_ts.append(ko_tsumo_notk_3(sub_ts))
        if ko_tsumo_notk_4(sub_ts) != None:
            if ko_tsumo_notk_3(sub_ts) != "3飜20符":
              list_ts.append(ko_tsumo_notk_4(sub_ts))
        if ko_tsumo_notk_4(sub_ts) == None:
          list_ts.append(ko_tsumo_notk_ov5(sub_ts))
        
        if ko_tyoku_1(sub_ty) != None:
          list_ty.append(ko_tyoku_1(sub_ty))
        if ko_tyoku_2(sub_ty) != None:
          if ko_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(ko_tyoku_2(sub_ty))
        if ko_tyoku_3(sub_ty) != None:      
          if ko_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(ko_tyoku_3(sub_ty))
        if ko_tyoku_4(sub_ty) != None:
            if ko_tyoku_3(sub_ty) != "3飜20符":
              list_ty.append(ko_tyoku_4(sub_ty))
        if ko_tyoku_4(sub_ty) == None:
          list_ty.append(ko_tyoku_ov5(sub_ty))
        
        if ko_ron_1(sub_ro) != None:
          list_ro.append(ko_ron_1(sub_ro))
        if ko_ron_2(sub_ro) != None:
          if ko_ron_1(sub_ro) != "1飜30符":
            list_ro.append(ko_ron_2(sub_ro))
        if ko_ron_3(sub_ro) != None:      
          if ko_ron_2(sub_ro) != "2飜20符":
            list_ro.append(ko_ron_3(sub_ro))
        if ko_ron_4(sub_ro) != None:
            if ko_ron_3(sub_ro) != "3飜20符":
              list_ro.append(ko_ron_4(sub_ro))
        if ko_ron_4(sub_ro) == None:
          list_ro.append(ko_ron_ov5(sub_ro))

      print("ツモ:", " or ".join(list_ts))
      print("直撃:", " or ".join(list_ty))
      print("ロン:", " or ".join(list_ro))


  if len(scores) == 3:
    if sit[1] == sit[3]:
      print("トップだよ")
      sys.exit()
    else:
      print("1位条件:")
      sub_ts = tsumo(sit[1], sit[3])
      sub_ty = tyoku(sit[1], sit[3])
      sub_ro = ron(sit[1], sit[3])
      list_ts = []
      list_ty = []
      list_ro = []
      if oya == 1:
        if ko_tsumo_kaburi_1(sub_ts) != None:
          list_ts.append(ko_tsumo_kaburi_1(sub_ts))
        if ko_tsumo_kaburi_2(sub_ts) != None:
          if ko_tsumo_kaburi_1(sub_ts) != "1飜30符":
            list_ts.append(ko_tsumo_kaburi_2(sub_ts))
        if ko_tsumo_kaburi_3(sub_ts) != None:      
          if ko_tsumo_kaburi_2(sub_ts) != "2飜20符":
            list_ts.append(ko_tsumo_kaburi_3(sub_ts))
        if ko_tsumo_kaburi_4(sub_ts) != None:
            if ko_tsumo_kaburi_3(sub_ts) != "3飜20符":
              list_ts.append(ko_tsumo_kaburi_4(sub_ts))
        if ko_tsumo_kaburi_4(sub_ts) == None:
          list_ts.append(ko_tsumo_kaburi_ov5(sub_ts))
        
        if ko_tyoku_1(sub_ty) != None:
          list_ty.append(ko_tyoku_1(sub_ty))
        if ko_tyoku_2(sub_ty) != None:
          if ko_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(ko_tyoku_2(sub_ty))
        if ko_tyoku_3(sub_ty) != None:      
          if ko_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(ko_tyoku_3(sub_ty))
        if ko_tyoku_4(sub_ty) != None:
            if ko_tyoku_3(sub_ty) != "3飜20符":
              list_ty.append(ko_tyoku_4(sub_ty))
        if ko_tyoku_4(sub_ty) == None:
          list_ty.append(ko_tyoku_ov5(sub_ty))
        
        if ko_ron_1(sub_ro) != None:
          list_ro.append(ko_ron_1(sub_ro))
        if ko_ron_2(sub_ro) != None:
          if ko_ron_1(sub_ro) != "1飜30符":
            list_ro.append(ko_ron_2(sub_ro))
        if ko_ron_3(sub_ro) != None:      
          if ko_ron_2(sub_ro) != "2飜20符":
            list_ro.append(ko_ron_3(sub_ro))
        if ko_ron_4(sub_ro) != None:
            if ko_ron_3(sub_ro) != "3飜20符":
              list_ro.append(ko_ron_4(sub_ro))
        if ko_ron_4(sub_ro) == None:
          list_ro.append(ko_ron_ov5(sub_ro))
      
      elif oya == 3:
        if oya_tsumo_1(sub_ts) != None:
          list_ts.append(oya_tsumo_1(sub_ts))
        if oya_tsumo_2(sub_ts) != None:
          if oya_tsumo_1(sub_ts) != "1飜30符":
            list_ts.append(oya_tsumo_2(sub_ts))
        if oya_tsumo_3(sub_ts) != None:      
          if oya_tsumo_2(sub_ts) != "2飜20符":
            list_ts.append(oya_tsumo_3(sub_ts))
        if oya_tsumo_4(sub_ts) != None:
          if oya_tsumo_3(sub_ts) != "3飜20符":
            list_ts.append(oya_tsumo_4(sub_ts))
        if oya_tsumo_4(sub_ts) == None:
          list_ts.append(oya_tsumo_ov5(sub_ts))
        
        if oya_tyoku_1(sub_ty) != None:
          list_ty.append(oya_tyoku_1(sub_ty))
        if oya_tyoku_2(sub_ty) != None:
          if oya_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(oya_tyoku_2(sub_ty))
        if oya_tyoku_3(sub_ty) != None:      
          if oya_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(oya_tyoku_3(sub_ty))
        if oya_tyoku_4(sub_ty) != None:
          if oya_tyoku_3(sub_ty) != "3飜20符":
            list_ty.append(oya_tyoku_4(sub_ty))
        if oya_tyoku_4(sub_ty) == None:
          list_ty.append(oya_tyoku_ov5(sub_ty))
        
        if oya_ron_1(sub_ro) != None:
          list_ro.append(oya_ron_1(sub_ro))
        if oya_ron_2(sub_ro) != None:
          if oya_ron_1(sub_ro) != "1飜30符":
            list_ro.append(oya_ron_2(sub_ro))
        if oya_ron_3(sub_ro) != None:      
          if oya_ron_2(sub_ro) != "2飜20符":
            list_ro.append(oya_ron_3(sub_ro))
        if oya_ron_4(sub_ro) != None:
          if oya_ron_3(sub_ro) != "3飜20符":
            list_ro.append(oya_ron_4(sub_ro))
        if oya_ron_4(sub_ro) == None:
          list_ro.append(oya_ron_ov5(sub_ro))
      
      else:
        if ko_tsumo_notk_1(sub_ts) != None:
          list_ts.append(ko_tsumo_notk_1(sub_ts))
        if ko_tsumo_notk_2(sub_ts) != None:
          if ko_tsumo_notk_1(sub_ts) != "1飜30符":
            list_ts.append(ko_tsumo_notk_2(sub_ts))
        if ko_tsumo_notk_3(sub_ts) != None:      
          if ko_tsumo_notk_2(sub_ts) != "2飜20符":
            list_ts.append(ko_tsumo_notk_3(sub_ts))
        if ko_tsumo_notk_4(sub_ts) != None:
            if ko_tsumo_notk_3(sub_ts) != "3飜20符":
              list_ts.append(ko_tsumo_notk_4(sub_ts))
        if ko_tsumo_notk_4(sub_ts) == None:
          list_ts.append(ko_tsumo_notk_ov5(sub_ts))
        
        if ko_tyoku_1(sub_ty) != None:
          list_ty.append(ko_tyoku_1(sub_ty))
        if ko_tyoku_2(sub_ty) != None:
          if ko_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(ko_tyoku_2(sub_ty))
        if ko_tyoku_3(sub_ty) != None:      
          if ko_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(ko_tyoku_3(sub_ty))
        if ko_tyoku_4(sub_ty) != None:
            if ko_tyoku_3(sub_ty) != "3飜20符":
              list_ty.append(ko_tyoku_4(sub_ty))
        if ko_tyoku_4(sub_ty) == None:
          list_ty.append(ko_tyoku_ov5(sub_ty))
        
        if ko_ron_1(sub_ro) != None:
          list_ro.append(ko_ron_1(sub_ro))
        if ko_ron_2(sub_ro) != None:
          if ko_ron_1(sub_ro) != "1飜30符":
            list_ro.append(ko_ron_2(sub_ro))
        if ko_ron_3(sub_ro) != None:      
          if ko_ron_2(sub_ro) != "2飜20符":
            list_ro.append(ko_ron_3(sub_ro))
        if ko_ron_4(sub_ro) != None:
            if ko_ron_3(sub_ro) != "3飜20符":
              list_ro.append(ko_ron_4(sub_ro))
        if ko_ron_4(sub_ro) == None:
          list_ro.append(ko_ron_ov5(sub_ro))

      print("ツモ:", " or ".join(list_ts))
      print("直撃:", " or ".join(list_ty))
      print("ロン:", " or ".join(list_ro))


      print("2位条件:")
      sub_ts = tsumo(sit[2], sit[3])
      sub_ty = tyoku(sit[2], sit[3])
      sub_ro = ron(sit[2], sit[3])
      list_ts = []
      list_ty = []
      list_ro = []
      if oya == 2:
        if ko_tsumo_kaburi_1(sub_ts) != None:
          list_ts.append(ko_tsumo_kaburi_1(sub_ts))
        if ko_tsumo_kaburi_2(sub_ts) != None:
          if ko_tsumo_kaburi_1(sub_ts) != "1飜30符":
            list_ts.append(ko_tsumo_kaburi_2(sub_ts))
        if ko_tsumo_kaburi_3(sub_ts) != None:      
          if ko_tsumo_kaburi_2(sub_ts) != "2飜20符":
            list_ts.append(ko_tsumo_kaburi_3(sub_ts))
        if ko_tsumo_kaburi_4(sub_ts) != None:
            if ko_tsumo_kaburi_3(sub_ts) != "3飜20符":
              list_ts.append(ko_tsumo_kaburi_4(sub_ts))
        if ko_tsumo_kaburi_4(sub_ts) == None:
          list_ts.append(ko_tsumo_kaburi_ov5(sub_ts))
        
        if ko_tyoku_1(sub_ty) != None:
          list_ty.append(ko_tyoku_1(sub_ty))
        if ko_tyoku_2(sub_ty) != None:
          if ko_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(ko_tyoku_2(sub_ty))
        if ko_tyoku_3(sub_ty) != None:      
          if ko_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(ko_tyoku_3(sub_ty))
        if ko_tyoku_4(sub_ty) != None:
            if ko_tyoku_3(sub_ty) != "3飜20符":
              list_ty.append(ko_tyoku_4(sub_ty))
        if ko_tyoku_4(sub_ty) == None:
          list_ty.append(ko_tyoku_ov5(sub_ty))
        
        if ko_ron_1(sub_ro) != None:
          list_ro.append(ko_ron_1(sub_ro))
        if ko_ron_2(sub_ro) != None:
          if ko_ron_1(sub_ro) != "1飜30符":
            list_ro.append(ko_ron_2(sub_ro))
        if ko_ron_3(sub_ro) != None:      
          if ko_ron_2(sub_ro) != "2飜20符":
            list_ro.append(ko_ron_3(sub_ro))
        if ko_ron_4(sub_ro) != None:
            if ko_ron_3(sub_ro) != "3飜20符":
              list_ro.append(ko_ron_4(sub_ro))
        if ko_ron_4(sub_ro) == None:
          list_ro.append(ko_ron_ov5(sub_ro))
      
      elif oya == 3:
        if oya_tsumo_1(sub_ts) != None:
          list_ts.append(oya_tsumo_1(sub_ts))
        if oya_tsumo_2(sub_ts) != None:
          if oya_tsumo_1(sub_ts) != "1飜30符":
            list_ts.append(oya_tsumo_2(sub_ts))
        if oya_tsumo_3(sub_ts) != None:      
          if oya_tsumo_2(sub_ts) != "2飜20符":
            list_ts.append(oya_tsumo_3(sub_ts))
        if oya_tsumo_4(sub_ts) != None:
          if oya_tsumo_3(sub_ts) != "3飜20符":
            list_ts.append(oya_tsumo_4(sub_ts))
        if oya_tsumo_4(sub_ts) == None:
          list_ts.append(oya_tsumo_ov5(sub_ts))
        
        if oya_tyoku_1(sub_ty) != None:
          list_ty.append(oya_tyoku_1(sub_ty))
        if oya_tyoku_2(sub_ty) != None:
          if oya_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(oya_tyoku_2(sub_ty))
        if oya_tyoku_3(sub_ty) != None:      
          if oya_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(oya_tyoku_3(sub_ty))
        if oya_tyoku_4(sub_ty) != None:
          if oya_tyoku_3(sub_ty) != "3飜20符":
            list_ty.append(oya_tyoku_4(sub_ty))
        if oya_tyoku_4(sub_ty) == None:
          list_ty.append(oya_tyoku_ov5(sub_ty))
        
        if oya_ron_1(sub_ro) != None:
          list_ro.append(oya_ron_1(sub_ro))
        if oya_ron_2(sub_ro) != None:
          if oya_ron_1(sub_ro) != "1飜30符":
            list_ro.append(oya_ron_2(sub_ro))
        if oya_ron_3(sub_ro) != None:      
          if oya_ron_2(sub_ro) != "2飜20符":
            list_ro.append(oya_ron_3(sub_ro))
        if oya_ron_4(sub_ro) != None:
          if oya_ron_3(sub_ro) != "3飜20符":
            list_ro.append(oya_ron_4(sub_ro))
        if oya_ron_4(sub_ro) == None:
          list_ro.append(oya_ron_ov5(sub_ro))
      
      else:
        if ko_tsumo_notk_1(sub_ts) != None:
          list_ts.append(ko_tsumo_notk_1(sub_ts))
        if ko_tsumo_notk_2(sub_ts) != None:
          if ko_tsumo_notk_1(sub_ts) != "1飜30符":
            list_ts.append(ko_tsumo_notk_2(sub_ts))
        if ko_tsumo_notk_3(sub_ts) != None:      
          if ko_tsumo_notk_2(sub_ts) != "2飜20符":
            list_ts.append(ko_tsumo_notk_3(sub_ts))
        if ko_tsumo_notk_4(sub_ts) != None:
            if ko_tsumo_notk_3(sub_ts) != "3飜20符":
              list_ts.append(ko_tsumo_notk_4(sub_ts))
        if ko_tsumo_notk_4(sub_ts) == None:
          list_ts.append(ko_tsumo_notk_ov5(sub_ts))
        
        if ko_tyoku_1(sub_ty) != None:
          list_ty.append(ko_tyoku_1(sub_ty))
        if ko_tyoku_2(sub_ty) != None:
          if ko_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(ko_tyoku_2(sub_ty))
        if ko_tyoku_3(sub_ty) != None:      
          if ko_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(ko_tyoku_3(sub_ty))
        if ko_tyoku_4(sub_ty) != None:
            if ko_tyoku_3(sub_ty) != "3飜20符":
              list_ty.append(ko_tyoku_4(sub_ty))
        if ko_tyoku_4(sub_ty) == None:
          list_ty.append(ko_tyoku_ov5(sub_ty))
        
        if ko_ron_1(sub_ro) != None:
          list_ro.append(ko_ron_1(sub_ro))
        if ko_ron_2(sub_ro) != None:
          if ko_ron_1(sub_ro) != "1飜30符":
            list_ro.append(ko_ron_2(sub_ro))
        if ko_ron_3(sub_ro) != None:      
          if ko_ron_2(sub_ro) != "2飜20符":
            list_ro.append(ko_ron_3(sub_ro))
        if ko_ron_4(sub_ro) != None:
            if ko_ron_3(sub_ro) != "3飜20符":
              list_ro.append(ko_ron_4(sub_ro))
        if ko_ron_4(sub_ro) == None:
          list_ro.append(ko_ron_ov5(sub_ro))

      print("ツモ:", " or ".join(list_ts))
      print("直撃:", " or ".join(list_ty))
      print("ロン:", " or ".join(list_ro))

  if len(scores) == 4:
    if sit[1] == sit[4]:
      print("トップだよ")
      sys.exit()
    else:
      print("1位条件:")
      sub_ts = tsumo(sit[1], sit[4])
      sub_ty = tyoku(sit[1], sit[4])
      sub_ro = ron(sit[1], sit[4])
      list_ts = []
      list_ty = []
      list_ro = []
      if oya == 1:
        if ko_tsumo_kaburi_1(sub_ts) != None:
          list_ts.append(ko_tsumo_kaburi_1(sub_ts))
        if ko_tsumo_kaburi_2(sub_ts) != None:
          if ko_tsumo_kaburi_1(sub_ts) != "1飜30符":
            list_ts.append(ko_tsumo_kaburi_2(sub_ts))
        if ko_tsumo_kaburi_3(sub_ts) != None:      
          if ko_tsumo_kaburi_2(sub_ts) != "2飜20符":
            list_ts.append(ko_tsumo_kaburi_3(sub_ts))
        if ko_tsumo_kaburi_4(sub_ts) != None:
            if ko_tsumo_kaburi_3(sub_ts) != "3飜20符":
              list_ts.append(ko_tsumo_kaburi_4(sub_ts))
        if ko_tsumo_kaburi_4(sub_ts) == None:
          list_ts.append(ko_tsumo_kaburi_ov5(sub_ts))
        
        if ko_tyoku_1(sub_ty) != None:
          list_ty.append(ko_tyoku_1(sub_ty))
        if ko_tyoku_2(sub_ty) != None:
          if ko_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(ko_tyoku_2(sub_ty))
        if ko_tyoku_3(sub_ty) != None:      
          if ko_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(ko_tyoku_3(sub_ty))
        if ko_tyoku_4(sub_ty) != None:
            if ko_tyoku_3(sub_ty) != "3飜20符":
              list_ty.append(ko_tyoku_4(sub_ty))
        if ko_tyoku_4(sub_ty) == None:
          list_ty.append(ko_tyoku_ov5(sub_ty))
        
        if ko_ron_1(sub_ro) != None:
          list_ro.append(ko_ron_1(sub_ro))
        if ko_ron_2(sub_ro) != None:
          if ko_ron_1(sub_ro) != "1飜30符":
            list_ro.append(ko_ron_2(sub_ro))
        if ko_ron_3(sub_ro) != None:      
          if ko_ron_2(sub_ro) != "2飜20符":
            list_ro.append(ko_ron_3(sub_ro))
        if ko_ron_4(sub_ro) != None:
            if ko_ron_3(sub_ro) != "3飜20符":
              list_ro.append(ko_ron_4(sub_ro))
        if ko_ron_4(sub_ro) == None:
          list_ro.append(ko_ron_ov5(sub_ro))
      
      elif oya == 4:
        if oya_tsumo_1(sub_ts) != None:
          list_ts.append(oya_tsumo_1(sub_ts))
        if oya_tsumo_2(sub_ts) != None:
          if oya_tsumo_1(sub_ts) != "1飜30符":
            list_ts.append(oya_tsumo_2(sub_ts))
        if oya_tsumo_3(sub_ts) != None:      
          if oya_tsumo_2(sub_ts) != "2飜20符":
            list_ts.append(oya_tsumo_3(sub_ts))
        if oya_tsumo_4(sub_ts) != None:
          if oya_tsumo_3(sub_ts) != "3飜20符":
            list_ts.append(oya_tsumo_4(sub_ts))
        if oya_tsumo_4(sub_ts) == None:
          list_ts.append(oya_tsumo_ov5(sub_ts))
        
        if oya_tyoku_1(sub_ty) != None:
          list_ty.append(oya_tyoku_1(sub_ty))
        if oya_tyoku_2(sub_ty) != None:
          if oya_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(oya_tyoku_2(sub_ty))
        if oya_tyoku_3(sub_ty) != None:      
          if oya_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(oya_tyoku_3(sub_ty))
        if oya_tyoku_4(sub_ty) != None:
          if oya_tyoku_3(sub_ty) != "3飜20符":
            list_ty.append(oya_tyoku_4(sub_ty))
        if oya_tyoku_4(sub_ty) == None:
          list_ty.append(oya_tyoku_ov5(sub_ty))
        
        if oya_ron_1(sub_ro) != None:
          list_ro.append(oya_ron_1(sub_ro))
        if oya_ron_2(sub_ro) != None:
          if oya_ron_1(sub_ro) != "1飜30符":
            list_ro.append(oya_ron_2(sub_ro))
        if oya_ron_3(sub_ro) != None:      
          if oya_ron_2(sub_ro) != "2飜20符":
            list_ro.append(oya_ron_3(sub_ro))
        if oya_ron_4(sub_ro) != None:
          if oya_ron_3(sub_ro) != "3飜20符":
            list_ro.append(oya_ron_4(sub_ro))
        if oya_ron_4(sub_ro) == None:
          list_ro.append(oya_ron_ov5(sub_ro))
      
      else:
        if ko_tsumo_notk_1(sub_ts) != None:
          list_ts.append(ko_tsumo_notk_1(sub_ts))
        if ko_tsumo_notk_2(sub_ts) != None:
          if ko_tsumo_notk_1(sub_ts) != "1飜30符":
            list_ts.append(ko_tsumo_notk_2(sub_ts))
        if ko_tsumo_notk_3(sub_ts) != None:      
          if ko_tsumo_notk_2(sub_ts) != "2飜20符":
            list_ts.append(ko_tsumo_notk_3(sub_ts))
        if ko_tsumo_notk_4(sub_ts) != None:
            if ko_tsumo_notk_3(sub_ts) != "3飜20符":
              list_ts.append(ko_tsumo_notk_4(sub_ts))
        if ko_tsumo_notk_4(sub_ts) == None:
          list_ts.append(ko_tsumo_notk_ov5(sub_ts))
        
        if ko_tyoku_1(sub_ty) != None:
          list_ty.append(ko_tyoku_1(sub_ty))
        if ko_tyoku_2(sub_ty) != None:
          if ko_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(ko_tyoku_2(sub_ty))
        if ko_tyoku_3(sub_ty) != None:      
          if ko_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(ko_tyoku_3(sub_ty))
        if ko_tyoku_4(sub_ty) != None:
            if ko_tyoku_3(sub_ty) != "3飜20符":
              list_ty.append(ko_tyoku_4(sub_ty))
        if ko_tyoku_4(sub_ty) == None:
          list_ty.append(ko_tyoku_ov5(sub_ty))
        
        if ko_ron_1(sub_ro) != None:
          list_ro.append(ko_ron_1(sub_ro))
        if ko_ron_2(sub_ro) != None:
          if ko_ron_1(sub_ro) != "1飜30符":
            list_ro.append(ko_ron_2(sub_ro))
        if ko_ron_3(sub_ro) != None:      
          if ko_ron_2(sub_ro) != "2飜20符":
            list_ro.append(ko_ron_3(sub_ro))
        if ko_ron_4(sub_ro) != None:
            if ko_ron_3(sub_ro) != "3飜20符":
              list_ro.append(ko_ron_4(sub_ro))
        if ko_ron_4(sub_ro) == None:
          list_ro.append(ko_ron_ov5(sub_ro))

      print("ツモ:", " or ".join(list_ts))
      print("直撃:", " or ".join(list_ty))
      print("ロン:", " or ".join(list_ro))


      print("2位条件:")
      sub_ts = tsumo(sit[2], sit[4])
      sub_ty = tyoku(sit[2], sit[4])
      sub_ro = ron(sit[2], sit[4])
      list_ts = []
      list_ty = []
      list_ro = []
      if oya == 2:
        if ko_tsumo_kaburi_1(sub_ts) != None:
          list_ts.append(ko_tsumo_kaburi_1(sub_ts))
        if ko_tsumo_kaburi_2(sub_ts) != None:
          if ko_tsumo_kaburi_1(sub_ts) != "1飜30符":
            list_ts.append(ko_tsumo_kaburi_2(sub_ts))
        if ko_tsumo_kaburi_3(sub_ts) != None:      
          if ko_tsumo_kaburi_2(sub_ts) != "2飜20符":
            list_ts.append(ko_tsumo_kaburi_3(sub_ts))
        if ko_tsumo_kaburi_4(sub_ts) != None:
            if ko_tsumo_kaburi_3(sub_ts) != "3飜20符":
              list_ts.append(ko_tsumo_kaburi_4(sub_ts))
        if ko_tsumo_kaburi_4(sub_ts) == None:
          list_ts.append(ko_tsumo_kaburi_ov5(sub_ts))
        
        if ko_tyoku_1(sub_ty) != None:
          list_ty.append(ko_tyoku_1(sub_ty))
        if ko_tyoku_2(sub_ty) != None:
          if ko_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(ko_tyoku_2(sub_ty))
        if ko_tyoku_3(sub_ty) != None:      
          if ko_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(ko_tyoku_3(sub_ty))
        if ko_tyoku_4(sub_ty) != None:
            if ko_tyoku_3(sub_ty) != "3飜20符":
              list_ty.append(ko_tyoku_4(sub_ty))
        if ko_tyoku_4(sub_ty) == None:
          list_ty.append(ko_tyoku_ov5(sub_ty))
        
        if ko_ron_1(sub_ro) != None:
          list_ro.append(ko_ron_1(sub_ro))
        if ko_ron_2(sub_ro) != None:
          if ko_ron_1(sub_ro) != "1飜30符":
            list_ro.append(ko_ron_2(sub_ro))
        if ko_ron_3(sub_ro) != None:      
          if ko_ron_2(sub_ro) != "2飜20符":
            list_ro.append(ko_ron_3(sub_ro))
        if ko_ron_4(sub_ro) != None:
            if ko_ron_3(sub_ro) != "3飜20符":
              list_ro.append(ko_ron_4(sub_ro))
        if ko_ron_4(sub_ro) == None:
          list_ro.append(ko_ron_ov5(sub_ro))
      
      elif oya == 4:
        if oya_tsumo_1(sub_ts) != None:
          list_ts.append(oya_tsumo_1(sub_ts))
        if oya_tsumo_2(sub_ts) != None:
          if oya_tsumo_1(sub_ts) != "1飜30符":
            list_ts.append(oya_tsumo_2(sub_ts))
        if oya_tsumo_3(sub_ts) != None:      
          if oya_tsumo_2(sub_ts) != "2飜20符":
            list_ts.append(oya_tsumo_3(sub_ts))
        if oya_tsumo_4(sub_ts) != None:
          if oya_tsumo_3(sub_ts) != "3飜20符":
            list_ts.append(oya_tsumo_4(sub_ts))
        if oya_tsumo_4(sub_ts) == None:
          list_ts.append(oya_tsumo_ov5(sub_ts))
        
        if oya_tyoku_1(sub_ty) != None:
          list_ty.append(oya_tyoku_1(sub_ty))
        if oya_tyoku_2(sub_ty) != None:
          if oya_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(oya_tyoku_2(sub_ty))
        if oya_tyoku_3(sub_ty) != None:      
          if oya_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(oya_tyoku_3(sub_ty))
        if oya_tyoku_4(sub_ty) != None:
          if oya_tyoku_3(sub_ty) != "3飜20符":
            list_ty.append(oya_tyoku_4(sub_ty))
        if oya_tyoku_4(sub_ty) == None:
          list_ty.append(oya_tyoku_ov5(sub_ty))
        
        if oya_ron_1(sub_ro) != None:
          list_ro.append(oya_ron_1(sub_ro))
        if oya_ron_2(sub_ro) != None:
          if oya_ron_1(sub_ro) != "1飜30符":
            list_ro.append(oya_ron_2(sub_ro))
        if oya_ron_3(sub_ro) != None:      
          if oya_ron_2(sub_ro) != "2飜20符":
            list_ro.append(oya_ron_3(sub_ro))
        if oya_ron_4(sub_ro) != None:
          if oya_ron_3(sub_ro) != "3飜20符":
            list_ro.append(oya_ron_4(sub_ro))
        if oya_ron_4(sub_ro) == None:
          list_ro.append(oya_ron_ov5(sub_ro))
      
      else:
        if ko_tsumo_notk_1(sub_ts) != None:
          list_ts.append(ko_tsumo_notk_1(sub_ts))
        if ko_tsumo_notk_2(sub_ts) != None:
          if ko_tsumo_notk_1(sub_ts) != "1飜30符":
            list_ts.append(ko_tsumo_notk_2(sub_ts))
        if ko_tsumo_notk_3(sub_ts) != None:      
          if ko_tsumo_notk_2(sub_ts) != "2飜20符":
            list_ts.append(ko_tsumo_notk_3(sub_ts))
        if ko_tsumo_notk_4(sub_ts) != None:
            if ko_tsumo_notk_3(sub_ts) != "3飜20符":
              list_ts.append(ko_tsumo_notk_4(sub_ts))
        if ko_tsumo_notk_4(sub_ts) == None:
          list_ts.append(ko_tsumo_notk_ov5(sub_ts))
        
        if ko_tyoku_1(sub_ty) != None:
          list_ty.append(ko_tyoku_1(sub_ty))
        if ko_tyoku_2(sub_ty) != None:
          if ko_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(ko_tyoku_2(sub_ty))
        if ko_tyoku_3(sub_ty) != None:      
          if ko_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(ko_tyoku_3(sub_ty))
        if ko_tyoku_4(sub_ty) != None:
            if ko_tyoku_3(sub_ty) != "3飜20符":
              list_ty.append(ko_tyoku_4(sub_ty))
        if ko_tyoku_4(sub_ty) == None:
          list_ty.append(ko_tyoku_ov5(sub_ty))
        
        if ko_ron_1(sub_ro) != None:
          list_ro.append(ko_ron_1(sub_ro))
        if ko_ron_2(sub_ro) != None:
          if ko_ron_1(sub_ro) != "1飜30符":
            list_ro.append(ko_ron_2(sub_ro))
        if ko_ron_3(sub_ro) != None:      
          if ko_ron_2(sub_ro) != "2飜20符":
            list_ro.append(ko_ron_3(sub_ro))
        if ko_ron_4(sub_ro) != None:
            if ko_ron_3(sub_ro) != "3飜20符":
              list_ro.append(ko_ron_4(sub_ro))
        if ko_ron_4(sub_ro) == None:
          list_ro.append(ko_ron_ov5(sub_ro))

      print("ツモ:", " or ".join(list_ts))
      print("直撃:", " or ".join(list_ty))
      print("ロン:", " or ".join(list_ro)) 

      print("3位条件:")
      sub_ts = tsumo(sit[3], sit[4])
      sub_ty = tyoku(sit[3], sit[4])
      sub_ro = ron(sit[3], sit[4])
      list_ts = []
      list_ty = []
      list_ro = []
      if oya == 3:
        if ko_tsumo_kaburi_1(sub_ts) != None:
          list_ts.append(ko_tsumo_kaburi_1(sub_ts))
        if ko_tsumo_kaburi_2(sub_ts) != None:
          if ko_tsumo_kaburi_1(sub_ts) != "1飜30符":
            list_ts.append(ko_tsumo_kaburi_2(sub_ts))
        if ko_tsumo_kaburi_3(sub_ts) != None:      
          if ko_tsumo_kaburi_2(sub_ts) != "2飜20符":
            list_ts.append(ko_tsumo_kaburi_3(sub_ts))
        if ko_tsumo_kaburi_4(sub_ts) != None:
            if ko_tsumo_kaburi_3(sub_ts) != "3飜20符":
              list_ts.append(ko_tsumo_kaburi_4(sub_ts))
        if ko_tsumo_kaburi_4(sub_ts) == None:
          list_ts.append(ko_tsumo_kaburi_ov5(sub_ts))
        
        if ko_tyoku_1(sub_ty) != None:
          list_ty.append(ko_tyoku_1(sub_ty))
        if ko_tyoku_2(sub_ty) != None:
          if ko_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(ko_tyoku_2(sub_ty))
        if ko_tyoku_3(sub_ty) != None:      
          if ko_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(ko_tyoku_3(sub_ty))
        if ko_tyoku_4(sub_ty) != None:
            if ko_tyoku_3(sub_ty) != "3飜20符":
              list_ty.append(ko_tyoku_4(sub_ty))
        if ko_tyoku_4(sub_ty) == None:
          list_ty.append(ko_tyoku_ov5(sub_ty))
        
        if ko_ron_1(sub_ro) != None:
          list_ro.append(ko_ron_1(sub_ro))
        if ko_ron_2(sub_ro) != None:
          if ko_ron_1(sub_ro) != "1飜30符":
            list_ro.append(ko_ron_2(sub_ro))
        if ko_ron_3(sub_ro) != None:      
          if ko_ron_2(sub_ro) != "2飜20符":
            list_ro.append(ko_ron_3(sub_ro))
        if ko_ron_4(sub_ro) != None:
            if ko_ron_3(sub_ro) != "3飜20符":
              list_ro.append(ko_ron_4(sub_ro))
        if ko_ron_4(sub_ro) == None:
          list_ro.append(ko_ron_ov5(sub_ro))
      
      elif oya == 4:
        if oya_tsumo_1(sub_ts) != None:
          list_ts.append(oya_tsumo_1(sub_ts))
        if oya_tsumo_2(sub_ts) != None:
          if oya_tsumo_1(sub_ts) != "1飜30符":
            list_ts.append(oya_tsumo_2(sub_ts))
        if oya_tsumo_3(sub_ts) != None:      
          if oya_tsumo_2(sub_ts) != "2飜20符":
            list_ts.append(oya_tsumo_3(sub_ts))
        if oya_tsumo_4(sub_ts) != None:
          if oya_tsumo_3(sub_ts) != "3飜20符":
            list_ts.append(oya_tsumo_4(sub_ts))
        if oya_tsumo_4(sub_ts) == None:
          list_ts.append(oya_tsumo_ov5(sub_ts))
        
        if oya_tyoku_1(sub_ty) != None:
          list_ty.append(oya_tyoku_1(sub_ty))
        if oya_tyoku_2(sub_ty) != None:
          if oya_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(oya_tyoku_2(sub_ty))
        if oya_tyoku_3(sub_ty) != None:      
          if oya_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(oya_tyoku_3(sub_ty))
        if oya_tyoku_4(sub_ty) != None:
          if oya_tyoku_3(sub_ty) != "3飜20符":
            list_ty.append(oya_tyoku_4(sub_ty))
        if oya_tyoku_4(sub_ty) == None:
          list_ty.append(oya_tyoku_ov5(sub_ty))
        
        if oya_ron_1(sub_ro) != None:
          list_ro.append(oya_ron_1(sub_ro))
        if oya_ron_2(sub_ro) != None:
          if oya_ron_1(sub_ro) != "1飜30符":
            list_ro.append(oya_ron_2(sub_ro))
        if oya_ron_3(sub_ro) != None:      
          if oya_ron_2(sub_ro) != "2飜20符":
            list_ro.append(oya_ron_3(sub_ro))
        if oya_ron_4(sub_ro) != None:
          if oya_ron_3(sub_ro) != "3飜20符":
            list_ro.append(oya_ron_4(sub_ro))
        if oya_ron_4(sub_ro) == None:
          list_ro.append(oya_ron_ov5(sub_ro))
      
      else:
        if ko_tsumo_notk_1(sub_ts) != None:
          list_ts.append(ko_tsumo_notk_1(sub_ts))
        if ko_tsumo_notk_2(sub_ts) != None:
          if ko_tsumo_notk_1(sub_ts) != "1飜30符":
            list_ts.append(ko_tsumo_notk_2(sub_ts))
        if ko_tsumo_notk_3(sub_ts) != None:      
          if ko_tsumo_notk_2(sub_ts) != "2飜20符":
            list_ts.append(ko_tsumo_notk_3(sub_ts))
        if ko_tsumo_notk_4(sub_ts) != None:
            if ko_tsumo_notk_3(sub_ts) != "3飜20符":
              list_ts.append(ko_tsumo_notk_4(sub_ts))
        if ko_tsumo_notk_4(sub_ts) == None:
          list_ts.append(ko_tsumo_notk_ov5(sub_ts))
        
        if ko_tyoku_1(sub_ty) != None:
          list_ty.append(ko_tyoku_1(sub_ty))
        if ko_tyoku_2(sub_ty) != None:
          if ko_tyoku_1(sub_ty) != "1飜30符":
            list_ty.append(ko_tyoku_2(sub_ty))
        if ko_tyoku_3(sub_ty) != None:      
          if ko_tyoku_2(sub_ty) != "2飜20符":
            list_ty.append(ko_tyoku_3(sub_ty))
        if ko_tyoku_4(sub_ty) != None:
            if ko_tyoku_3(sub_ty) != "3飜20符":
              list_ty.append(ko_tyoku_4(sub_ty))
        if ko_tyoku_4(sub_ty) == None:
          list_ty.append(ko_tyoku_ov5(sub_ty))
        
        if ko_ron_1(sub_ro) != None:
          list_ro.append(ko_ron_1(sub_ro))
        if ko_ron_2(sub_ro) != None:
          if ko_ron_1(sub_ro) != "1飜30符":
            list_ro.append(ko_ron_2(sub_ro))
        if ko_ron_3(sub_ro) != None:      
          if ko_ron_2(sub_ro) != "2飜20符":
            list_ro.append(ko_ron_3(sub_ro))
        if ko_ron_4(sub_ro) != None:
            if ko_ron_3(sub_ro) != "3飜20符":
              list_ro.append(ko_ron_4(sub_ro))
        if ko_ron_4(sub_ro) == None:
          list_ro.append(ko_ron_ov5(sub_ro))

      print("ツモ:", " or ".join(list_ts))
      print("直撃:", " or ".join(list_ty))
      print("ロン:", " or ".join(list_ro)) 

  print("""
""")
