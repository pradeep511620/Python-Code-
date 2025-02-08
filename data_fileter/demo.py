import csv
import pymysql

from fractions import Fraction

obj1 = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="data_filter"
)
print("Database Connection ")
mycursor = obj1.cursor()

filename = "/home/pradeep/Downloads/csv/Locknuts_23nov.csv"
with open(filename, 'r', encoding='utf-8') as f:
    data = csv.reader(f)
    # for x in data:
    #     print(x)

    # for row in data:
    #     sql = "INSERT INTO Locknuts (MPN, L3, DataType, SuperAtt, Type, ATTRIBUTE, VALUE, PreP, value1, unit1, PostP, value2, unit2, key_value) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #     val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
    #     mycursor.execute(sql, val)
    # print("Insert Into Data")
    # obj1.commit()
    #      # Insert data into table

sql1 = "SELECT * from Locknuts "
mycursor.execute(sql1)
myresult = mycursor.fetchall()
# print(myresult)

for z in myresult:
    id = z[0]
    p = z[3]  # data type
    a = z[6]  # attribute
    f = z[10]  # value1 into update this variable
    x = z[7]  # row_value ("")
    # print(":",x)

    # ===========================================  Discrete and  Varchar =============================================
    if p == "Discrete" or p == "Varchar" or p == "varchar" or p == "VarChar":
        s = x
        # print(x)
        val = (s, id)
        # print(val)
        sql = "Update Locknuts set value1 = %s where id = %s"
        mycursor.execute(sql, val)
        # print("Varchar, Discrete")

    # ================================================= inch ========================================================
    if '"' in x and "-" not in x:
        inch = "inch"
        val = (inch, id)
        # print(val)
        sql = "UPDATE Locknuts SET unit1=%s WHERE id=%s"
        mycursor.execute(sql, val)
        # print("inch")
        # obj1.commit()
    # ================================================= rp_25 lbs. ==================================================
    if " lbs." in x:                                     # rp_25 lbs. results value1 = rp_25 and unit1 = lbs.
        lb = x.split(" ")[0]
        lb1 = x.split(" ")[1]
        val = (lb, lb1, id)
        # print(val)
    #     sql = "UPDATE Locknuts SET value1=%s, unit1=%s WHERE id=%s"
    #     mycursor.execute(sql, val)
    #     print("lbs.")
    # obj1.commit()

    # =============================================== rp_82 Deg. ====================================================
    if "Deg." in x:                                   # rp_82 Deg.  results: value1 = rp_82 and unit1 = Deg.
        d = x.split(" ")[0]
        d1 = x.split(" ")[1]
        val = (d, d1, id)
        # print(val)
        sql = "UPDATE Locknuts SET value1=%s, unit1=%s WHERE id=%s"
        mycursor.execute(sql, val)
        # print("Deg")
        # obj1.commit()

    # ==============================================='rp_1" results = rp_1 ======================================
    if "Base Dia." in a and "_" in x and "/" not in x and "mm" not in x:            # 'rp_1"    results = rp_1
        l = x.split('"')[0]
        val = (l, id)
        # print(val)
        # sql = "UPDATE Weld_Nuts SET value1=%s WHERE id=%s"
        # mycursor.execute(sql, val)
        # print("rp_1")
        # obj1.commit()

    # ========================================= rp_No.23 ======================================================
    if "rp_No." in x:                           # rp_No. 7 results: value1 = rp_7 and PreP = NO.
        r = x.replace("No. ", "")  # rp_7
        no = "NO"
        val = (no, r, id)
        # print(val)
        # sql = "UPDATE Locknuts SET PreP=%s, value1=%s  WHERE id=%s"
        # mycursor.execute(sql, val)
        # print("NO', 'rp_8")
        # obj1.commit()

    # ============================================= rp_8mm ======================================================
    if "mm" in x:                               # rp_8mm results = value1 = rp_8 and unit1 = mm
        u = x.split("mm")[0]
        mm = "mm"
        val = (u, mm, id)
        # print(val)
        sql = "UPDATE Locknuts SET value1=%s, unit1=%s WHERE id=%s"
        mycursor.execute(sql, val)
        # print("mm")
        # obj1.commit()
    if "mm" in x and "." in x:
        mm = x.split(" ")[0]
        mm1 = x.split(" ")[1]
        val = (mm, mm1, id)
        # print(val)
        # sql = "UPDATE Locknuts SET value1=%s, unit1=%s WHERE id=%s"
        # mycursor.execute(sql, val)
        # print("mm")
        # obj1.commit()

    # ==============================================  rp_731814.0000 ==============================================
    if '000' in x:                                     # rp_731814.0000 result: value1 = rp_731814.0000
        s = x
        val = (s, id)
        # print(val)
        sql = "UPDATE Locknuts SET value1=%s WHERE id=%s"
        mycursor.execute(sql, val)
        # print("rp_731814.0000")
        # obj1.commit()

    # ==========================================  rp_#10 ======================================
    if "_#" in x and "-" not in x:                # rp_#6   results:  PreP = # and value1 = rp_6
        g = x.replace("#", "")
        val = (g, id)
        # print(val)
        sql = "Update Locknuts set value1 = %s where id = %s"
        mycursor.execute(sql, val)
        # print("rp_10")
        # obj1.commit()

    # ================================================ rp_0.138" ==================================================
    if "_0." in x:                                     # rp_0.138" results: value = rp_0.138 and unit1 = inch
        c = x.split('"')[0]
        val = (c, id)
        # print(val)
        sql = "Update Locknuts set value1 = %s where id = %s"
        mycursor.execute(sql, val)
        # print("rp_0.138")
        # obj1.commit()
    # =================================================  rp_1 3/4" ===============================================
    if "/" in x and '"' in x and "-" not in x:           # rp_1 3/4"  results: value1 = rp_0.62 and unit1 = inch
        # print(x)
        f = x.split("rp_")[1]
        f2 = f.split('"')[0]
        f3 = f2.replace(" ", "+")
        rp = "rp_"
        d = round(float(eval(f3)), 2)
        ad = rp + str(d)
        val = (ad, id)
        #     print(val)
        sql = "UPDATE Locknuts SET value1=%s WHERE id=%s"
        mycursor.execute(sql, val)
    #     print("rp_0.62")
    # obj1.commit()

    # ========================================= Thread Dia  # rp_#6-32 ==============================================
    if "Thread Dia." in a and "-" in x and "/" not in x:        # rp_#6-32    results: value1 = rp_6 and Prep = #
        per = x.split("-")[0]  # rp_#10
        pe = per.replace("#", "")
        H = "#"
        val = (H, pe, id)
        # print(val)
        sql = "Update Locknuts set PreP=%s, value1=%s where id = %s"
        mycursor.execute(sql, val)
    #     print("#', 'rp_10")
    # obj1.commit()

    # ==================================== Thread Per Inch  # rp_#6-32 =============================================
    if "#" in x and "-" in x and "," not in x:              # rp_#6-32   results: value1 = rp_32 and PreP = #
        per = x.split("-")[1]
        per1 = x.split("#")[0]
        H = "#"
        ad = per1 + per
        val = (H, ad, id)
        # print(val)
        sql = "Update Locknuts set PreP=%s, value1=%s where id = %s"
        mycursor.execute(sql, val)
        # print("kk")
        # obj1.commit()

    # ==================================== Thread Dia. # rp_1/4"-20 =================================================
    if "Thread Dia." in a and '"-' in x and "," not in x:       # rp_1/4"-20 results value1 = rp_0.25 unit1 = inch
        th = x.split('rp_')[1]  # 1/4"-20
        th1 = th.split('"-')[0]  # 1/4
        rp = "rp_"
        inch = "inch"
        # print(th1)
        th2 = th1.replace(" ", "+")
        d = round(float(eval(th2)), 2)
        ad = rp + str(d)  # rp_0.31
        val = (ad, inch, id)
        # print(val)
        sql = "Update Locknuts set value1=%s, unit1=%s where id = %s"
        mycursor.execute(sql, val)
        # print("rp_0.31', 'inch")
    # obj1.commit()

    # ==================================== Thread Per Inch =========================================================
    if "Thread Per Inch" in a and '"-' in x and "," not in x:   # rp_1/4"-20      results: value1 = rp_20
        per = x.split("-")[1]
        rp = "rp_"
        ad = rp + per
        val = (ad, id)
        # print(val)
        sql = "Update Locknuts set value1 = %s where id = %s"
        mycursor.execute(sql, val)
        # print("Thread Per inch")
        # obj1.commit()

    #  ============================================== Thread Dia. ==================================================
    if "M" in x and "Thread Dia." in a:         # rp_M4 x 0.7  results: value1 = rp_4 and PreP = M unit1 = mm
        da = x.split(" ")[0]
        da1 = da.replace("M", "")
        M = "M"
        mm = "mm"
        val = (M, da1, mm, id)
        # print(val)
        sql = "Update Locknuts set PreP=%s, value1=%s, unit1=%s where id = %s"
        mycursor.execute(sql, val)
        # print("M', 'rp_4")
        # obj1.commit()

    # ===================================== Thread Pitch ============================================================
    if 'M' in x and "Thread Pitch" in a:  # rp_M1.4 x 0.3      results: value1 = rp_0.3
        p = x.split("x ")[1]
        rp = "rp_"
        ad = rp + p
        val = (ad, id)
        # print(val)
        sql = "Update Locknuts set value1 = %s where id = %s"
        mycursor.execute(sql, val)
        # print("Thread Pitch")
        # obj1.commit()
    # ===================================== Range 1 rp_-40 Deg. To 180 Deg. F =======================================
    if "Deg. F" in x:  # rp_Not Rated to 220 Deg. F results: value1 = rp_Not Rated and value2 rp_220 and unit2 = Deg.F
        # print(x)
        f = x.split(" ")[0]
        f1 = x.split(" ")[1]
        f3 = x.split(" ")[3]
        f4 = x.split(" ")[4]
        rp = "rp_"
        F = "F"
        ff = f + f1
        ad = rp + f3
        FF = f4 + F
        val = (ff, ad, FF, id)
        # print(val)
        sql = "update Locknuts set value1=%s ,value2=%s ,unit2=%s  WHERE id=%s"
        mycursor.execute(sql, val)
