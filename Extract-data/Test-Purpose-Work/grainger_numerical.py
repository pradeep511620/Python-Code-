import csv
import mysql.connector
from fractions import Fraction

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="grainger"
)
mycursor = mydb.cursor()

def fractionByvalue():

    sql1 = "SELECT * from DATA  WHERE DataType='Numerical' "
    mycursor.execute(sql1)
    l = mycursor.fetchall()
    for x in l:
            # value = x[10]
            Datatype = x[5]
            
            value1=x[10]
            inc = "Inch"
            rp = "rp_"
            mm = "mm"
            id = x[0]
            Deg=""
            d=x[5]
            
            # try:

            if '/' in value1 and ' ' not in value1:
                    print(value1)
                    try:
                        if '-' in value1:
                            a = value1.strip('rp_').strip('RP_')
                            a2 = float(Fraction(a))
                            rs = round(a2, 3)
                            rs1 = "rp_" + str(rs)
                            val = (rs1,"-",id)
                            sql1 = "Update DATA set value1=%s,PreP=%s,unit1=%s where id = %s"
                            mycursor.execute(sql1, val)
                        else:
                            a = value1.strip('rp_').strip('RP_')
                            a2 = float(Fraction(a))
                            rs = round(a2, 3)
                            rs1 = "rp_" + str(rs)
                            val = (rs1,id)
                            sql1 = "Update DATA set value1=%s where id = %s"
                            mycursor.execute(sql1, val)    
                    except:
                        pass     
                           




            if '"' not in value1 and "mm" not in value1 and "Data" not in value1 and  ' ' in value1:
                print(value1)
                f=value1.split(' ')
                print(len(f))
                if len(f)==2:
                    f=value1.split(' ')
                    val = (f[0], f[1], id)
                    sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                    mycursor.execute(sql1, val)
                    print("lol")
                else:
                    f=value1.split(' ')
                    val = (f[0], f[1]+f[2], id)
                    sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                    mycursor.execute(sql1, val)    
                    print("lol")
    mydb.commit()            
                

#                 if  '"' in value1 and 'to' not in value1 and '-' not in value1 and '(' not in value1 and 'OD' not in value1 and "ID" not in value1 and 'Numerical'  in Datatype :
#                         print(value1)
#                         if '/' in value1 and ' ' not in value1:
#                             a = value1.strip('rp_').strip('RP_')
#                             b = a.strip('"')
#                             a2 = float(Fraction(b))
#                             rs = round(a2, 3)
#                             rs1 = "rp_" + str(rs)
#                             val = (rs1, inc, id)
#                             sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
#                             mycursor.execute(sql1, val)

#                         elif '/' in value1 and ' ' in value1:
#                             a = value1.strip('rp_').strip('RP_')
#                             b = a.strip('"')
#                             c = b.split(' ')[1]
#                             d = float(b.split(' ')[0])
#                             # print(d)
#                             a2 = float(Fraction(c))
#                             a3 = d + a2
#                             rs = round(a3, 3)

#                             rs1 = "rp_" + str(rs)
#                             # print(rs1)
#                             print(id)
#                             val = (rs1, inc, id)
#                             sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
#                             mycursor.execute(sql1, val)
#                         else:
#                             a = value1.strip('rp_').strip('RP_')
#                             rs = a.strip('"')
#                             rs1 = "rp_" + str(rs)
#                             val = (rs1, inc, id)
#                             sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
#                             mycursor.execute(sql1, val)


#                 if  'mm' in value1 and 'Numerical'  in Datatype :
#                     if ' mm' in value1 or 'mm' in value1:
#                         f = value1.replace(' mm','').replace('mm','')
#                         print(value1)
#                         i = round(eval(f.replace("rp_", '').replace(" ", '+')), 3)
#                         p = rp + str(i)
#                         print("safffffffff",p)
#                         val = (p, mm, id)
#                         sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
#                         mycursor.execute(sql1, val)
#                         print("mm : ", value1)
#             except Exception as e:
#                 print(e)

        

#     mydb.commit()


