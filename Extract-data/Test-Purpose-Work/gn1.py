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
            
            try:
                
                    
                if '/' in value1 and ' ' not in value1 and 'M' not in value1:
                        print(value1)
                        try:
                            if '-' in value1:
                                rs=value1.replace('-','').split(' ')
                                
                                val = (rs[0],"-",rs[1],id)
                                sql1 = "Update DATA set value1=%s,PreP=%s,unit1=%s where id = %s"
                                mycursor.execute(sql1, val)
                            else:
                                rs=round(eval(value1.replace("rp_", '').replace('"','')), 3)
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
                        try:
                            if '/' in f[0]:
                                f=value1.split(' ')
                                val = ("rp_"+str(round(eval(f[0].replace('rp_','')),3)), f[1], id)
                                sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                                mycursor.execute(sql1, val)
                                print("lol")
                            elif "cal/sq cm" in value1:   
                                f=value1.split(' ')
                                val = ("rp_"+str(round(eval(f[0].replace('rp_','')),3)), f[1]+f[2], id)
                                sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                                mycursor.execute(sql1, val)
                                print("lol") 
                            else:    
                                f=value1.split(' ')
                                val = (f[0], f[1], id)
                                sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                                mycursor.execute(sql1, val)
                                print("lol")
                        except:
                            pass        
                    else:
                        f=value1.split(' ')
                        if '/' in f[1] and '/sq' not in f[1]:
                            val = ("rp_"+str(int(f[0].replace("rp_", ''))+round(eval(f[1].replace("rp_", '').replace('"','')), 3)), f[2], id)
                            sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                            mycursor.execute(sql1, val)    
                            print("lol")
                        else:    
                            val = (f[0], f[1]+f[2], id)
                            sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                            mycursor.execute(sql1, val)    
                            print("lol")
                
                    

                elif  '"' in value1 and 'to' not in value1 and '-' not in value1 and '(' not in value1 and 'OD' not in value1 and "ID" not in value1 and 'Numerical'  in Datatype and 'M' not in value1 and 'mm/sec' not in value1:
                        value1=value1.lower()
                        print(value1)
                        if '"/min' in value1:
                            bv=value1.replace('"/min','')
                            val = (bv, "inch/min", id)
                            sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                            mycursor.execute(sql1, val)

                        if '/min' not in value1:
                            if '/' in value1 and ' ' not in value1:
                                rs=round(eval(value1.replace("rp_", '').replace('"','')), 3)
                                rs1 = "rp_" + str(rs)
                                val = (rs1, inc, id)
                                sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                                mycursor.execute(sql1, val)

                            elif '/' in value1 and ' ' in value1 and 'ft.' not in value1:
                                
                                rs=round(eval(value1.replace("rp_", '').replace('"','').strip().replace(" ", '+')), 3)
                                # print(d)

                                rs1 = "rp_" + str(rs)
                                # print(rs1)
                                print(id)
                                val = (rs1, inc, id)
                                sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                                mycursor.execute(sql1, val)
                            else:
                                a = value1.strip('rp_').strip('RP_')
                                rs = a.strip('"')
                                rs1 = "rp_" + str(rs)
                                val = (rs1, inc, id)
                                sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                                mycursor.execute(sql1, val)


                if  'mm' in value1 and 'Numerical'  in Datatype :
                    
                    if 'N-mm' in value1:
                        b=value1.split(' ')
                        val = (b[0], b[1], id)
                        sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"    
                    elif 'mm/hg' in value1:
                            b=value1.split(' ')
                            val = (b[0], b[1], id)
                            sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"        
                    value1=value1.lower()
                    if 'hg' not in value1 and 'N' not in value1:
                        if ' mm' in value1 or 'mm' in value1 and "mm/sec" not in value1 :
                            f = value1.replace(' mm','').replace('mm','').replace(',','')
                            print(value1)
                            i = round(eval(f.replace("rp_", '').strip().replace(" ", '+')), 3)
                            p = rp + str(i)
                            print("safffffffff",p)
                            val = (p, mm, id)
                            sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                            mycursor.execute(sql1, val)
                            print("mm : ", value1)
                        elif 'mm/sec' in value1 and ' ' not in value1:
                                rs=round(eval(value1.replace("rp_", '').replace('mm/sec','')), 3)
                                rs1 = "rp_" + str(rs)
                                val = (rs1, "mm/sec", id)
                                sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                                mycursor.execute(sql1, val)    
                     
                if 'ft.' in value1:
                            vp=value1.split('ft.')
                            print(vp)
                            rs=round(int(vp[0].strip().replace("rp_", '').replace('ft.',''))/12, 3)+round(eval(vp[1].strip().replace("rp_", '').replace('"','').replace(' ','+')), 3)
                            rs1 = "rp_" + str(rs)
                            val = (rs1, 'inch', id)
                            sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                            mycursor.execute(sql1, val)    
            except:  
                pass                  
            

        

    mydb.commit()


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
        value1 = x[8].replace('RP_','rp_')
        v=x[8].replace('RP_','rp_')
        inc = "Inch"
        rp = "rp_"
        mm = "mm"
        id = x[0]
        Deg = ""
        th=x[6]
        # val = ('', '','','',id)
        # sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
        # mycursor.execute(sql, val) 
        # rp_0.63A to 1.00A
        # rp_0 to 180 sec.
        
        if 'Â' in value1:
            value1=value1.replace('Â','')
        if 'A' in value1 and 'V AC' not in value1 and 'to' in value1:
            print("fafa",value1)
            a1=value1.split(' ')
            val = (a1[0].replace('A',''), "A","rp_"+a1[2].replace('A','') ,"A",id)
            sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
            mycursor.execute(sql, val)
        if 'V AC' in value1 :
            print(value1)
            a1=value1.split(' ')
            if len(a1)==4:
                val = (a1[0], "V AC","rp_"+a1[2].replace('V AC','') ,"V AC",id)
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


        if 'sec' in value1 and 'to' in v:
            value1=value1.lower()
            a1=value1.split('to')
            val = (a1[0].strip().replace(' sec',''), "sec","rp_"+a1[1].strip().replace(' sec',''),"sec",id)
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
            if len(a1)==4:
                val = (a1[0], "RPM","rp_"+a1[2],"RPM",id)
                sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
                mycursor.execute(sql, val)  
            else:
                val = (a1[0],"RPM",id)
                sql = "UPDATE DATA SET value1=%s, unit1=%sWHERE id=%s"
                mycursor.execute(sql, val)        
        
        if 'A AC' in value1 and 'to'  in value1:
            print(value1)
            a1=value1.split(' ')
            if len(a1)==5:
                val = (a1[0].replace('A',''), "A AC","rp_"+a1[3].replace('A',''),"A AC",id)
                sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
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
        
        

        
        
        if '"' in v:
            if '-' in v:
                b = v.split('-')
                print(b)
                print(i)
                d = b[1].replace('"', '')
                # print(d)
                e = d
                s = '-'
                val = (s, e, inc, id)
                sql = "UPDATE DATA SET PreP=%s ,value1=%s, unit1=%s WHERE id=%s"
                mycursor.execute(sql, val)

                # print(i)
                d = b[0].replace('"', '')
                # print(d)
                e = d
                print(e)
                print("sd")
                s = '+'
                val = (s, e, inc, id)
                sql = "UPDATE DATA SET PostP=%s ,value2=%s ,unit2=%s WHERE id=%s"
                mycursor.execute(sql, val)
            else:

                b = v.replace('"', '')
                # print(d)
                e = b
                val = (e, inc, id)
                sql = "UPDATE DATA SET value1=%s, unit1=%s WHERE id=%s"
                mycursor.execute(sql, val)
        if 'mm' in v:
            if '-' in v:
                b = v.split('-')
                print(b)
                print(i)
                d = b[1].replace('"', '')
                # print(d)
                e = d
                s = '-'
                val = (s, e, mm, id)
                sql = "UPDATE DATA SET PreP=%s ,value1=%s, unit1=%s WHERE id=%s"
                mycursor.execute(sql, val)

                # prin(i)
                d = b[0].replace('"', '')
                # print(d)
                e = d
                print(e)
                print("sd")
                s = '+'
                val = (e, mm, id)
                sql = "UPDATE DATA SET value2=%s ,unit2=%s WHERE id=%s"
                mycursor.execute(sql, val)
            else:
                b = v.replace('mm', '')
                # print(d)
                e = b
                val = (e, mm, id)
                sql = "UPDATE DATA SET value1=%s, unit1=%s WHERE id=%s"
                mycursor.execute(sql, val)
        if 'Deg.' in v:
            if 'C' in v:
                dt = v.split("to")
                # print(r[0])
                # print(r[1])
                # print(v,":",n)
                # print(r)
                for i in dt:

                    if i == dt[0]:
                        if '-' in i:
                            print(i)
                            j = i.replace('-', '').replace('Deg. C', '').replace('Deg.', '')
                            Deg = 'Deg.C'
                            si = '-'
                            val = (si, j, Deg, id)
                            sql = "UPDATE DATA SET PreP=%s,value1=%s,unit1=%s WHERE id=%s"
                            mycursor.execute(sql, val)
                        else:
                            j = i.replace('-', '').replace('Deg. C', '').replace('Deg.', '')
                            Deg = 'Deg.C'
                            si = '+'
                            val = (si, j, Deg, id)
                            sql = "UPDATE DATA SET PreP=%s,value1=%s,unit1=%s WHERE id=%s"
                            mycursor.execute(sql, val)

                    elif i == dt[1]:
                        j = i.replace('-', '').replace('Deg. C', '').replace('Deg.', '')
                        print(j)
                        e = rp + j.replace('-', '')
                        Deg = 'Deg.C'
                        si = "+"
                        val = (si, e, Deg, id)
                        sql = "UPDATE DATA SET PostP=%s,value2=%s,unit2=%s WHERE id=%s"
                        mycursor.execute(sql, val)
                else:
                    dt = v.split("to")
                    # print(r[0])
                    # print(r[1])
                    # print(v,":",n)
                    # print(r)
                    for i in dt:

                        if i == dt[0]:
                            if '-' in i:
                                print(i)
                                j = i.replace('-', '').replace('Deg. F', '').replace('Deg.', '')
                                Deg = 'Deg.F'
                                si = '-'
                                val = (si, j, Deg, id)
                                sql = "UPDATE DATA SET PreP=%s,value1=%s,unit1=%s WHERE id=%s"
                                mycursor.execute(sql, val)
                            else:
                                j = i.replace('-', '').replace('Deg. F', '').replace('Deg.', '')
                                Deg = 'Deg.F'
                                si = '+'
                                val = (si, j, Deg, id)
                                sql = "UPDATE DATA SET PreP=%s,value1=%s,unit1=%s WHERE id=%s"
                                mycursor.execute(sql, val)

                        elif i == dt[1]:
                            j = i.replace('-', '').replace('Deg. F', '').replace('Deg.', '')
                            print(j)
                            e = rp + j.replace('-', '')
                            Deg = 'Deg.F'
                            si = "+"
                            val = (si, e, Deg, id)
                            sql = "UPDATE DATA SET PostP=%s,value2=%s,unit2=%s WHERE id=%s"
                            mycursor.execute(sql, val)        

        if '% RH' in v:
            per=v.split('to') 
            val = (a1[0].replace('%',''), "% RH","rp_"+a1[2].replace('% RH',''),"% RH",id)
            sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
            mycursor.execute(sql, val)
        
        
        
        
        if '-' in v and "mm" in v:
            a = v.strip('mm')
            b = a.split('-')
            c = "rp_"
            # print(b)
            for i in b:
                if i == b[0]:
                    j = i.strip('mm')
                    print(j)
                    e = j
                    print(e)

                elif i == b[1]:
                    j = i.strip('mm')
                    print(j)
                    e = c + j
                    print(e)
                    m = 'mm'
                    val = (e, m, id)
                    sql = "UPDATE DATA SET value2=%s,unit2=%s WHERE id=%s"
                    mycursor.execute(sql, val)

        if 'to' in v and '"' in v:
            # n = v.replace('"', '').replace('rp_', '').replace(" to",'')
            r = v.split("to")
            print(r[0])
            print(r[1])
            # print(v,":",n)
            # print(r)
            if '-' in r[0] and '-' in r[1]:
                M = float(r[0])
                L = float(r[1])
                if M < L:
                    d = r[1].replace("-", '').replace('"', '')
                    # print(d)
                    e = rp + d
                    s = '-'
                    val = (s, e, inc, id)
                    sql = "UPDATE DATA SET PostP=%s ,value2=%s,unit2=%sWHERE id=%s"

                    mycursor.execute(sql, val)
                    print(rp + r[1])
                    u = r[0].replace("-", '').replace('"', '')
                    e2 = rp + u
                    val = (s, e2, inc, id)
                    sql = "UPDATE DATA SET PreP=%s ,value1=%s,unit1=%sWHERE id=%s"
                    mycursor.execute(sql, val)

            elif '-' not in v and 'to' in v or "Tolerance" in th:
                if "Tolerance" in th:
                    for i in r:
                        if i == r[0]:
                            hj = r[0].split('"', 1)[0]
                            i = round(eval(hj.replace(" ", '+').replace("rp_", '').replace('"', '')), 3)
                            e2 = rp + str(i)
                            s = "+"
                            val = (s, e2, inc, id)
                            sql = "UPDATE DATA SET PreP=%s,value1=%s,unit1=%sWHERE id=%s"
                            mycursor.execute(sql, val)
                        else:
                            hj = r[1].split('"', 1)[0]
                            i = round(eval(hj.replace(" ", '+').replace("rp_", '').replace('"', '')), 3)
                            e3 = rp + str(i)
                            s = "+"
                            val = (s, e3, inc, id)
                            sql = "UPDATE DATA SET PostP=%s,value2=%s,unit2=%sWHERE id=%s"
                            mycursor.execute(sql, val)
                else:
                    

                    if '"' in v and 'ft' not in v:
                        for i in r:
                            print("ss")
                            if i == r[0]:
                                hj = r[0].split('"', 1)[0]
                                i = round(eval(hj.strip().replace(" ", '+').replace("rp_", '').replace('"', '')), 3)
                                e2 = rp + str(i)

                                val = (e2, inc, id)
                                sql = "UPDATE DATA SET value1=%s,unit1=%sWHERE id=%s"
                                mycursor.execute(sql, val)
                            else:
                                if 'Infinity' in v:
                                    

                                    e3 = rp + "Infinity"

                                    val = (e3, id)
                                    sql = "UPDATE DATA SET value2=%s WHERE id=%s"
                                    mycursor.execute(sql, val)
                                else:
                                    hj = r[1].split('"', 1)[0]
                                    i = round(eval(hj.strip().replace(" ", '+').replace("rp_", '').replace('"', '')), 3)

                                    e3 = rp + str(i)

                                    val = (e3, inc, id)
                                    sql = "UPDATE DATA SET value2=%s,unit2=%s WHERE id=%s"
                                    mycursor.execute(sql, val)
                    if '"' in v and 'ft' in v:
                        for i in r:
                            print("ss")
                            if i == r[0]:
                                hj = r[0].split('"', 1)[0]
                                i = round(eval(hj.strip().replace(" ", '+').replace("rp_", '').replace('"', '')), 3)
                                e2 = rp + str(i)

                                val = (e2, inc, id)
                                sql = "UPDATE DATA SET value1=%s,unit1=%sWHERE id=%s"
                                mycursor.execute(sql, val)
                            else:
                                hj = r[1].split('ft', 1)[0]
                                i = round(eval(hj.strip().replace(" ", '+').replace("rp_", '').replace('ft', '')), 3)
                                e3 = rp + str(i)

                                val = (e3, "ft", id)
                                sql = "UPDATE DATA SET value2=%s,unit2=%s WHERE id=%s"
                                mycursor.execute(sql, val)

            else:
                n = v.replace('"', '').replace('rp_', '')
                r = n.split("to")
                for i in r:
                    print("asfdsd")
                    if '-' in i:
                        print(i)
                        d = i.replace("-", '').replace('"', '')
                        # print(d)
                        e = rp + d
                        s = '-'
                        val = (s, e, inc, id)
                        sql = "UPDATE DATA SET PreP=%s ,value1=%s, unit1=%s WHERE id=%s"
                        mycursor.execute(sql, val)
                    elif i != '':
                        # print(i)
                        e = rp + i
                        print(e)
                        print("sd")
                        s = '+'
                        val = (s, e, inc, id)
                        sql = "UPDATE DATA SET PostP=%s ,value2=%s ,unit2=%s WHERE id=%s"
                        mycursor.execute(sql, val)
        elif 'to' in v and 'mm' in v :
            
            if 'sfm' not in v:
                n = v.replace('mm', '').replace('rp_', '')
                r = n.split("to")
                # print(v,":",n)
                # print(r)
                if '-' in r[0] and '-' in r[1]:
                    M = float(r[0])
                    L = float(r[1])
                    if M < L:
                        d = r[1].replace("-", '')
                        # print(d)
                        e = rp + d
                        s = '-'
                        val = (s, e, mm, id)
                        sql = "UPDATE DATA SET PostP=%s ,value2=%s,unit2=%sWHERE id=%s"

                        mycursor.execute(sql, val)
                        print(rp + r[1])
                        u = r[0].replace("-", '')
                        e2 = rp + u
                        val = (s, e2, mm, id)
                        sql = "UPDATE DATA SET PreP=%s ,value1=%s,unit1=%sWHERE id=%s"
                        mycursor.execute(sql, val)
                elif '-' not in r[0] and '-' not in r[1]:
                    M = float(r[0])
                    L = float(r[1])
                    if M < L:
                        d = r[1].replace("-", '')
                        # print(d)
                        e = rp + d
                        s = ''
                        val = (s, e, mm, id)
                        sql = "UPDATE DATA SET PostP=%s ,value2=%s,unit2=%sWHERE id=%s"

                        mycursor.execute(sql, val)
                        print(rp + r[1])
                        u = r[0].replace("+", '')
                        e2 = rp + u
                        s = ''
                        val = (s, e2, mm, id)
                        sql = "UPDATE DATA SET PreP=%s ,value1=%s,unit1=%sWHERE id=%s"
                        mycursor.execute(sql, val)


                else:
                    n = v.replace('rp_', '')
                    r = n.split('to')

                    for i in r:
                        if '-' in i:
                            d = i.replace("-", '').replace('mm', '')
                            # print(d)
                            e = rp + d
                            s = '-'
                            val = (s, e, mm, id)
                            sql = "UPDATE DATA SET PreP=%s ,value1=%s, unit1=%s WHERE id=%s"
                            mycursor.execute(sql, val)
                        elif i != '':
                            # print(i)
                            e = rp + i
                            print(e)
                            print("sd")
                            s = '+'
                            val = (s, e, mm, id)
                            sql = "UPDATE DATA SET PostP=%s ,value2=%s ,unit2=%s WHERE id=%s"
                            mycursor.execute(sql, val)

        if ',' not in v and 'to' not in v and '-' not in v:
            print(v)
            s = v.replace("rp_", '')
            if '"' in v or '/' in v:
                if '/' not in v and '(' not in v:
                    print(s)
                    s1 = s.replace('"', '').replace(' ', '')
                    print(s1)
                    s2 = rp + str(1)
                    val = (s1, inc, id)
                    sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                    mycursor.execute(sql1, val)
                if '/' in v and '(' not in v and 'V' not in v and 'ft' not in v:
                    if '"' in v:
                        print(s)
                        s1 = round(eval(s.replace('"', '').replace(' ', '')), 3)
                        print(s1)
                        s2 = rp + str(s1)
                        val = (s2, inc, id)
                        sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                        mycursor.execute(sql1, val)
                        
            if 'mm' in v or '/' in v and 'V' not in v:
                if '/' not in v and '(' not in v:
                    print(s)
                    s1 = s.replace('mm', '').replace(' ', '')
                    s2 = rp + str(s1)
                    val = (s2, mm, id)
                    sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                    mycursor.execute(sql1, val)
                if '/' in v and '(' not in v:
                    if 'mm' in v:
                        print(s)
                        s1 = round(eval(s.replace('"', '').replace(' ', '')), 3)
                        s2 = rp + str(s1)
                        val = (s2, mm, id)
                        sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                        mycursor.execute(sql1, val)    
                    if 'ft' in v:
                        print(s)
                        s1 = round(eval(s.replace(' ft.', '').replace(' ', '+')), 3)
                        s2 = rp + str(s1)
                        val = (s2, 'ft.', id)
                        sql1 = "Update DATA set value1=%s,unit1=%s where id = %s"
                        mycursor.execute(sql1, val)


            if 'V AC/DC' in v:
                
                val = ("-",value1.replace(' V AC/DC','').replace('"',''), "V AC",value1.replace(' V AC/DC','').replace('"',''),"V DC","+",id)
                sql = "UPDATE DATA SET PreP=%s,value1=%s, unit1=%s,value2=%s, unit2=%s,PostP=%s WHERE id=%s"
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
        try:
            if ',' not in v:
                v=v.replace('rp_','')
                
                if '"' in v:
                    if ' ' in v:    
                        rs=round(eval(v.replace("rp_", '').replace('"','').replace(' ','+')), 3)

                        rs1 = "rp_" + str(rs)
                        print(rs1)
                        val = (rs1, inc, id)
                        sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                        mycursor.execute(sql1, val)
                    else:
                        i = round(eval(v.strip('rp_').strip('RP_').replace('"','')), 3)
                            
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
                    print(v)
                    i = round(eval(v.replace('V AC','')), 3)
                        
                    val = ("rp_"+str(i), "V AC", id)
                    sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                    mycursor.execute(sql1, val) 

                elif 'V' in v and 'V AC' not in v:
                    i = round(eval(v.replace('V','')), 3)
                        
                    val = ("rp_"+str(i), "V", id)
                    sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                    mycursor.execute(sql1, val)  

                elif 'Hz' in v :
                    i = round(eval(v.replace('Hz','')), 3)
                        
                    val = ("rp_"+str(i), "Hz", id)
                    sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                    mycursor.execute(sql1, val)

                elif 'mm' in v :
                    i = round(eval(v.replace('mm','')), 3)
                        
                    val = ("rp_"+str(i), "mm", id)
                    sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                    mycursor.execute(sql1, val)
                elif ' oz.' in v :
                    i = round(eval(v.replace(' oz.','')), 3)
                        
                    val = ("rp_"+str(i), "oz.", id)
                    sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                    mycursor.execute(sql1, val)    
                elif ' A' in v :
                    i = round(eval(v.replace(' A','')), 3)
                        
                    val = ("rp_"+str(i), "A", id)
                    sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                    mycursor.execute(sql1, val)    
                elif ' fpm' in v :
                    i = round(eval(v.replace(' fpm','')), 3)
                        
                    val = ("rp_"+str(i), "fpm", id)
                    sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                    mycursor.execute(sql1, val)
                else:      
                    i = round(eval(v), 3)
                        
                    val = ("rp_"+str(i), id)
                    sql1 = "Update DATA set value1=%s  where id = %s"
                    mycursor.execute(sql1, val)
        except:
            pass            

        if ',' in v:
            v=v.replace('rp_','')
            
            
            s = v.split(", ")
            k = s[0]
            for i in s:
                try:
                    if i == k:
                        key = 1

                        if '"' in i:
                        
                            if ' ' in i:
                                rs=round(eval(i.replace("rp_", '').replace('"','').replace(' ','+')), 3)

                                rs1 = "rp_" + str(rs)
                                val = (rs1, inc, id)
                                sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                                mycursor.execute(sql1, val)
                            else:    
                                j = round(eval(i.replace('"', '').replace("rp_", '')), 3)
                                p = rp + str(j)
                        
                                val = (p, "inch", key, id)
                                print(p)
                                sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                                mycursor.execute(sql1, val)
                        if 'mm' in i:
                                        print(i)
                                        i1 = i.replace(' mm', '')
                                        j = round(eval(i1.replace('mm', '').replace("rp_", '').replace(" ", '+').replace(',','')), 3)
                                        p = rp + str(j)
                                        val = (p, mm, key, id)
                                        print(p)
                                        sql1 = "Update DATA set  value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                                        mycursor.execute(sql1, val)        
                        elif 'hp' in i:
                            j = round(eval(i.replace('hp', '').replace("rp_", '')), 3)
                            p = rp + str(j)
                            val = (p, "hp", key, id)
                            print(p)
                            sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                            mycursor.execute(sql1, val)   
                        elif ' oz.' in i:
                            j = round(eval(i.replace(' oz.', '').replace("rp_", '')), 3)
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
                            j = round(eval(i.replace(' V', '').replace('V','').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (p, "V", key, id)
                            print(p)
                            sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                            mycursor.execute(sql1, val) 
                        elif 'V AC' in i:
                            j = round(eval(i.strip().replace('V AC', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (p, "V AC", key, id)
                            print(p)
                            sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                            mycursor.execute(sql1, val)        
                        elif 'W' in i:
                            j = round(eval(i.replace('W', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (p, "W", key, id)
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
                            
                            val = ("rp_"+i, key, id)
                        
                            sql1 = "Update DATA set value1=%s,keyvalue=%s  where id = %s"
                            mycursor.execute(sql1, val)    


                    else:
                        key = key + 1
                        print(s)
                        if 'hp' in i:
                            j = round(eval(i.replace('hp', '').replace("rp_", '')), 3)
                            p = rp + str(j)
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "hp", key)
                            sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)
                        elif '"' in i:
                            
                            if ' ' in i:
                                rs=round(eval(i.replace("rp_", '').replace('"','').replace(' ','+')), 3)

                                rs1 = "rp_" + str(rs)
                                val = (rs1, inc, id)
                                sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                                mycursor.execute(sql1, val)
                            else:    
                                j = round(eval(i.replace('"', '').replace("rp_", '')), 3)
                                p = rp + str(j)
                                print(p)
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "inch", key)
                                sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)

                        elif 'mm' in i:
                            kl=i.replace(' mm','')
                            j = round(eval(kl.replace('mm', '').replace("rp_", '').replace(" ", '+').replace(",", '')), 3)
                            p = rp + str(j)
                            print(p)
                            print(s)
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "mm", key)
                            sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)

                        
                        elif 'V DC' in i:
                            j = round(eval(i.replace('V DC', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "V DC", key)
                            sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)   
                        elif 'INC' in i:
                            j = round(eval(i.replace('W INC', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "W INC", key)
                            sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)    
                        elif 'V' in i and 'V DC' not in i and 'V AC' not in i:
                            j = round(eval(i.replace(' V', '').replace('V', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "V", key)
                            sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)    
                        elif 'V AC' in i:
                            j = round(eval(i.replace(' V AC', '').replace('V AC', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "V AC", key)
                            sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)   
                        elif ' oz.' in i:
                            j = round(eval(i.replace(' oz.', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "V AC", key)
                            sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)      
                        elif 'V AC' in v and "V DC" not in v:
                            j = round(eval(i.replace('V AC', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "V AC", key)
                            sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)    
                        elif 'X' in v:    
                            
                            p = rp + i
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, key)
                            sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)
                        else:    
                            
                            p = rp + i
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, key)
                            sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)    
                except:
                    pass            
      

    mydb.commit()

def Range3():
    sql1 = "SELECT * from DATA WHERE DataType='Range 3' "
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
        try:
            if ',' not in v:
                v=v.replace('rp_','')

                if "to" in v:
                            
                            if 'A' in v:
                                a1=v.split(' ')
                                val = ("rp_"+a1[0].replace('A',''), "A","rp_"+a1[2].replace('A','') ,"A",id)
                                sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
                                mycursor.execute(sql, val)
                            if 'V' in v:
                                a1=v.split(' ')
                                val = ("rp_"+a1[0].replace('V',''), "V","rp_"+a1[2].replace('V','') ,"V",id)
                                sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
                                mycursor.execute(sql, val)    
                            if 'V AC' in v:
                                a1=v.split(' ')
                                val = ("rp"+a1[0].replace('V AC','').replace('V',''), "V AC","rp_"+a1[2].replace('V AC','') ,"V AC",id)
                                sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
                                mycursor.execute(sql, val)
                            if 'V DC' in v:
                                a1=v.split(' ')
                                val = ("rp"+a1[0].replace('V DC',''), "V DC","rp_"+a1[2].replace('V DC','') ,"V DC",id)
                                sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s WHERE id=%s"
                                mycursor.execute(sql, val)

                            

                else:
                        if 'V AC' in v :
                            i = round(eval(v.replace('V AC','')), 3)
                                
                            val = ("rp_"+str(i), "V AC", id)
                            sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                            mycursor.execute(sql1, val) 

                        elif 'V DC' in v :
                            i = round(eval(v.replace('V DC','')), 3)
                                
                            val = ("rp_"+str(i), "V DC", id)
                            sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                            mycursor.execute(sql1, val)    

                        elif 'V' in v and 'V AC' not in v and 'V DC' not in v:
                            i = round(eval(v.replace('V','')), 3)
                                
                            val = ("rp_"+str(i), "V", id)
                            sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                            mycursor.execute(sql1, val)  

                        elif 'A' in v :
                            i = round(eval(v.replace('A','')), 3)
                                
                            val = ("rp_"+str(i), "A", id)
                            sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                            mycursor.execute(sql1, val)
                        elif 'hp' in v:
                            j = round(eval(i.replace('hp', '').replace("rp_", '')), 3)
                            p = rp + str(j)
                            val = (p, "hp", key, id)
                            print(p)
                            sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                            mycursor.execute(sql1, val)
                        elif '"' in v:
                            if ' ' in v:    
                                in1=v.split(' ')
                                print(in1)
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
                        else:      
                            i = round(eval(v), 3)
                                
                            val = ("rp_"+str(i), id)
                            sql1 = "Update DATA set value1=%s  where id = %s"
                            mycursor.execute(sql1, val)
        except:
            pass            

        if ',' in v:
            v=v.replace('rp_','')
            s = v.split(", ")
            k = s[0]
            for i in s:
                
                try:
                    if i == k:
                        key = 1
                        if "to" in i:
                            if 'A' in i:
                                a1=i.split(' ')
                                val = ("rp_"+a1[0].replace('A',''), "A","rp_"+a1[2].replace('A','') ,"A",key,id)
                                sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s,keyvalue=%s  WHERE id=%s"
                                mycursor.execute(sql, val)
                            if 'V AC' in i:
                                i=i.replace(' V','').replace(' V AC','')
                                a1=i.split(' ')
                                val = ("rp_"+a1[0].replace('V AC',''), "V AC","rp_"+a1[2].replace('V AC','') ,"V AC",key,id)
                                sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s,keyvalue=%s  WHERE id=%s"
                                mycursor.execute(sql, val)
                            if 'V DC' in i:
                                a1=i.split(' ')
                                val = ("rp_"+a1[0].replace('V DC',''), "V DC","rp_"+a1[2].replace('V DC','') ,"V DC",key,id)
                                sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s,keyvalue=%s  WHERE id=%s"
                                mycursor.execute(sql, val)  
                            if 'V' in v and 'DC' not in v and 'AC' not in v:
                                a1=v.split(' ')
                                val = ("rp_"+a1[0].replace('V',''), "V","rp_"+a1[2].replace('V,','') ,"V",key,id)
                                sql = "UPDATE DATA SET value1=%s, unit1=%s,value2=%s, unit2=%s,keyvalue=%s  WHERE id=%s"
                                mycursor.execute(sql, val) 
                               

                        else:
                            
                            print(v)
                            if '"' in i:
                                if ' ' in i:    
                                    a = i.strip('rp_').strip('RP_')
                                    b = a.strip('"')
                                    c = b.split(' ')[1]
                                    
                                    # print(d)
                                    a2 = float(Fraction(c))
                                    a3 = float(c[0]) + a2
                                    rs = round(a3, 3)

                                    rs1 = "rp_" + str(rs)
                                    val = (rs1, inc,key, id)
                                    sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s   where id = %s"
                                    mycursor.execute(sql1, val)
                                else:
                                    i = round(eval(i.replace('"','')), 3)
                                        
                                    val = ("rp_"+str(i), "inch",key, id)
                                    sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s   where id = %s"
                                    mycursor.execute(sql1, val)
                            elif 'V AC' in i :
                                i = round(eval(i.replace('V AC','')), 3)
                                    
                                val = ("rp_"+str(i), "V AC",key, id)
                                sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s   where id = %s"
                                mycursor.execute(sql1, val) 

                            elif 'V DC' in i :
                                i = round(eval(i.replace('V DC','')), 3)
                                    
                                val = ("rp_"+str(i), "V DC",key, id)
                                sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s   where id = %s"
                                mycursor.execute(sql1, val) 


                            elif 'V' in i and 'V AC' not in i and 'V DC' not in i:
                                i = round(eval(i.replace('V','')), 3)
                                    
                                val = ("rp_"+str(i), "V",key, id)
                                sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s   where id = %s"
                                mycursor.execute(sql1, val)  

                            elif 'v' in i and 'V AC' not in i and 'V DC' not in i:
                                i = round(eval(i.replace('v','')), 3)
                                    
                                val = ("rp_"+str(i), "V",key, id)
                                sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s   where id = %s"
                                mycursor.execute(sql1, val)    

                            elif 'A' in v :
                                i = round(eval(i.replace('A','')), 3)
                                    
                                val = ("rp_"+str(i), "A",key, id)
                                sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s   where id = %s"
                                mycursor.execute(sql1, val)

                            elif 'hp' in v:
                                j = round(eval(i.replace('hp', '').replace("rp_", '')), 3)
                                p = rp + str(j)
                                val = (p, "hp", key, id)
                                print(p)
                                sql1 = "Update DATA set value1=%s,unit1=%s,keyvalue=%s  where id = %s"
                                mycursor.execute(sql1, val)
                            else:      
                                i = eval(i)
                                    
                                val = ("rp_"+str(i),key, id)
                                sql1 = "Update DATA set value1=%s keyvalue=%s  where id = %s"
                                mycursor.execute(sql1, val)    


                    else:
                        key = key + 1
                        print(s)
                        if 'to' in i:
                            if 'hp' in i:
                                j = round(eval(i.replace('hp', '').replace("rp_", '')), 3)
                                p = rp + str(j)
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "hp", key)
                                sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)          
                            elif 'V DC' in i:
                                a1=i.split(' ')
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],"rp_"+a1[0].replace('V AC',''), "V AC","rp_"+a1[2].replace('V AC','') ,"V AC", key)
                                sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,value2,unit2,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)   
                            elif 'V' in i and 'V DC' not in i and 'V AC' not in i:
                                a1=i.split(' ')
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],"rp_"+a1[0].replace('V',''), "V","rp_"+a1[2].replace('V,','') ,"V", key)
                                sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,value2,unit2,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)    
                            elif 'V AC' in i:
                                a1=i.split(' ')
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],"rp_"+a1[0].replace('V AC',''), "V AC","rp_"+a1[2].replace('V AC','') ,"V AC", key)
                                sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,value2,unit2,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)   
                     
                        
                        else:
                            if 'V DC' in i:
                                j = round(eval(i.replace('V DC', '').replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(j)
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "V DC", key)
                                sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)   
                            elif 'V' in i and 'V DC' not in i and 'V AC' not in i:
                                j = round(eval(i.replace('V', '').replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(j)
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "V", key)
                                sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)    
                            elif 'V AC' in i:
                                j = round(eval(i.replace('V AC', '').replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(j)
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "V AC", key)
                                sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)     
                            elif 'V AC' in v and "V DC" not in v:
                                j = round(eval(i.replace('V AC', '').replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(j)
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "V AC", key)
                                sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)    
                            elif 'X' in v:    
                                
                                p = rp + i
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, key)
                                sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)        
                            elif 'A' in v:    
                                
                                p = rp + i
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p,"A", key)
                                sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1,unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)    

                            elif '"' in i:
                                
                                if ' ' in i:
                                    a = i.strip('rp_').strip('RP_')
                                    b = a.strip('"')
                                    c = b.split(' ')[1]
                                    
                                    # print(d)
                                    a2 = float(Fraction(c))
                                    a3 = float(c[0]) + a2
                                    rs = round(a3, 3)

                                    rs1 = "rp_" + str(rs)
                        
                                    val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],rs1, "inch", key)
                                    sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                    mycursor.execute(sql1, val)
                                else:    
                                    j = round(eval(i.replace('"', '').replace("rp_", '')), 3)
                                    p = rp + str(j)
                                    print(p)
                                    val = (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],p, "inch", key)
                                    sql1 = "INSERT INTO DATA (Ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                    mycursor.execute(sql1, val)    
                except:
                    pass            
                        
      

    mydb.commit()