obj1.commit()

# ========================== Range 1 rp_-40 Deg. To 180 Deg. F ====================================
#     if "Deg. F" in x:  # rp_-40 Deg. To 180 Deg. F
#         r = x.split(" ")[0]  # rp_-40
#         r1 = x.split(" ")[1]  # Deg.
#         r3 = x.split(" ")[3]  # 180
#         r4 = x.split(" ")[5]  # F
#         re = r.replace("-", "")  # rp_40
#         t = r1 + r4  # Deg.F
#         rp = "rp_"
#         m = "-"
#         p = "+"
#         g = "0"
#         ad = rp + r3
#         val = (m, re, t, p, ad, t, id)
#         print(val)
#         sql = "update Locknuts set PreP=%s, value1=%s ,unit1=%s ,PostP=%s ,value2=%s ,unit2=%s  WHERE id=%s"
#         mycursor.execute(sql, val)
#         obj1.commit()

# ========================================= Range 1   rp_0.000" to 0.002 ===========================================
#     if "Range 1" in p and "to" in x:  # rp_0.000" to 0.002"
#         ra = x.split("to")[0]
#         r1 = x.split("to")[1]
#         r2 = r1.split('"')[0]
#         r3 = r2.replace(" ", "")
#         rp = "rp_"
#         ad = rp + r3
#         ra1 = ra.split('"')[0]
#         ra7 = ra1.replace("-", "")
#         p = "+"
#         p1 = "+"
#         val = (p, ad, p1, ra7, id)
#         print(val)
#         sql = "UPDATE Bolts SET PreP=%s, value1=%s,PostP=%s, value2=%s WHERE id=%s"
#         mycursor.execute(sql, val)
#         print("Range 1")
# obj1.commit()