# def sortingvalue():
#     sql1 = "SELECT * from DATA   "
#     mycursor.execute(sql1)
#     l = mycursor.fetchall()
#     for x in l:
#         value = x[7]
#         Datatype = x[3]
#         attribute = x[6]
#         value1 = x[9]
#         inc = "Inch"
#         rp = "rp_"
#         mm = "mm"
#         id = x[0]
#         Deg = ""
#         if 'Discrete' not in Datatype and 'VarChar' not in Datatype and '(' not in value1 and 'OD' not in value1 and "ID" not in value1:
#             if ' Deg.' in value1 and 'Range 1' not in Datatype and ' Deg.F' not in value1:
#                 print(value1)
#                 dg = value1.replace(' Deg.F', '')
#                 print(dg)
#                 Deg = "Deg."
#                 val = (dg, Deg, id)
#                 sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
#                 mycursor.execute(sql1, val)


#             if ' Deg.F' in value1 and 'Range 1' not in Datatype:
#                 print(value1)
#                 dg = value1.replace(' Deg.', '')
#                 print(dg)
#                 Deg = "Deg."
#                 val = (dg, Deg, id)
#                 sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
#                 mycursor.execute(sql1, val)
#             if ' lbs.' in value1 and 'Numerical' in Datatype:
#                 lb = value1.replace(' lbs.', '')
#                 lbs = "lbs."
#                 val = (lb, lbs, id)
#                 sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
#                 mycursor.execute(sql1, val)

#             elif 'rp_M' in value1 and ',' not in value1:
#                 j = value1.replace('M', '')
#                 p = 'M'
#                 print(j, "fasdfds")
#                 val = (p, j, mm, id)
#                 sql1 = "Update DATA set PreP=%s,value1=%s,unit1=%s where id = %s"
#                 mycursor.execute(sql1, val)
#             elif 'rp_No.' in value1 and ',' not in value1 and 'Numerical' in Datatype:
#                 i = value1.replace("No. ", '')
#                 print('no:', i)
#                 p = "No."
#                 val = (p, i, id)
#                 sql1 = "Update DATA set PreP=%s,value1=%s where id = %s"
#                 mycursor.execute(sql1, val)

#             elif "ga" in value1 and 'Numerical' in Datatype:
#                 io=value1.strip(" ga.")
#                 g = round(eval(io.replace("rp_", '').replace(" ", '+').replace("ga.", '')), 3)
#                 g1=rp+str(g)
#                 ga = "ga."
#                 val = (g1, ga, id)
#                 sql = "UPDATE DATA SET value1=%s,unit1=%s WHERE id=%s"
#                 mycursor.execute(sql, val)
#             elif "psi" in value1 or '' in value1 and 'Numerical' in Datatype:
#                 if "psi" in value1:
#                     e = value1.split(" ")
#                     val = (e[0], e[1], id)
#                     sql = "UPDATE DATA SET value1=%s,unit1=%s WHERE id=%s"
#                     mycursor.execute(sql, val)
#                 else:
#                     val = (value1, id)
#                     sql = "UPDATE DATA SET value1=%s WHERE id=%s"
#                     mycursor.execute(sql, val)
#             if 'min.' in value1 and 'Range 1' not in Datatype and 'Numerical' in Datatype:
#                 print(value1)
#                 mi1 = value1.replace('min.', '')
#                 min = "min."
#                 val = (mi1, min, id)
#                 sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
#                 mycursor.execute(sql1, val)
#             if 'hrs.' in value1 and 'Range 1' not in Datatype and 'Numerical' in Datatype:
#                 print(value1)
#                 hr1 = value1.replace('hrs.', '')
#                 print(hr1)
#                 hrs = "hrs."
#                 val = (hr1, hrs, id)
#                 sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
#                 mycursor.execute(sql1, val)
#     mydb.commit()