def thread():
    sql1 = "SELECT * from DATA   "
    mycursor.execute(sql1)
    l = mycursor.fetchall()
    for x in l:
        value = x[11]
        Datatype = x[5]
        attribute = x[6]
        value1 = x[10]
        inc = "Inch"
        rp = "rp_"
        mm = "mm"
        id = x[0]
        Deg = ""
        if "Numerical" in Datatype or 'Range 2' in Datatype and ',' not in value1:

                    if "Thread Per Inch" in attribute or "Threads Per Inch" in attribute :
                        if '-' in value1:
                            di = value1.split("-")
                            if '"' in value1 or "/" in value1:
                                i = di[1]
                                p = rp + str(i)
                                val = (p,id)
                                sql1 = "Update DATA set value1=%s  where id = %s"
                                mycursor.execute(sql1, val)
                            else:
                                print(value1)
                                he = value1.split('-')
                                n = rp + he[1]
                                val = (value1, id)
                                sql1 = "Update DATA set value1=%s where id = %s"
                                mycursor.execute(sql1, val)

                            if "Thread Dia." in attribute:
                                di = value1.split("-")
                                if '"' in value1 or "/" in value1:
                                    i = di[0]
                                    p = rp + str(round(eval(i).replace('rp_',''),3))
                                    val = (p,"inch",id)
                                    sql1 = "Update DATA set value1=%s,unit1=%s  where id = %s"
                                    mycursor.execute(sql1, val)
                                else:
                                    print(value1)
                                    he = value1.split('-')
                                    n = rp + he[0]
                                    val = (value1, id)
                                    sql1 = "Update DATA set value1=%s where id = %s"
                                    mycursor.execute(sql1, val)    

           


                    
                        
    mydb.commit()