# ========================= Thread Per Inch ===================== range 2 ==========
#     if "Range 2" in p and "#" in x and "," in x:
#         rp = "rp_"
#         ran = x.split(" ")[0]
#         ra = ran.split("-")[1].replace(",", "")
#         ad = rp + ra
#         o = "1"
#         val = (o, ad, id)
#         # print(val)
#         sql = "Update Wing set PreP=%s value1=%s, unit1=%s where id = %s"
#         mycursor.execute(sql, val)

# ran1 = x.split(" ")[1]
# ra1 = ran1.split("-")[1].replace(",", "").replace("#8-", "")
# ad1 = rp + ra1
# t = "2"
# val1 = (t, ad1, id)
# print(val1)
# sql = "UPDATE Wing SET PreP=%s, value1=%s, key_value=%s WHERE id=%s"
# mycursor.execute(sql, val)
# # print(ad1)
#
# ran2 = x.split(" ")[2]
# ra2 = ran2.split("-")[1].replace(",", "").replace("#10-", "")
# ad2 = rp + ra2
# th = "3"
# val2 = (th, ad2, id)
# print(val2)
# sql = "UPDATE Wing SET PreP=%s, value1=%s, key_value=%s WHERE id=%s"
# mycursor.execute(sql, val)
#
# ran3 = x.split(" ")[3]
# ra3 = ran3.split("-")[1].replace(",", "").replace("#1/4-", "")
# ad3 = rp + ra3
# f = "4"
# val3 = (f, ad3, id)
# print(val3)
# sql = "UPDATE Wing SET PreP=%s, value1=%s, key_value=%s WHERE id=%s"
# mycursor.execute(sql, val)
#
# ran4 = x.split(" ")[4]
# ra4 = ran4.split("-")[1].replace(",", "").replace("5/16", "")
# ad4 = rp + ra4
# fi = "5"
# val4 = (fi, ad4, id)
# print(val4)
# sql = "UPDATE Wing SET PreP=%s, value1=%s, key_value=%s WHERE id=%s"
# mycursor.execute(sql, val)
#
# ran5 = x.split(" ")[5]
# ra5 = ran5.split("-")[1].replace(",", "").replace("3/8-", "")
# ad5 = rp + ra5
# si = "6"
# val5 = (si, ad5, id)
# sql = "UPDATE Wing SET PreP=%s, value1=%s, key_value=%s WHERE id=%s"
# mycursor.execute(sql, val)
# print(val5)