def range1():
    sql1 = "SELECT * from DATA  WHERE DataType='Range 1' "
    mycursor.execute(sql1)
    
    
    l = mycursor.fetchall()
    for x in l:
        value = x[8]
        Datatype = x[3]
        attribute = x[6]
        value1 = x[10]
        inc = "Inch"
        rp = "rp_"
        mm = "mm"
        id = x[0]
        Deg = ""
        # val = ('', '','','',id)
        # sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
        # mycursor.execute(sql, val) 
        # rp_0.63A to 1.00A
        # rp_0 to 180 sec.
        if 'A' in value1 and 'V AC' not in value1:
            print(value1)
            a1=value1.split(' ')
            val = (a1[0].replace('A',''), "A","rp_"+a1[2].replace('A','') ,"A",id)
            sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
            mycursor.execute(sql, val)
        if 'V AC' in value1 :
            print(value1)
            a1=value1.split(' ')
            if len(a1)==4:
                val = (a1[0], "V AC","rp_"+a1[2].replace('V','') ,"V AC",id)
                sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
                mycursor.execute(sql, val)  
            else:
                val = (a1[0],"V AC",id)
                sql = "UPDATE DATA SET value1=%s, unit1=%sWHERE id=%s"
                mycursor.execute(sql, val)   

        if 'sec.' in value1:
            a1=value1.split(' ')
            val = (a1[0], "sec.","rp_"+a1[2],"sec.",id)
            sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
            mycursor.execute(sql, val)

        if 'V DC' in value1 :
            print(value1)
            a1=value1.split(' ')
            if len(a1)==3:
                val = (a1[0], "V DC","rp_"+a1[2].replace('V DC','') ,"V DC",id)
                sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
                mycursor.execute(sql, val)  
            else:
                val = (a1[0],"V DC",id)
                sql = "UPDATE DATA SET value1=%s, unit1=%sWHERE id=%s"
                mycursor.execute(sql, val)    

        if 'RPM' in value1 :
            print(value1)
            a1=value1.split(' ')
            if len(a1)==3:
                val = (a1[0], "RPM","rp_"+a1[2],"RPM",id)
                sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
                mycursor.execute(sql, val)  
            else:
                val = (a1[0],"RPM",id)
                sql = "UPDATE DATA SET value1=%s, unit1=%sWHERE id=%s"
                mycursor.execute(sql, val)        
        # rp_30% to 80%         
        if '%' in value1 :
            print(value1)
            a1=value1.split(' ')
            if len(a1)==3:
                val = (a1[0].replace('%',''), "%","rp_"+a1[2].replace('%',''),"%",id)
                sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
                mycursor.execute(sql, val)  
            else:
                val = (a1[0].replace('%',''),"%",id)
                sql = "UPDATE DATA SET value1=%s, unit1=%sWHERE id=%s"
                mycursor.execute(sql, val)
                   
            # rp_+/-0.005"

        if '+/' in value1 :
            print(value1)
            if '"' in value1:
                val = ("-",value1.replace('+/-','').replace('"',''), "inch",value1.replace('+/-','').replace('"',''),"inch","+",id)
                sql = "UPDATE DATA SET PreP=%s,value1=%s, unit1=%s,value2=%s, unit2=%s,PostP=%s WHERE id=%s"
                mycursor.execute(sql, val) 
            if 'mm' in value1:  
                val = ("-",value1.replace('+/-','').replace('"','').replace('mm',''), "mm",value1.replace('+/-','').replace('"','').replace('mm',''),"mm","+",id)
                sql = "UPDATE DATA SET PreP=%s,value1=%s, unit1=%s,value2=%s, unit2=%s,PostP=%s WHERE id=%s"
                mycursor.execute(sql, val)    
             
        # rp_-50 Deg. to 259 Deg. F 
        if "Deg." in value1:
            print(value1)
            a1=value1.split(' ')
           
            val = ('-',a1[0].replace('-',''), "Deg.F",'+',"rp_"+a1[3],"Deg.F",id)
            sql = "UPDATE DATA SET PreP=%s,value1=%s, unit1=%s,PostP=%s,value2=%s, unit2=%s WHERE id=%s"
            mycursor.execute(sql, val)  
            

    mydb.commit()