def dimensions():
    sql1 = "SELECT * from DATA WHERE DataType='Dimension'   "
    mycursor.execute(sql1)
    l = mycursor.fetchall()
    print(len(l))
    for x in l:
       
        v = x[8]
        c = x[5]
        inc = "Inch"
        rp = "rp_"
        mm = "mm"
        id = x[0]
        print(x[8])
        v=v.lower()
        print(v)
        if '-' in v and '#' not in v:
            v=v.replace('rp_','rp_#')
        if 'x' not in v:
            if '#' in v:
                        n=v.split('-')
                        ne = n[0].replace('#', '')
                        p = ne
                        M = '#'
                        val = ("thread Dia",x[6], x[8], M, p,id)
                        print(p)
                        sql1 = "Update DATA set  Super_Att=%s,NEW_ATTRIBUTE=%s,VALUE=%s,PreP=%s,value1=%s  where id = %s"
                        mycursor.execute(sql1, val)

                        j = round(eval(n[1].strip().replace('"', '').replace("rp_", '').replace(" ", '+')), 3)
                        p = rp + str(j)

                        val = (x[1],x[2],x[3],x[4],x[5],x[6],"Thread Per inch",x[8],p, "inch")
                        sql1 = "INSERT INTO DATA (ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                        mycursor.execute(sql1, val)
            else:
                    if '"' in v:
                        i = round(eval(v.replace("rp_", '').replace('"','').replace(" ", '+')), 3)
                        p = rp + str(i)
                        print(p)
                       
                        val = (x[6], p, inc, id)
                        sql1 = "Update DATA set NEW_ATTRIBUTE=%s,value1=%s,unit1=%s  where id = %s"
                        mycursor.execute(sql1, val)      

                    if ' ft' in v:
                        i = round(eval(v.replace("rp_", '').replace(' ft','').replace(" ", '+')), 3)
                        p = rp + str(i)
                        print(p)
                       
                        val = (x[6], p, "ft", id)
                        sql1 = "Update DATA set NEW_ATTRIBUTE=%s,value1=%s,unit1=%s  where id = %s"
                        mycursor.execute(sql1, val)             

        if 'x' in v:
            di = v.split('x')
            

            print(di)
            i1 = di[0]
            i2 = di[1]
            try:
                i3=di[2]
            except:
                pass    
            print(di)
            print("dsdds")
            
            for i in di:
        
                if i == i1:
                    i=str(i)
                    key = 1
        
                    if '/' in i and '#' not in i:
                        if 'sq. in' in i:
                            io = i1.split(' sq. in.')
                            g = round(eval(io[0].replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(g)
                            print(p)
                            s = 'A'
                            val = (s, x[6], p, key, "sq. in.", id)
                            sql1 = "Update DATA set  Super_Att=%s,NEW_ATTRIBUTE=%s,value1=%s,keyvalue=%s,unit1=%s  where id = %s"
                            mycursor.execute(sql1, val)
                        else:  
                            if '"' in v:  
                                io = i1.split('"')
                                g = round(eval(io[0].replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(g)
                                print(p)
                                s = 'A'
                                val = (s, x[6], p, key, inc, id)
                                sql1 = "Update DATA set  Super_Att=%s,NEW_ATTRIBUTE=%s,value1=%s,keyvalue=%s,unit1=%s  where id = %s"
                                mycursor.execute(sql1, val)

                            elif 'ft' in v:
                                    io = i.split(' ft')
                                    g = round(eval(io[0].replace("rp_", '').replace(" ", '+')), 3)
                                    p = rp + str(g)
                                    s = 'A'
                                    val = (s, x[6], p, key, "ft", id)
                                    sql1 = "Update DATA set  Super_Att=%s,NEW_ATTRIBUTE=%s,value1=%s,keyvalue=%s,unit1=%s  where id = %s"
                                    mycursor.execute(sql1, val)    
                    else:
                        if '#' in v:
                            n=di[0].split('-')
                            ne = n[0].replace('#', '')
                            p = ne
                            M = '#'
                            val = ("thread Dia",x[6], x[8], M, p,key, id)
                            print(p)
                            sql1 = "Update DATA set  Super_Att=%s,NEW_ATTRIBUTE=%s,VALUE=%s,PreP=%s,value1=%s,keyvalue=%s  where id = %s"
                            mycursor.execute(sql1, val)

                            j = round(eval(n[1].strip().replace('"', '').replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(j)

                            val = (x[1],x[2],x[3],x[4],x[5],x[6],"Thread Per inch",x[8],p, key)
                            sql1 = "INSERT INTO DATA (ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val) 
                        else:
                            if 'mm' in v and 'l' not in v:
                                io = i1.split(' ')
                                g = round(eval(io[0].strip().replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(g)
                                print(p)
                                s = 'A'
                                val = (s, x[6], p, key, mm, id)
                                sql1 = "Update DATA set  Super_Att=%s,NEW_ATTRIBUTE=%s,value1=%s,keyvalue=%s,unit1=%s  where id = %s"
                                mycursor.execute(sql1, val)


                            elif '" h' in v:        
                                
                                io = i1.replace('" h','')
                                print(io)

                                g = round(eval(io.strip().replace("rp_", '').replace(" ", '+')), 3)
                                print(g)
                                p = rp + str(g)
                                print(p)
                                s = 'H'
                                val = (str(s), str(x[6]), str(p), str(key),'inch', str(id))
                                sql1 = "Update DATA set  Super_Att=%s,NEW_ATTRIBUTE=%s,value1=%s,keyvalue=%s,unit1=%s  where id = %s"
                                mycursor.execute(sql1, val)   
                            elif '" w' in v:        
                                
                                io = i1.replace('" w','')
                                print(io)

                                g = round(eval(io.strip().replace("rp_", '').replace(" ", '+')), 3)
                                print(g)
                                p = rp + str(g)
                                print(p)
                                s = 'W'
                                val = (str(s), str(x[6]), str(p), str(key),'inch', str(id))
                                sql1 = "Update DATA set  Super_Att=%s,NEW_ATTRIBUTE=%s,value1=%s,keyvalue=%s,unit1=%s  where id = %s"
                                mycursor.execute(sql1, val)     

                            elif ' mm l' in v:
                                io = i.replace(' mm l','')
                                g = round(eval(io.strip().replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(g)
                                print(p)
                                s = 'L'
                                val = (s, x[6], p, key,'mm', id)
                                sql1 = "Update DATA set  Super_Att=%s,NEW_ATTRIBUTE=%s,value1=%s,keyvalue=%s,unit1=%s  where id = %s"
                                mycursor.execute(sql1, val) 

                            else:
                                if 'mm' in v:
                                    io = i.split('mm')
                                    g = round(eval(io[0].strip().replace("rp_", '').replace(" ", '+')), 3)
                                    p = rp + str(g)
                                    s = 'A'
                                    val = (s, x[6], p, key, mm, id)
                                    sql1 = "Update DATA set  Super_Att=%s,NEW_ATTRIBUTE=%s,value1=%s,keyvalue=%s,unit1=%s  where id = %s"
                                    mycursor.execute(sql1, val)
                                elif '"' in v and 'h' not in v:
                                    io = i.split('"')
                                    g = round(eval(io[0].replace("rp_", '').replace(" ", '+')), 3)
                                    p = rp + str(g)
                                    s = 'A'
                                    val = (s, x[6], p, key, "inch", id)
                                    sql1 = "Update DATA set  Super_Att=%s,NEW_ATTRIBUTE=%s,value1=%s,keyvalue=%s,unit1=%s  where id = %s"
                                    mycursor.execute(sql1, val)

                                elif 'ft' in v:
                                    io = i.split(' ft')
                                    g = round(eval(io[0].replace("rp_", '').replace(" ", '+')), 3)
                                    p = rp + str(g)
                                    s = 'A'
                                    val = (s, x[6], p, key, "ft", id)
                                    sql1 = "Update DATA set  Super_Att=%s,NEW_ATTRIBUTE=%s,value1=%s,keyvalue=%s,unit1=%s  where id = %s"
                                    mycursor.execute(sql1, val)    


                        
                elif i == i2:
                    key = 2
                    print(i)
                    if '#' in v:
                        if '/' in i:
                            print("la")
                            io = i.split('"')
                            g = round(eval(io[0].replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(g)
                            print(p)
                            s = 'B'
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],"length",x[8],p, "inch", key)
                            sql1 = "INSERT INTO DATA (ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)
                        else:

                            p = rp + i
                            s = 'B'
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],"length",x[8],p, "inch", key)
                            sql1 = "INSERT INTO DATA (ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val)
                    else:
                        if '/' in i:
                            print("la")
                            io = i.split('"')
                            g = round(eval(io[0].replace("rp_", '').replace(" ", '+')), 3)
                            p = rp + str(g)
                            print(p)
                            s = 'B'
                            
                            val = (x[1],x[2],x[3],x[4],x[5],x[6],s,x[8],p, "ft", key)
                            sql1 = "INSERT INTO DATA (ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                            mycursor.execute(sql1, val) 
                        elif '" w' in i2:
                                io = i2.replace('" w','')
                                g = round(eval(io.strip().replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(g)
                                print(p)
                                s = 'W'
                                
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],s,x[8],p, "inch", key)
                                sql1 = "INSERT INTO DATA (ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val) 
                        elif '" h' in i2:
                                io = i2.replace('" h','')
                                g = round(eval(io.strip().replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(g)
                                print(p)
                                s = 'H'
                                
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],s,x[8],p, "inch", key)
                                sql1 = "INSERT INTO DATA (ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)        
                        elif ' mm w' in v:
                                io = i.replace(' mm w','')
                                g = round(eval(io.strip().replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(g)
                                print(p)
                                s = 'W'
                                
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],s,x[8],p, "mm", key)
                                sql1 = "INSERT INTO DATA (ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)         
                        
                        else:
                            if 'mm' in v:
                                io = i.split('mm')
                                g = round(eval(io[0].strip().replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(g)
                                s = 'B'
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],"B",x[8],p, "mm", key)
                                sql1 = "INSERT INTO DATA (ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)
                            elif '"' in v:
                                io = i.split('"')
                                g = round(eval(io[0].replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(g)
                                s = 'B'
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],"B",x[8],p, "inch", key)
                                sql1 = "INSERT INTO DATA (ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)   

                            elif 'ft' in v:
                                io = i.split(' ft')
                                g = round(eval(io[0].replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(g)
                                s = 'B'
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],"B",x[8],p, "ft", key)
                                sql1 = "INSERT INTO DATA (ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)     

                elif i==i3:    
                    key=3
                    if '" d' in i3:
                                io = i3.replace('" d','')
                                g = round(eval(io.strip().replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(g)
                                print(p)
                                s = 'D'
                               
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],s,x[8],p, "inch", key)
                                sql1 = "INSERT INTO DATA (ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)   
                    

                    elif ' mm h' in i3:
                                io = i3.replace(' mm h','')
                                g = round(eval(io.strip().replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(g)
                                print(p)
                                s = 'H'
                            
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],s,x[8],p, "mm", key)
                                sql1 = "INSERT INTO DATA (ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)   
                    else:
                            if 'mm' in v:
                                io = i3.split('mm')
                                g = round(eval(io[0].replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(g)
                                s = 'C'
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],s,x[8],p, "mm", key)
                                sql1 = "INSERT INTO DATA (ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)
                            if '"' in i3:        
                                io = i3.split('"')
                                g = round(eval(io[0].strip().replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(g)
                                print(p)
                                s = 'C'
                                
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],s,x[8],p, "inch", key)
                                sql1 = "INSERT INTO DATA (ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)    

                            if 'ft' in v:
                                io = i.split(' ft')
                                g = round(eval(io[0].replace("rp_", '').replace(" ", '+')), 3)
                                p = rp + str(g)
                                s = 'C'
                                val = (x[1],x[2],x[3],x[4],x[5],x[6],s,x[8],p, "ft", key)
                                sql1 = "INSERT INTO DATA (ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                                mycursor.execute(sql1, val)                                            
                else:
                    key=4
                    io = i.split('"')
                    g = round(eval(io[0].replace("rp_", '').replace(' ','+')), 3)
                    p = rp + str(g)
                    s = 'D'
                    val = (x[1],x[2],x[3],x[4],x[5],x[6],s,x[8],p, "inch", key)
                    sql1 = "INSERT INTO DATA (ti,item_No ,Type,L3,DataType,NEW_ATTRIBUTE,Super_Att,VALUE,value1, unit1,keyvalue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                    mycursor.execute(sql1, val)
                    

            
                    
    mydb.commit()    



def mapping():
    sql1 = "SELECT * from map"
    mycursor.execute(sql1)
    l = mycursor.fetchall()
    print(len(l))
    for c in l:
        value=c[4]
      
        if ',' in value:
            sp=value.split(',')
            k=sp[0]
            for i in sp:
                if i==k:
                    print(i)
                    key = 1
                    p = str(i)
                    val = (c[1],c[2],c[3],p,c[0])
                    print(p)
                    sql1 = "Update map set name=%s,mapped=%s,map=%s,ma=%s  where id = %s"
                    mycursor.execute(sql1, val)
                    print('lol')

                else:   
                    print(i)
                    p = str(i)
                    val = (c[1],c[2],c[3],p)
                    sql1 = "INSERT INTO map (name,mapped,map,ma) values(%s,%s,%s,%s) "
                    mycursor.execute(sql1, val) 
                    print('lol')

    mydb.commit()                





def add(): 
    sql1 = "SELECT DISTINCT iD from A"
    mycursor.execute(sql1)
    l = mycursor.fetchall()
    for c in l:   
        sql1= "SELECT * from A WHERE iD= %s"
        val=(c)
        mycursor.execute(sql1,val)
        g = mycursor.fetchall()
        h=''
        for hj in g:
            h=h+hj[3]+","
        print(h)
        val = (c)
        sql1= "SELECT * from A WHERE iD= %s"
        mycursor.execute(sql1,val)
        gb = mycursor.fetchall()
        print('lol')
        for hk in gb:
            val=(h[:-1],hk[0])
            sql1="update A set J=%s where ids = %s"
            mycursor.execute(sql1,val)
            mydb.commit()