"""
# ========================================= RANGE 2  rp_#2, M2 ======================================================
    if "Range2" in p and '#' in x:
        # print(x)
        u = x.split(",")[0]
        u1 = u.replace("#", "")
        h = "#"
        key1 = "1"
        val = (h, u1, key1, id)
        print(val)
        # sql = "UPDATE Retaining SET PreP=%s, value1=%s, key_value=%s WHERE id=%s"
        # mycursor.execute(sql, val)
    if "Range2" in p and '#' in x:
        i = x.split("#")[0]
        i1 = x.split("M")[1]
        M = "M"
        ad1 = i + i1
        mm = "mm"
        key2 = "2"
        mpn = z[1]
        val1 = (M, ad1, mm, key2, mpn)
        # print(val1)
        # sql1 = "INSERT INTO Retaining (PreP, value1, unit1, key_value,MPN) values(%s,%s,%s,%s,%s)"
        # mycursor.execute(sql1, val1)
        # obj1.commit()
"""

"""
#     if p == "Numerical":
#         n = x
#         # print(n)
#
#     if "mm" in x:
#         u = x.split("mm")[0]
#         mm = "mm"
#         val = (u, mm, id)
#         # print(val)
#         sql = "UPDATE Thread_Forming SET value1=%s, unit1=%s WHERE id=%s"
#         mycursor.execute(sql, val)
#     # obj1.commit()
#     if '"' in x and "to" not in x:
#         inch = "inch"
#         val = (inch, id)
#         # print(val)
#         sql = "UPDATE Thread_Forming SET unit1=%s WHERE id=%s"
#         mycursor.execute(sql, val)
#         # print(x)
#         # obj1.commit()
#
#     if "ga" in x:
#         g = "ga"
#         val = (g, id)
#         # print(val)
#         sql = "UPDATE Thread_Forming SET unit1=%s WHERE id=%s"
#         mycursor.execute(sql, val)
#
#     if '00' in x:
#         s = x
#         val = (s, id)
#         # print(val)
#         sql = "UPDATE Thread_Forming SET value1=%s WHERE id=%s"
#         mycursor.execute(sql, val)
#
#     if "/" in x and '"' in x:                                                           # rp_1 3/4"
#         f = x.split("rp_")[1]
#         f2 = f.split('"')[0]
#         f3 = f2.replace(" ", "+")
#         rp = "rp_"
#         d = round(float(eval(f3)), 2)
#         ad = rp + str(d)
#         val = (ad, id)
#         # print(val)
#         sql = "UPDATE Thread_Forming SET value1=%s WHERE id=%s"
#         mycursor.execute(sql, val)
#         # obj1.commit()
#
#     if "/" in x and '"' in x:
#         f = x.split("rp_")[1]
#         f1 = f.split('"')[0]
#         f2 = f1.split(" ga")[0]
#         # print(f2)
#         f3 = f2.replace(" ", "+")
#         rp = "rp_"
#         d = round(float(eval(f3)), 2)
#         ad = rp + str(d)
#         val = (ad, id)
#         # print(val)
#         sql = "UPDATE Thread_Forming SET value1=%s WHERE id=%s"
#         mycursor.execute(sql, val)
#
#     if "." in x and "/" not in x and "00" not in x and "png" not in x:
#         # print(x)
#         d = x.split('"')[0]
#         d1 = d.replace("ga.", "")
#         val = (d1, id)
#         # print(val)
#         sql = "UPDATE Thread_Forming SET value1=%s WHERE id=%s"
#         mycursor.execute(sql, val)
#
#     if "d" in x and " " not in x and "R" not in x:                              # rp_8d
#         d = x.split("d")[0]
#         val = (d, id)
#         # print(val)
#         sql = "UPDATE Thread_Forming SET value1=%s WHERE id=%s"
#         mycursor.execute(sql, val)
#
#     if '"' in x and "." not in x and "/" not in x:                               # rp_3"
#         t = x.split('"')[0]
#         val = (t, id)
#         # print(val)
#         sql = "UPDATE Thread_Forming SET value1=%s WHERE id=%s"
#         mycursor.execute(sql, val)
#
#     if "rp_11" in x:                                                               # rp_11
#         e = x
#         val = (e, id)
#         # print(val)
#         sql = "UPDATE Thread_Forming SET value1=%s WHERE id=%s"
#         mycursor.execute(sql, val)
#     # obj1.commit()


"""
"""
    # ========================================= RANGE 2  rp_#2, M2 ======================================================
    if "Range2" in p and '#' in x:
        # print(x)
        u = x.split(",")[0]
        u1 = u.replace("#", "")
        h = "#"
        key1 = "1"
        val = (h, u1, key1, id)
        # print(val)
        sql = "UPDATE Retaining SET PreP=%s, value1=%s, key_value=%s WHERE id=%s"
        mycursor.execute(sql, val)
    if "Range2" in p and '#' in x:
        i = x.split("#")[0]
        i1 = x.split("M")[1]
        M = "M"
        ad1 = i + i1
        mm = "mm"
        key2 = "2"
        mpn = z[1]
        val1 = (M, ad1, mm, key2, mpn)
        # print(val1)
        sql1 = "INSERT INTO Retaining (PreP, value1, unit1, key_value,MPN) values(%s,%s,%s,%s,%s)"
        mycursor.execute(sql1, val1)
obj1.commit()
"""


