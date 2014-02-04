#!/usr/bin/python
print 'Content-Type: text/html\n\n'
from random import randint
numbers = []
for i in range(4):
    numbers.append(randint(0,649))
for i in range(len(numbers)):
    numbers[i] = str(numbers[i])

string = """<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="../general.css">
    <title> ABOUT</title>
</head>
<body>
    <h1>
	<i>about</i>
    </h1>
    <h2> 
	<a href = "pokestyle.html">   the unofficial pokemon comparator </a>
    </h2>
	<hr>
	<box> 
	    <a href = "pokestyle.html"> home </a> 
	    <a href = "dex.py"> dex </a> 
	    <a href = "analysis.py"> analysis </a>  
	</box>
	<p><b><u>W<i>H</i>A<i>T?</i></u></b></p>
	<p class = "text">The <i>Unofficial Pokemon Comparator</i> is a repository of information on all 649 Pokemon. It includes their stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed), types, sprites, and abilities. You can view these properties individually in the 'dex' page, or you can compare up to 3 Pokemon in the 'analysis' page. It'll tell you which Pokemon is stronger in every single stat (with the difference noted on the right), the net sum of the differences for the Pokemon with the higher net sum, and it will note if one Pokemon has a type advantage over the other. Click one of the links on the bottom to begin!</p> 
	<p><b><u><i>W</i>HY<i>?</i></u></b></p>
	<p class = "text">Pokemon seemed like the most fun thing to do. Furthermore, Pokemon is actually very mathematical, and the amount of Pokemon is very expansive, so it made sense to use it for an analysis/comparison project. I sort of had to do this for a project in a CS class. Actually, I didn't. I don't even exist in said CS class. Goddamnit. 

        <p> <b><u><i>W</i>HO<i>?</i> </u></b> </p>
	<p class = "text"> <b>I</b> wrote the HTML/CSS for all 4 pages, as well as the Python code used to analyze the Pokemon data. The data included CSV files of all the Pokemon's number values, their names, types, stats, and abilities. This data was provided by the open-source <b>veekun</b> pokedex (the csv files are on their <u><a href = "https://github.com/veekun/pokedex">GitHub</a></u>). The Pikachu picture on the right was supplied by <u><a href = "http://bulbapedia.bulbagarden.net/wiki/Pikachu">Bulbapedia</a></u>. </p>
	<p> <b><u>WhaT Did YoU ThInK? WhAt HapPenEd?</u></b></p>
	<p class = "text">About styling, I learned that good design doesn't just hit you in the head one day. You gradually get better over time. Maybe I can make some great looking sites before I apply for colleges.<br> About OS X, I learned that Mr. Brooks's web servers don't work. Blegh. <br> </p>

	<p> <img class = "img1" src = "http://www.serebii.net/art/th/N0.png"> </p>
	<p> <img class ="img2" src = "http://www.serebii.net/art/th/N1.png"> </p>
	<p> <img class = "img3" src = "http://www.serebii.net/art/th/N2.png"> </p>
	<p> <img class = "img4" src = "http://www.serebii.net/art/th/N3.png"> </p>
	</body>
</html>"""
for i in range(len(numbers)):
    string = string.replace('N' + str(i), numbers[i])
print string
