#!/usr/bin/python
import cgi,cgitb
from math import ceil
cgitb.enable()
print 'Content-Type: text/html\n\n'
data = cgi.FieldStorage()
###THIS SECTION IS DATA###
table = "Sprite, Number, Name, Type(s), HP, Atk, Def, SpA, SpD, Spe, Ability/Abilities, Color\n"
statid = ['Stats', 'HP', 'Atk', 'Def', 'SpA', 'Spe', 'Accuracy', 'Evasion']
typeid = ['Types', 'Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Dark']
colorid = ['Colors', 'Black', 'Blue', 'Brown', 'Gray', 'Green', 'Pink', 'Purple', 'Red', 'White', 'Yellow']
#ability is different because there are many abilities, each with a flavor text, instead of a limited set of colors, for example
#because of it's length, i need to use python to automate generation of ability
abilityid = open('abilityidentifer.csv', 'r').read().split('\n')
for i in range(len(abilityid)):
    abilityid[i]= abilityid[i].split(',')
    if i == 0:
        abilityid[i] = 'indexHolder'
    else:
        abilityid[i] = (abilityid[i])[1].capitalize()
abilityflavor =  {}
abilitytext = open('abilitytext.csv','r').read().split('."')
for i in range(len(abilitytext)):
    abilitytext[i] = abilitytext[i].split(',')
    if i == 0:
        abilityflavor[0] = "indexHolder"
    else:
        text = abilitytext[i] 
        if int(text[2]) == 9:
            abilityflavor[abilityid[int((text[0].strip('\n')))]] = text[3].replace('"','').replace('\n',' ') + '.'
#now for the names
pokename = [['indexHolder']]
pokemen = open('names.csv','r').read().split('\n')
for i in range(len(pokemen)):
    pokemen[i] = pokemen[i].split(',')
startmen = pokemen[0]
colorindex = int(startmen.index('color_id')) #get the index of colors
pokemen.pop(0) #name labels; don't need that (no pokemon named 'Identifier_ID'!)
types = open('types.csv','r').read().split('\n')
for i in range(len(types)):
    types[i] = types[i].split(',')

stats = [['indexHolder']]
statadd = open('stats.csv','r').read().split('\n')
for i in statadd:
    stats.append(i.split(','))
for i in range(1,len(stats)):
    stats[i].pop(3)
(stats[1])[0] = '1' #for some reason it's giving me xx1, wtf 
#change 0s to 000s, 10s to 010s, etc.
def dexify(i):
    if i < 100 and i >= 10:
        return '#' + '0' + str(i)
    elif i < 10:
        return '#' + '00' + str(i)
    elif i >= 100:
        return '#' + str(i)
def undexify(s):
    #un-dexifies the dexified part of the Pokemon's name. I need it to find the integer position of a pokemon
    return int(s.strip('#'))
man = table
tC = 0
nC = 0
##no way in hell i'm going to save 649 image files; time to use the Internet~!
def getPicture(n):
    return '<img src = "http://www.serebii.net/blackwhite/pokemon/%s.png">'%dexify(n)[1:]
#pics, numbers, names, types
while nC < len(pokemen):
    man += getPicture(nC + 1) + ","
    man += dexify(nC + 1) + ","
    man += (pokemen[nC])[1].capitalize()
    if (types[tC + 1])[2] == '2':
        man += "," + typeid[int((types[tC])[1])] + '/' + typeid[int((types[tC + 1])[1])] 
        tC += 2
        nC += 1
    else:
        man += "," + typeid[int((types[tC])[1])] 
        tC += 1
        nC += 1
    man += "\n"
man = man.split('\n')
man.pop(len(man) - 1)
for i in range(len(man)):
    man[i] = man[i].split(',')

sC = 1
mC = 1
while mC < len(man):
    currentStat = stats[sC]
    if sC != 3894 and currentStat[0] == (stats[sC + 1])[0]:
        man[mC].append(currentStat[2])
        sC += 1
    else:
        man[mC].append(currentStat[2])
        sC += 1
        mC += 1