"""
# ========================================= RANGE 2  rp_1/4", M6 ======================================================
# ======================================UPDATE INTO TABLE RANGE 2 =====================================================
    if "Range2" in p and '",' in x:                          # rp_1/4", M6
        u = x.split("rp_")[1]   # 1/4", M6
        u1 = u.split('",')[0]   # 1/4 and 1/4
        d = round(float(eval(u1)), 2)                       # 0.25  and 0.25
        rp = "rp_"
        ad = rp + str(d)                                    # rp_0.25 and rp_0.25
        inch = "inch"
        key1 = "1"
        val = (ad, inch, key1, id)
        print(val)
        sql = "UPDATE Retaining SET value1=%s, unit1=%s, key_value=%s WHERE id=%s"
        mycursor.execute(sql, val)
        # print("UPDATE")
    # obj1.commit()
# ======================================= INSERT INTO TABLE RANGE 2=====================================================
    if "Range2" in p and '",' in x:                          # rp_1/4", M6
        s = x.split("rp_")[1]                                # 1/4", M6 , like this value
        k = x.split("M")[1]                                  # 6 and 8
        rp = "rp_"
        ad1 = rp + k                                         # rp_6 and rp_8
        M = "M"
        mm = "mm"
        key2 = "2"
        mpn = z[1]
        val1 = (M, ad1, mm, key2, mpn)
        sql1 = "INSERT INTO Retaining (PreP, value1, unit1, key_value,MPN) values(%s,%s,%s,%s,%s)"
        mycursor.execute(sql1, val1)
        # print("INSERT")
# obj1.commit()
"""  # RANGE 2  rp_1/4", M6

