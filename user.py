'''san=(input("San kirit: "))
if san.isdigit:
    san=int(san)
    if san>0 and san<30:
        qaldiq=san%10
        letter=''
        if san>=10 and san<20:
            letter='on '
        if san>=20 and san<30:
            letter='jigirma '
        if qaldiq==1:
            letter+='bir'
        elif qaldiq==2:
            letter+='eki'
        elif qaldiq==3:
            letter+="u'sh"
        elif qaldiq==4:
            letter+="to'rt"
        elif qaldiq==5:
            letter+='bes'
        elif qaldiq==6:
            letter+='alti'
        elif qaldiq==7:
            letter+='jeti'
        elif qaldiq==8:
            letter+='segiz'
        elif qaldiq==9:
            letter+="tog'iz"
        print(letter)
    else:
        print('0den 30ga shekemgi san kiritin !')
else:
    print('San kiritin !')

print("Chortik bahasi 30_000 min' som")
a=int(input("Neshe som beresiz: "))
if a<=10000 :
    print("yag'aw bolmayd apa !")
if a>10000 and a<=20000:
    print("Yag'aw kittay qosin'sa !")
elif a>=23000 and a<=30000:
    print("Yaqshi kelistik !")'''