#finished stats, swagmasteryoloface
def giveText(index):
    return abilityid[index] + ' : ' + abilityflavor[abilityid[index]]
nameabil = open('abilities.csv').read().split('\n')
nameabil[0] = 'indexHolder'
for i in range(1,len(nameabil)):
    nameabil[i] = nameabil[i].split(',')
    nameabil[i].pop(2)
    nameabil[i].pop(2)
    (nameabil[i])[1] = (nameabil[i])[1].capitalize()
aC = 1
mC = 1
while mC < len(man):
    currentAbil = nameabil[aC]
    if aC != 1602 and currentAbil[0] == (nameabil[aC + 1])[0]:
        man[mC].append('')
        (man[mC])[10] += giveText(int(currentAbil[1])) + '/'
        aC += 1
    else:
        man[mC].append('')
        (man[mC])[10] += giveText(int(currentAbil[1]))
        aC += 1
        mC += 1
for i in range(0,len(man) - 1):
    man[i + 1].append(colorid[int((pokemen[i])[colorindex])])
for i in range(0, len(man) - 1):
    for j in range(man[i].count('')):
        man[i].remove('')

FINALSTRING = """"""
for i in man:
    for j in i:
        FINALSTRING += j + ","
    FINALSTRING = FINALSTRING[:len(FINALSTRING) - 1] #gets rid of awkward last comma
    FINALSTRING += "\n"

##WRITE TO NECESSARY CSV
FINALWRITE = open('extracted.csv','w')
FINALWRITE.write(FINALSTRING)
FINALWRITE.close()
###THIS SECTION IS ANALYSIS####
f = open('extracted.csv','r')
lines = f.readlines()
f.close()
for i in range(len(lines)):
    lines[i] = lines[i].split(',')
for i in range(len(lines[0])):
    (lines[0])[i] = (lines[0])[i].strip(' ') #weird spacing before stats; will mess up indexing later 
def tableMaker(first,second):
    firstpok = lines[first]
    secondpok = lines[second]
    ref = lines[0]
    body = ""
    body += '<table border = "1">\n'
    poks = [firstpok,secondpok]
    for k in range(0,4):
        body += "<tr>"
        for j in poks:
            body += "<td><b>" + ref[k] + "</b>" + ": "+ j[k] + "</td>"
        body += "</tr>\n"
    netdiff = 0
    for k in range(4,10):
        body += "<tr>"
        firstNum = int(firstpok[k])
        secondNum = int(secondpok[k])
        netdiff += firstNum - secondNum
        if firstNum >  secondNum:
            diff = str(firstNum - secondNum)
            body+= "<td><b>" + ref[k] + "</b>: <better>" + firstpok[k] + "</better>" + " (+" + diff + ")</td>"
            body += "<td><b>" + ref[k] + "</b>: <worse>" + secondpok[k] + "</worse>" + " (-" + diff + ")</td>"
        elif secondNum > firstNum:
            diff = str(secondNum - firstNum)
            body+= "<td><b>" + ref[k] + "</b>: <worse>" + firstpok[k] + "</worse>" + " (-" + diff + ")</td>"
            body += "<td><b>" + ref[k] + "</b>: <better>" + secondpok[k] + "</better>" + " (+" + diff + ")</td>"
        else:
           for i in [firstpok, secondpok]:
               body+= "<td><b>" + ref[k] + "</b>: <neutral>" + i[k] + "</neutral></td>"
        body += "</tr>"
    body += "<tr>"
    for i in range(2):
        body += "<td><b>Net Diff</b>: " + str((1 - 2 * i) * netdiff) + "</td>" #1 - 2 * i turns the second net diff into -netdiff, which it is (netdiffs are opposite)
    body += "</tr>"
    body += "<tr>"
    for j in poks:
        body+= "<td>" + "<b>" + ref[10] + "</b>" + ": " + "<br>" + j[10].replace('/','<br>') + "</td>"
    body += "</tr>\n"
    body += "<tr>"
    for j in poks:
        body+= "<td>" + "<b>" + ref[11] + "</b>" + ": " + "\n" + '<div style = "color: ' + j[11].lower().strip('\n') + ';">' + j[11] + "</div></td>"
    body += "</tr>"
    body += "</table>\n"
    return body