"""    
    if "rp_No." in x:               # rp_No. 7
        r = x.replace("No. ", "")   # rp_7
        no = "NO"
        val = (no, r, id)
        # print(val)
        sql = "UPDATE Plow_Bolts SET PreP=%s, value1=%s  WHERE id=%s"
        mycursor.execute(sql, val)

    if "000" in x and "psi" not in x:           # rp_731815.2000
        k = x
        val = (k, id)
        # print(val)
        sql = "UPDATE Plow_Bolts SET value1=%s  WHERE id=%s"
        mycursor.execute(sql, val)
    if "Deg." in x:                             # rp_82 Deg.
        d = x.split(" ")[0]
        d1 = x.split(" ")[1]
        val = (d, d1, id)
        # print(val)
        sql = "UPDATE Plow_Bolts SET value1=%s, unit1=%s  WHERE id=%s"
        mycursor.execute(sql, val)    

    if "psi" in x:                      # rp_120,000 psi
        p = x.split(" ")[0]
        p1 = x.split(" ")[1]
        val = (p, p1, id)
        # print(val)
        sql = "UPDATE Plow_Bolts SET value1=%s, unit1=%s  WHERE id=%s"
        mycursor.execute(sql, val)
       obj1.commit()
"""

"""
# =========================================Numerical rp_40,000 psi =============================================
    if "psi" in x:                                      # rp_40,000 psi
        p = x.split(" ")[0]                             # rp_40,000
        p1 = x.split(" ")[1]                            # psi
        val = (p, p1, id)
        sql = "Update Nut_Inserts set value1=%s, unit1=%s WHERE id = %s"
        mycursor.execute(sql, val)
        print("execute")
        obj1.commit()
    if "Tensile Strength" in a and "_" in x and "psi" not in x:
        u = x
        val1 = (u, id)
        # print(val1)
        sql1 = "Update Nut_Inserts set value1=%s WHERE id = %s"
        mycursor.execute(sql1, val1)
        print("execute")
        obj1.commit()
"""  # Numerical                             value  rp_40,000 psi