def Range2():
    sql1 = "SELECT * from DATA WHERE DataType='Range 2' "
    mycursor.execute(sql1)
    l = mycursor.fetchall()
    for x in l:

        v = x[8]
        c = x[3]
        th = x[6]
        v1 = x[9]
        inc = "Inch"
        rp = "rp_"
        mm = "mm"
        id = x[0]
        mpn = x[1]
        type = x[5]
        if ',' not in v:
            v=v.replace('rp_','')
            
            if '"' in v:
                if ' ' in v:    
                    in1=v.split(' ')
                    i = round(eval(in1[1].replace('"','')), 3)
                    jh="rp_"+str(int(in1[0])+int(i))
                    val = (jh, inc, id)
                    sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                    mycursor.execute(sql1, val)
                else:
                    i = round(eval(v.replace('"','')), 3)
                        
                    val = ("rp_"+str(i), "inch", id)
                    sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                    mycursor.execute(sql1, val)        
        
            elif 'hp' in v:
                # if ' ' in v:
                #     in1=v.split(' ')
                #     i = round(eval(in1[1].replace('hp','')), 3)
                #     jh="rp_"+str(int(in1[0])+int(i))
                #     val = (jh, inc, id)
                    
                #     val = (jh, "hp", id)
                #     sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                #     mycursor.execute(sql1, val)
                # else:
                i = round(eval(v.replace('hp','')), 3)
                
                val = ("rp_"+str(i), "hp", id)
                sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                mycursor.execute(sql1, val)   

            elif 'V AC' in v :
                i = round(eval(v.replace('V AC','')), 3)
                    
                val = ("rp_"+str(i), "V AC", id)
                sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                mycursor.execute(sql1, val) 

            elif 'V' in v and 'V AC' not in v:
                i = round(eval(v.replace('V','')), 3)
                    
                val = ("rp_"+str(i), "V", id)
                sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                mycursor.execute(sql1, val)  

            else:      
                i = round(eval(v), 3)
                    
                val = ("rp_"+str(i), id)
                sql1 = "Update DATA set value1=%s  where id = %s"
                mycursor.execute(sql1, val)

        if ',' in v:
            v=v.replace('rp_','')
            
            
            s = v.split(", ")
            k = s[0]
            for i in s:
                if i == k:
                    key = 1
                    if '"' in i:
                        ino=i.split(' ')
                        if ' ' in i:
                            j = round(eval(ino[1].replace('"', '').replace("rp_", '')), 3)
                       
                            jh="rp_"+str(int(j)+int(ino[0]))
                            val = (jh, "inch", key, id)
                            print(p)
                            sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                            mycursor.execute(sql1, val)
                        else:    
                            j = round(eval(i.replace('"', '').replace("rp_", '')), 3)
                            p = rp + str(j)
                    
                            val = (p, "inch", key, id)
                            print(p)
                            sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                            mycursor.execute(sql1, val)
                    elif 'hp' in i:
                        j = round(eval(i.replace('hp', '').replace("rp_", '')), 3)
                        p = rp + str(j)
                        val = (p, "hp", key, id)
                        print(p)
                        sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                        mycursor.execute(sql1, val)   
                    elif 'V DC' in i:
                        j = round(eval(i.replace('V DC', '').replace("rp_", '').replace(" ", '+')), 3)
                        p = rp + str(j)
                        val = (p, "V DC", key, id)
                        print(p)
                        sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                        mycursor.execute(sql1, val)    
                    elif 'V' in i and 'V DC' not in i and 'V AC' not in i:
                        print("fsafddfsda",i)
                        j = round(eval(i.replace('V', '').replace("rp_", '').replace(" ", '+')), 3)
                        p = rp + str(j)
                        val = (p, "V", key, id)
                        print(p)
                        sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                        mycursor.execute(sql1, val) 
                    elif 'V AC' in i:
                        j = round(eval(i.replace('V AC', '').replace("rp_", '').replace(" ", '+')), 3)
                        p = rp + str(j)
                        val = (p, "V AC", key, id)
                        print(p)
                        sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                        mycursor.execute(sql1, val)        
                    elif 'V AC' in v and "V DC" not in v:
                        j = round(eval(i.replace('V AC', '').replace("rp_", '').replace(" ", '+')), 3)
                        p = rp + str(j)
                        val = (p, "V AC", key, id)
                        print(p)
                        sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                        mycursor.execute(sql1, val)    
                    elif 'X' in v:
                        
                        val = (i, key, id)
                        print(p)
                        sql1 = "Update DATA set value1=%s,keyvalue=%s  where id = %s"
                        mycursor.execute(sql1, val)


                else:
                    key = key + 1
                    print(s)
                    if 'hp' in i:
                        j = round(eval(i.replace('hp', '').replace("rp_", '')), 3)
                        p = rp + str(j)
                        val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "hp", key)
                        sql1 = "INSERT INTO DATA (Title,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                        mycursor.execute(sql1, val)
                    elif '"' in i:
                        ino=i.split(' ')
                        if ' ' in i:
                            j = round(eval(ino[1].replace('"', '').replace("rp_", '')), 3)
                       
                            jh="rp_"+str(int(j)+int(ino[0]))
                            
                            print(p)
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],jh, "inch", key)
                            sql1 = "INSERT INTO DATA (Title,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)
                        else:    
                            j = round(eval(i.replace('"', '').replace("rp_", '')), 3)
                            p = rp + str(j)
                            print(p)
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "inch", key)
                            sql1 = "INSERT INTO DATA (Title,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)



                      
                    elif 'V DC' in i:
                        j = round(eval(i.replace('V DC', '').replace("rp_", '').replace(" ", '+')), 3)
                        p = rp + str(j)
                        val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "V DC", key)
                        sql1 = "INSERT INTO DATA (Title,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                        mycursor.execute(sql1, val)   
                    elif 'V' in i and 'V DC' not in i and 'V AC' not in i:
                        j = round(eval(i.replace('V', '').replace("rp_", '').replace(" ", '+')), 3)
                        p = rp + str(j)
                        val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "V", key)
                        sql1 = "INSERT INTO DATA (Title,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                        mycursor.execute(sql1, val)    
                    elif 'V AC' in i:
                        j = round(eval(i.replace('V AC', '').replace("rp_", '').replace(" ", '+')), 3)
                        p = rp + str(j)
                        val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "V AC", key)
                        sql1 = "INSERT INTO DATA (Title,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                        mycursor.execute(sql1, val)     
                    elif 'V AC' in v and "V DC" not in v:
                        j = round(eval(i.replace('V AC', '').replace("rp_", '').replace(" ", '+')), 3)
                        p = rp + str(j)
                        val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "V AC", key)
                        sql1 = "INSERT INTO DATA (Title,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                        mycursor.execute(sql1, val)    
                    elif 'X' in v:    
                        
                        p = rp + i
                        val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, key)
                        sql1 = "INSERT INTO DATA (Title,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                        mycursor.execute(sql1, val)
      

    mydb.commit()