def tableSplitter(Range1,Range2,lines):
    body = "<table border = 1>"
    if Range2 >= len(lines):
        Range2 = len(lines)
    if Range1 > 0:
        body += "<tr>"
        for i in lines[0]:
            body += "<td>" + i + "</td>"
        body += "</tr>"
    for i in range(Range1,Range2):
        body += "<tr>\n"
        for j in lines[i]:
            j = j.replace('./','.<br>')
            body += "<td>" + j + "</td>"
        body += "</tr>"
    body += "</table>"
    return body
def dexMaker(lines,data,spp): #spp = show per page
    body = ""
    typeAdd = '&type=on&Types=%s'%data['Types'].value if 'type' in data else ''
    ABCAdd = '&ABC=on' if 'ABC' in data else ''
    colorAdd = '&color=on&Colors=%s'%data['Colors'].value if 'color' in data else ''
    textAdd = '&text=on&Text=%s'%data['Text'].value if 'text' in data else ''
    if 'page' not in data or data['page'].value == '1':
        spp = data['rpp'].value
        nextp = '' if int(spp) >= len(lines) - 1 else '&page=2'
        lastp = '' if int(spp) >= len(lines) - 1 else '&page=' + str(int(ceil(len(lines)/float(spp))))
        body += '<a href = "analysisv2.py?choose=dex%s&rpp=%s%s%s%s%s"> LAST </a><br>'%(lastp,spp,typeAdd,ABCAdd,colorAdd,textAdd)
        body += '<a href = "analysisv2.py?choose=dex%s&rpp=%s%s%s%s%s"> NEXT </a><br>'%(nextp,spp,typeAdd,ABCAdd,colorAdd,textAdd)
        body += tableSplitter(0,int(spp) + 1,lines)
    else:
        p = data['page'].value
        spp = data['rpp'].value
        lastp = '' if int(p) == 2 else '&page=' + str(int(p) - 1)
        nextp = '' if int(p) >= len(lines)/int(spp) else '&page=' + str(int(p) + 1) #one-line ifs cause im just that cool        
        body += '<a href = "analysisv2.py?choose=dex%s&rpp=%s%s%s%s%s"> LAST </a><br>\n'%(lastp,spp,typeAdd,ABCAdd,colorAdd,textAdd)
        body += '<a href = "analysisv2.py?choose=dex%s&rpp=%s%s%s%s%s"> NEXT </a><br>\n'%(nextp,spp,typeAdd,ABCAdd,colorAdd,textAdd)
        body += tableSplitter((int(p) - 1) * int(spp) + 1, (int(p) * int(spp)) + 1, lines)
    return body
def idSelector(IDlist):
    body = ""
    body += '<select name = "%s">\n'%IDlist[0]
    for i in range(1,len(IDlist)):
        body += '<option value = "%s">%s</option>\n'%(IDlist[i],IDlist[i])
    body += '</select>\n'
    return body
#resultsperpage select tag:
selectag = '<select name = "rpp">\n'
for i in range(1,650):
    selectag += '<option value = "%d">%s</option>\n'%(i,i)