"""
    if "Flange Thickness" in a and "_" in x and "mm" not in x:                    # rp_0.414"
        i = x.split('"')[0]                                                       # rp_0.414
        inch = "inch"
        val = (i, inch, id)                                                         # rp_0.414', 'inch', 10
        sql = "UPDATE Nut_Inserts SET value1=%s, unit1=%s  WHERE id=%s"
        mycursor.execute(sql, val)
        print("execute 1")
    if "Flange Thickness" in a and "mm" in x:                                       # rp_7.1 mm and rp_8 mm
        i1 = x.split(" ")[0]                                                         # rp_7.1
        i2 = x.split(" ")[1]                                                        # mm
        val1 = (i1, i2, id)
        sql = "UPDATE Nut_Inserts SET value1=%s, unit1=%s  WHERE id=%s"
        mycursor.execute(sql, val1)
        print("execute 2")
    obj1.commit()
"""  # Numerical                             Value1 rp_0.414"  and value2  rp_7.1 mm


"""
    if "Installed Length" in a and "_" in x and "mm" not in x:                    # rp_0.414"
        i = x.split('"')[0]                                                       # rp_0.414
        inch = "inch"
        val = (i, inch, id)                                                         # rp_0.414', 'inch', 10
        sql = "UPDATE Nut_Inserts SET value1=%s, unit1=%s  WHERE id=%s"
        mycursor.execute(sql, val)
        print("execute 1")
    if "Installed Length" in a and "mm" in x:                                       # rp_7.1 mm and rp_8 mm
        i1 = x.split(" ")[0]                                                         # rp_7.1
        i2 = x.split(" ")[1]                                                        # mm
        val1 = (i1, i2, id)
        sql = "UPDATE Nut_Inserts SET value1=%s, unit1=%s  WHERE id=%s"
        mycursor.execute(sql, val1)
        print("execute 2")
    obj1.commit()
"""  # Numerical Value1 rp_0.414"  and value2  rp_7.1 mm

"""
    # ================================== Numerical =========================================
    if "Barrel Diameter" in a and "_" in x and "mm"not in x and "/"not in x:    # rp_0.28" and rp_0.28"
        b = x.split('"')[0]                                                     # rp_0.28 and rp_0.28
        inch = "inch"
        val = (b, inch, id)
        sql = "UPDATE Nut_Inserts SET value1=%s, unit1=%s  WHERE id=%s"
        mycursor.execute(sql, val)
        # print("code execute 1 ")
        # obj1.commit()
    if "Barrel Diameter" in a and "mm" in x:                                    # rp_5.2 mm and rp_6.2 mm
        b1 = x.split(" ")[0]                                                    # rp_5.2 and rp_6.2
        b2 = x.split(" ")[1]                                                    # mm and mm
        val = (b1, b2, id)                                                      # rp_5.2', 'mm', 4033) and ('rp_6.2', 'mm', 4059
        sql = "UPDATE Nut_Inserts SET value1=%s, unit1=%s  WHERE id=%s"
        mycursor.execute(sql, val)
        print("code execute 2 ")
        obj1.commit()
"""  # Numerical Value1 rp_0.28" and rp_0.28 and value2  rp_5.2 mm and rp_6.2 mm

"""
# ================================== Numerical =========================================
    if "/" in x and '-' not in x and '(' not in x and ' ' not in x:
        a = x.split("rp_")[1]           # 3/16" and 1/4"
        b1 = a.split('"')[0]            # 3/16 and 1/4
        rp = "rp_"
        inch = "inch"
        # # if ' ' not in b1:
        d = round(float(Fraction(b1)), 2)                # 0.22 and 0.44
        ad = rp + str(d)                                 # rp_0.22 and rp_0.44
        val = (ad, inch, id)                             # rp_0.22', 8 and 'rp_0.44', 20
        print(val)
        sql = "UPDATE Nut_Inserts SET value1=%s, unit1=%s  WHERE id=%s"
        mycursor.execute(sql, val)
        print("code execute")
    obj1.commit()
"""  # Numerical                             Value  rp_3/16" and rp_1/4"