def Range3():
    sql1 = "SELECT * from DATA WHERE DataType='Range 2' "
    mycursor.execute(sql1)
    l = mycursor.fetchall()
    for x in l:

        v = x[8]
        c = x[3]
        th = x[6]
        v1 = x[9]
        inc = "Inch"
        rp = "rp_"
        mm = "mm"
        id = x[0]
        mpn = x[1]
        type = x[5]
        if ',' not in v:
            v=v.replace('rp_','')
            if "to" in v:
                        if 'A' in i:
                            a1=i.split(' ')
                            val = (a1[0].replace('A',''), "A","rp_"+a1[2].replace('A','') ,"A",id)
                            sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
                            mycursor.execute(sql, val)
                        if 'V AC' in i:
                            a1=i.split(' ')
                            val = (a1[0].replace('V AC',''), "V AC","rp_"+a1[2].replace('V AC','') ,"V AC",id)
                            sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
                            mycursor.execute(sql, val)
                        if 'V DC' in i:
                            a1=i.split(' ')
                            val = (a1[0].replace('V AC',''), "V AC","rp_"+a1[2].replace('V AC','') ,"V AC",id)
                            sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
                            mycursor.execute(sql, val)
            else:
                    if 'V AC' in v :
                        i = round(eval(v.replace('V AC','')), 3)
                            
                        val = ("rp_"+str(i), "V AC", id)
                        sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                        mycursor.execute(sql1, val) 

                    elif 'V' in v and 'V AC' not in v:
                        i = round(eval(v.replace('V','')), 3)
                            
                        val = ("rp_"+str(i), "V", id)
                        sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                        mycursor.execute(sql1, val)  

                    elif 'A' in v :
                        i = round(eval(v.replace('A','')), 3)
                            
                        val = ("rp_"+str(i), "A", id)
                        sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                        mycursor.execute(sql1, val)


                    else:      
                        i = round(eval(v), 3)
                            
                        val = ("rp_"+str(i), id)
                        sql1 = "Update DATA set value1=%s  where id = %s"
                        mycursor.execute(sql1, val)

        if ',' in v:
            v=v.replace('rp_','')
            s = v.split(", ")
            k = s[0]
            for i in s:
                if i == k:
                    key = 1
                    if "to" in i:
                        if 'A' in i:
                            a1=i.split(' ')
                            val = (a1[0].replace('A',''), "A","rp_"+a1[2].replace('A','') ,"A",id)
                            sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
                            mycursor.execute(sql, val)
                        if 'V AC' in i:
                            a1=i.split(' ')
                            val = (a1[0].replace('V AC',''), "V AC","rp_"+a1[2].replace('V AC','') ,"V AC",id)
                            sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
                            mycursor.execute(sql, val)
                        if 'V DC' in i:
                            a1=i.split(' ')
                            val = (a1[0].replace('V AC',''), "V AC","rp_"+a1[2].replace('V AC','') ,"V AC",id)
                            sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
                            mycursor.execute(sql, val)    

                    else:
                           

                        if 'V AC' in v :
                            i = round(eval(v.replace('V AC','')), 3)
                                
                            val = ("rp_"+str(i), "V AC", id)
                            sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                            mycursor.execute(sql1, val) 

                        elif 'V' in v and 'V AC' not in v:
                            i = round(eval(v.replace('V','')), 3)
                                
                            val = ("rp_"+str(i), "V", id)
                            sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                            mycursor.execute(sql1, val)  

                        elif 'A' in v :
                            i = round(eval(v.replace('A','')), 3)
                                
                            val = ("rp_"+str(i), "A", id)
                            sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                            mycursor.execute(sql1, val)


                        else:      
                            i = round(eval(v), 3)
                                
                            val = ("rp_"+str(i), id)
                            sql1 = "Update DATA set value1=%s  where id = %s"
                            mycursor.execute(sql1, val)    


                else:
                    key = key + 1
                    print(s)
                    if 'to' in i:          
                        if 'V DC' in i:
                            a1=i.split(' ')
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],a1[0].replace('V AC',''), "V AC","rp_"+a1[2].replace('V AC','') ,"V AC", key)
                            sql1 = "INSERT INTO DATA (Title,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,value2,unit2,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)   
                        elif 'V' in i and 'V DC' not in i and 'V AC' not in i:
                            a1=i.split(' ')
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],a1[0].replace('V',''), "V","rp_"+a1[2].replace('V','') ,"V", key)
                            sql1 = "INSERT INTO DATA (Title,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,value2,unit2,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)    
                        elif 'V AC' in i:
                            a1=i.split(' ')
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],a1[0].replace('V AC',''), "V AC","rp_"+a1[2].replace('V AC','') ,"V AC", key)
                            sql1 = "INSERT INTO DATA (Title,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,value1,unit2,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)     
                         
                    
                    else:
                        if 'V DC' in i:
                            j = round(eval(i.replace('V DC', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "V DC", key)
                            sql1 = "INSERT INTO DATA (Title,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)   
                        elif 'V' in i and 'V DC' not in i and 'V AC' not in i:
                            j = round(eval(i.replace('V', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "V", key)
                            sql1 = "INSERT INTO DATA (Title,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)    
                        elif 'V AC' in i:
                            j = round(eval(i.replace('V AC', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "V AC", key)
                            sql1 = "INSERT INTO DATA (Title,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)     
                        elif 'V AC' in v and "V DC" not in v:
                            j = round(eval(i.replace('V AC', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "V AC", key)
                            sql1 = "INSERT INTO DATA (Title,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)    
                        elif 'X' in v:    
                            
                            p = rp + i
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, key)
                            sql1 = "INSERT INTO DATA (Title,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)        
                        
      

    mydb.commit()