if len(data) == 0:
    head = """<!DOCTYPE html>
<html>
<head>
    <title> Comparator </title>
</head>
<body>
<form action = "analysisv2.py" method = "get">
   <h2> <input type = "radio" name = "choose" value = "compare"> Compare two Pokemon: <br></h2>
   Pokemon 1 : <select name = "pok1">"""
    tail = """</select>
<br>
<h2><input type = "radio" name = "choose" value = "dex"> Or just look at the Pokedex. <br></h2>
<b>Remember to choose your results per page.</b> <br>
%s </select><br>
<input type = "radio" name = "type">
You can sort the Pokedex so that it only shows Pokemon of Type : <br>
%s <br>
<input type = "radio" name = "color">
And/or Color : <br>
%s <br>
<input type = "radio" name = "text">
You can also search for a substring in a Pokemon's name (e.g.: you can put in 'Pika' and you would still get 'Pikachu').
<input name = "Text"> <br>
%s And click this to sort alphabetically versus alphanumerically. <br>
<input type = "Submit" value = "Go!"> 
</form>
<br>
Choose whether to compare Pokemon or to view the Dex (you must choose one of the big, bold radio buttons). For viewing the Dex, you must first decide how many Pokemon per page should be displayed.
Then, you have the option of limiting the page to display only 1 Type (hit the radio button and select your selected Type from the drop-down menu), or
to sort only Pokemon of a certain color. You can also hit the radio buttion for alphabetical sorting, to sort the Pokemon from A to Z as opposed to 1 through 649.
</body>
</html>""" %(selectag,idSelector(typeid), idSelector(colorid),'<input type = "radio" name = "ABC">')
  
    for i in range(1,len(lines)):
        head += """<option value = "%s">%s</option>"""%(((lines[i])[1])[1:],(lines[i])[2]) + "\n" #val=number of Pokemon, displayed to the user is the name
    head += """</select>
<br>
Pokemon 2 : <select name = "pok2">
"""
    for i in range(1,len(lines)):
        head += """<option value = "%s">%s</option>"""%(((lines[i])[1])[1:],(lines[i])[2]) + "\n"
    print head + tail

    
else:
    begin = """<!DOCTYPE html>
<html>
<head>
    <title> %s </title>
    <style>
        * {
        text-align: center;
        }
        better {
        color: green;
        }
        worse {
        color: red;
        }
        neutral {
        color: yellow;
        }
        
        img {
        display: block;
        margin: 0 auto;
        }
        body {
        background-color: lightblue;
        }
    </style>
</head>
<body>
"""%(data['choose'].value) if 'choose' in data else '<!DOCTYPE html><title>Hey!</title><body>'
    end = """</body>
</html>"""
    if 'choose' not in data:
        print begin + 'Dude! You didn\'t choose whether to compare or sort and display the Dex! Go <a href = "analysisv2.py"> back </a> and try again.' + end
    else:
        if data['choose'].value == 'dex':
	    OGlines = lines
            if 'rpp' not in data:
                print begin + '...You forgot to choose how many results per page... Go <a href = "analysisv2.py">BACK!</a>'
            else:
                spp = int(data['rpp'].value)
                if 'type' in data:
                    chosenOnes = [lines[0]]
                    types = sorted(types, key = lambda f: f[2])
                    for i in range(649):
                        chosenType = str(typeid.index(data['Types'].value))
                        this = types[i]
                        if this[1] == chosenType:
                            good = int(this[0])
                            chosenOnes.append(lines[good])
                    for i in range(673,968): 
                        this = types[i]
                        if this[1] == chosenType:
                            good = int(this[0])
                            chosenOnes.append(lines[good])
                    chosenOnes[1:] = sorted(chosenOnes[1:], key = lambda f: undexify(f[1]))
                    lines = chosenOnes
                if 'ABC' in data:
                    lines[1:] = sorted(lines[1:], key = lambda f: f[2])
                if 'color' in data:
                    check = data['Colors'].value + '\n'
                    chosenOnes = [lines[0]]
                    for i in lines:
                        if i[len(i) - 1] == check:
                            chosenOnes.append(i)
                    lines = chosenOnes
                if 'text' in data:
                    for i in range(len( pokemen)):
			pokemen[i] = (pokemen[i])[1].capitalize()
		    text = data['Text'].value.lower()
                    chosenOnes = [lines[0]]
                    for i in lines:
                        if text in i[2]:
        		    chosenOnes.append(OGlines[pokemen.index(i[2]) + 1])
                    lines = chosenOnes
		body = dexMaker(lines,data, spp)
		print begin + body + end
		
        elif data['choose'].value == 'compare':
            body = tableMaker(int(data['pok1'].value),int(data['pok2'].value))
            print begin + body + end
   