"""
    # # Range 2 update value rp_etc and no update polarity and tested it. it is working
    #     if 'rp_No.' in x and ',' not in x:                          # rp_No. 4 and rp_No. 10
    #         s = x.replace("No. ", "")                               # rp_4 and rp_10
    #         no = "No."
    #         val = (s, no, id)                                       # rp_4', 'No. and rp_6', 'No.
    #         sql = "UPDATE dataf SET polarity1=%s , value1=%s WHERE id=%s"
    #         mycursor.execute(sql, val)
    #         # print("execute")
    #
    #     elif "/" in x and '"' in x and ',' not in ' ' not in x:     # rp_3/16" and rp_7/16"
    #         h = x.split("rp_")[1]                                   # 3/16" and 5/32"
    #         g = h.split('"')[0]                                     # 3/16 and 5/32
    #         rp = "rp_"
    #         inch = "inch"
    #         d = round(float(Fraction(g)), 2)                        # 0.19 and 0.19
    #         ad = rp + str(d)                                        # rp_0.19 and rp_0.19
    #         val = (ad, inch, id)                                    # rp_0.19', 'inch and rp_0.19', 'inch
    #         sql = "UPDATE dataf SET value1=%s, unit1=%s  WHERE id=%s"
    #         mycursor.execute(sql, val)
    #         # print("execute")
    #
    #     elif "rp_M" in x and "Range 2" in p:                        # rp_M4 and rp_M2.5
    #         s = x.replace("M", "")                                  # rp_4  and rp_2.5
    #         mm = "mm"
    #         M = "M"
    #         o = "0"
    #         val = (s, mm, M, o, id)                                 # rp_2', 'mm', 'M', '0 and rp_2.5', 'mm', 'M', '0
    #         sql = "UPDATE dataf SET value1=%s, unit1=%s, polarity1=%s, polarity2=%s WHERE id=%s"
    #         mycursor.execute(sql, val)
    #         # print("execute")
    #     obj1.commit()
"""

# ======================================== range 2  rp_1/4", M6 =================================================
#     if '",' in x and "Range 2" in p:                        # rp_1/4", M6 , like this value
#         s = x.split("rp_")[1]                               # 1/4", M6 output file
#         s1 = s.split('",')[0]                               # 1/4  and 1 1/8 output file
#         s2 = s1.replace(' ', '+')                           # 1+1/8 output
#         rp = "rp_"
#         inch = "inch"
#         key = "1"
#         d = round(float(eval(s2)), 2)                       # 0.25  and 0.31
#         ad = (rp + str(d))                                  # rp_0.25 and rp_0.31
#         val = (ad, inch, key, id)                           # rp_0.25', 'inch', '1 and rp_0.31', 'inch', '1
#         sql = "UPDATE dataf SET value1=%s, unit1=%s, value_pairing=%s WHERE id=%s"
#         mycursor.execute(sql, val)
#
#         s = x.split("rp_")[1]                                # rp_1/4", M6 , like this value
#         k = x.split("M")[1]                                  # 6 and 8
#         ad1 = rp + k                                         # rp_6 and rp_8
#         M = "M"
#         mm = "mm"
#         key1 = "2"
#         val1 = (M, ad1, mm, key1)                             # M', 'rp_6', 'mm', '2' and 'M', 'rp_8', 'mm', '2
#         sql1 = "INSERT INTO dataf (polarity1, value1, unit1, value_pairing) values(%s,%s,%s,%s) "
#         mycursor.execute(sql1, val1)
#         # print("execute")
#     obj1.commit()


"""    
    if '"' in x:
        e = "inch"
        val = (e, id)
        # print(val)
        sql = "UPDATE dataf SET unit1=%s WHERE id=%s"
        mycursor.execute(sql, val)
    obj1.commit()
    
    elif " ' " in z:
        g = "Feet"
        val = (g, id)
        sql = "UPDATE dataf SET unit1=%s WHERE id=%s"
        mycursor.execute(sql, val)
    mydb.commit()
    
    elif 'mm' in z:
        e = "mm"
        val = (e, id)
        # print(val)
        sql = "UPDATE dataf SET unit1=%s WHERE id=%s"
        mycursor.execute(sql, val)
    obj1.commit()
    
    elif 'ga' in z:
        e = "ga"
        val = (e, id)
        sql = "UPDATE dataf SET unit1=%s WHERE id=%s"
        mycursor.execute(sql, val)
        # obj1.commit() Numerical#
"""
