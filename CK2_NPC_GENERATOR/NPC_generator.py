OUTPUT_FOLDER = "Characters"

import random, os
import info as info

numOfTraits = [1, 2, 3, 4, 5]

lessChance = [1, 2, 3]
chance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
moreChance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
              21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

randNum = random.choice(range(1, 6))
traitNums = random.sample(numOfTraits, randNum)


lessFate = random.choice(lessChance)
fate = random.choice(chance)
moreFate = random.choice(moreChance)

startDates = ["769", "867", "936", "1066", "1337"]
randomStartDate = random.choice(startDates)

sexes = ['male', 'female']
sex = random.choice(sexes)

#frozenKeys = frozenset(info.trait_exclusions.items())

theTraits = random.choice(info.traitsList)

info.traitsList.remove(theTraits)

culture = random.choice(list(info.cultureList.keys()))

Culture = info.cultureList[culture]

religions = random.choice(list(info.religionList.keys()))

Religions = info.religionList[religions]

edu_traits = random.choice(info.education_traits)

healthTraits = random.choice(info.health_traits)
severeHealthTraits = random.choice(info.severe_health_traits)

physique = random.choice(info.physique_traits)

Male = Culture.M
Female = Culture.F
Lastname = Culture.L
Religion = Religions.types

if sex is 'male':
    Fname = random.choice(Male)
else:
    Fname = random.choice(Female)

Lname = random.choice(Lastname)

Rel = random.choice(Religion)

north_germanic = False
central_germanic = False
western_germanic = False
latin = False
iberian = False
byzantine = False
celtic = False
finno_ugric = False
baltic = False
altaic = False
arabic = False
east_slavic = False
west_slavic = False
south_slavic = False
magyar = False
iranian = False
east_african = False
central_african = False
west_african = False
mesoamerican = False
israelite = False
indo_aryan = False
dravidian = False
tibetan = False
chinese = False

#trAit = random.sample(Traitslist.tolist(), traitNums)

print("Start Date:", randomStartDate, "\nThe character is a", sex + ".", "\nFirstname:", Fname, "\nLastname:", Lname)

if culture == "Norse" or culture == "Swedish" or culture == "Norwegian" or culture == "Danish":
    north_germanic = True
    print("Culture Group: Northern Germanic", "\nCulture:", culture)
    
elif culture == "German" or culture == "Lombard" or culture == "Frankish" or culture == "Suebi":
    central_germanic = True
    print("Culture Group: Central Germanic", "\nCulture:", culture)
    
elif culture == "English" or culture == "Anglo_Saxon" or culture == "Saxon" or culture == "Frisian" or culture == "Dutch":
    western_germanic = True
    print("Culture Group: Western Germanic", "\nCulture:", culture)

elif culture == "French" or culture == "Norman" or culture == "Italian" or culture == "Occitan" or culture == "Roman" or culture == "Dalmatian" or culture == "Outremer" or culture == "Sardinian":
    latin = True
    print("Culture Group: Latin", "\nCulture:", culture)

elif culture == "Basque" or culture == "Castillan" or culture == "Catalan" or culture == "Portuguese" or culture == "Visigothic":
    iberian = True
    print("Culture Group: Iberian", "\nCulture:", culture)

elif culture == "Arberian" or culture == "Armenian" or culture == "Greek" or culture == "Alan" or culture == "Georgian" or culture == "Assyrian" or culture == "Coptic" or culture == "Gothic":
    byzantine = True
    print("Culture Group: Byzantine", "\nCulture:", culture)

elif culture == "Irish" or culture == "Scottish" or culture == "Pictish" or culture == "Welsh" or culture == "Breton":
    celtic = True
    print("Culture Group: Celtic", "\nCulture:", culture)

elif culture == "Finnish" or culture == "Sami" or culture == "Estonian" or culture == "Komi" or culture == "Khanty" or culture == "Nenets" or culture == "Mordvin" or culture == "Meshchera":
    finno_ugric = True
    print("Culture Group: Finno Ugric", "\nCulture:", culture)

elif culture == "Lettigallish" or culture == "Lithuanian" or culture == "Prussian":
    baltic = True
    print("Culture Group: Baltic", "\nCulture:", culture)

elif culture == "Turkish" or culture == "Pecheneg" or culture == "Cuman" or culture == "Khazar" or culture == "Bolghar" or culture == "Avar" or culture == "Karluk" or culture == "Kirghiz" or culture == "Uyghur" or culture == "Mongol" or culture == "Khitan" or culture == "Jurchen":
    altaic = True
    print("Culture Group: Altaic", "\nCulture:", culture)

elif culture == "Bedouin" or culture == "Berber" or culture == "Levantine" or culture == "Egyptian" or culture == "Andalusian":
    arabic = True
    print("Culture Group: Arabic", "\nCulture:", culture)

elif culture == "Russian" or culture == "Ilmenian" or culture == "Severian" or culture == "Volhynian":
    east_slavic = True
    print("Culture Group: East Slavic", "\nCulture:", culture)

elif culture == "Pommeranian" or culture == "Bohemian" or culture == "Polish" or culture == "Slovieni":
    west_slavic = True
    print("Culture Group: West Slavic", "\nCulture:", culture)

elif culture == "Croatian" or culture == "Serbian" or culture == "Romanian" or culture == "Bulgarian" or culture == "Bosnian" or culture == "Carantanian":
    south_slavic = True
    print("Culture Group: South Slavic", "\nCulture:", culture)

elif culture == "Hungarian":
    magyar = True
    print("Culture Group: Magyar", "\nCulture:", culture)

elif culture == "Persian" or culture == "Sogdian" or culture == "Tocharian" or culture == "Kurdish" or culture == "Saka":
    iranian = True
    print("Culture Group: Iranian", "\nCulture:", culture)

elif culture == "Ethiopian" or culture == "Somali" or culture == "Nubian" or culture == "Daju":
    east_african = True
    print("Culture Group: East African", "\nCulture:", culture)

elif culture == "Kanuri" or culture == "Hausa" or culture == "Zaghawa":
    central_african = True
    print("Culture Group: Central African", "\nCulture:", culture)

elif culture == "Mande" or culture == "Soninke" or culture == "Songhay":
    west_african = True
    print("Culture Group: West African", "\nCulture:", culture)

elif culture == "Nahua":
    mesoamerican = True
    print("Culture Group: Mesoamerican", "\nCulture:", culture)

elif culture == "Ashkenazi" or culture == "Sephardi":
    israelite = True
    print("Culture Group: Israelite", "\nCulture:", culture)

elif culture == "Bengali" or culture == "Oriya" or culture == "Assamese" or culture == "Hindustani" or culture == "Gujurati" or culture == "Panjabi" or culture == "Rajput" or culture == "Sindhi" or culture == "Marathi" or culture == "Sinhala" or culture == "Nepali":
    indo_aryan = True
    print("Culture Group: Indo Aryan", "\nCulture:", culture)

elif culture == "Tamil" or culture == "Telugu" or culture == "Kannada":
    dravidian = True
    print("Culture Group: Dravidian", "\nCulture:", culture)

elif culture == "Bodpa" or culture == "Tangut" or culture == "Zhangzhung" or culture == "Sumpa":
    tibetan = True
    print("Culture Group: Tibetan", "\nCulture:", culture)

elif culture == "Han":
    chinese = True
    print("Culture Group: Chinese", "\nCulture:", culture)

###########################################################################

if north_germanic == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 7:
        Rel = random.choice(info.Germanic.types)
    elif fate >= 9:
        Rel = random.choice(info.Christian_Catholic.types)
    else:
        Rel = info.religionList[religions]
        
elif north_germanic == True and randomStartDate == "936" or randomStartDate == "1066":
    if fate <= 7:
        Rel = random.choice(info.Christian_Catholic.types)
    elif fate >= 9:
        Rel = random.choice(info.Germanic.types)
    else:
        Rel = info.religionList[religions]

elif north_germanic == True and randomStartDate == "1337":
    if fate <= 8:
        Rel = random.choice(info.Christian_Catholic.types)
    elif fate == 9:
        Rel = random.choice(info.Germanic.types)
    else:
        Rel = info.religionList[religions]

###########################################################################

if central_germanic == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 7:
        Rel = random.choice(info.Germanic.types)
    elif fate >= 9:
        Rel = random.choice(info.Christian_Catholic.types)
    else:
        info.religionList[religions]
        
elif central_germanic == True and randomStartDate == "936" or randomStartDate == "1066":
    if fate <= 7:
        Rel = random.choice(info.Christian_Catholic.types)
    elif fate >= 9:
        Rel = random.choice(info.Germanic.types)
    else:
        info.religionList[religions]

elif central_germanic == True and randomStartDate == "1337":
    if fate <= 8:
        Rel = random.choice(info.Christian_Catholic.types)
    elif fate == 9:
        Rel = random.choice(info.Germanic.types)
    else:
        info.religionList[religions]

############################################################################

if western_germanic == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 7:
        Rel = random.choice(info.Christian_Catholic.types)
    elif fate == 8:
        Rel = random.choice(info.Germanic.types)
    elif fate == 9:
        Rel = random.choice(info.Christian_Heresy.types)
    else:
        info.religionList[religions]
        
elif western_germanic == True and randomStartDate == "936" or randomStartDate == "1066":
    if fate <= 8:
        Rel = random.choice(info.Christian_Catholic.types)
    elif fate >= 9:
        Rel = random.choice(info.Germanic.types)
    else:
        info.religionList[religions]

elif western_germanic == True and randomStartDate == "1337":
    if fate <= 9:
        Rel = random.choice(info.Christian_Catholic.types)
    else:
        info.religionList[religions]

############################################################################

if latin == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 8:
        Rel = random.choice(info.Christian_Catholic.types)
    elif fate == 9:
        Rel = random.choice(info.Hellenic.types)
    else:
        info.religionList[religions]
        
elif latin == True and randomStartDate == "936" or randomStartDate == "1066":
    if fate <= 8:
        Rel = random.choice(info.Christian_Catholic.types)
    elif fate == 9:
        Rel = random.choice(info.Christian_Heresy.types)
    else:
        info.religionList[religions]

elif latin == True and randomStartDate == "1337":
    if fate <= 9:
        Rel = random.choice(info.Christian_Catholic.types)
    else:
        info.religionList[religions]

############################################################################

if iberian == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 6:
        Rel = random.choice(info.Muslim_Sunni.types)
    elif fate == 10:
         info.religionList[religions]
    else:
        Rel = random.choice(info.Christian_Catholic.types)
        
elif iberian == True and randomStartDate == "936" or randomStartDate == "1066":
    if fate <= 4:
        Rel = random.choice(info.Muslim_Sunni.types)
    elif fate == 10:
         info.religionList[religions]
    else:
        Rel = random.choice(info.Christian_Catholic.types)

elif iberian == True and randomStartDate == "1337":
   if fate <= 1:
       Rel = random.choice(info.Muslim_Sunni.types)
   elif fate == 10:
       info.religionList[religions]
   else:
       Rel = random.choice(info.Christian_Catholic.types)

############################################################################

if byzantine == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 7:
        Rel = random.choice(info.Orthodox.types)
    elif fate <= 9 and fate > 7:
         Rel = random.choice(info.Mazdan.types)
    else:
        info.religionList[religions]
        
elif byzantine == True and randomStartDate == "936" or randomStartDate == "1066":
    if fate <= 8:
        Rel = random.choice(info.Orthodox.types)
    elif fate == 10:
         Rel = random.choice(info.Mazdan.types)
    else:
        Rel = random.choice(info.Christian_Catholic.types)

elif byzantine == True and randomStartDate == "1337":
    if fate <= 8:
        Rel = random.choice(info.Orthodox.types)
    elif fate == 10:
         Rel = random.choice(info.Mazdan.types)
    else:
        Rel = random.choice(info.Christian_Catholic.types)

############################################################################

if celtic == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 8:
        Rel = random.choice(info.Christian_Catholic.types)
    elif fate == 9:
        Rel = random.choice(info.Christian_Heresy.types)
    else:
        info.religionList[religions]
        
elif celtic == True and randomStartDate == "936" or randomStartDate == "1066":
    if fate <= 8:
        Rel = random.choice(info.Christian_Catholic.types)
    elif fate == 9:
        Rel = random.choice(info.Christian_Heresy.types)
    else:
        info.religionList[religions]

elif celtic == True and randomStartDate == "1337":
    if fate <= 9:
        Rel = random.choice(info.Christian_Catholic.types)
    else:
        info.religionList[religions]

############################################################################

if finno_ugric == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 9:
        Rel = random.choice(info.Suomemsko.types)
    else:
        info.religionList[religions]
        
elif finno_ugric == True and randomStartDate == "936" or randomStartDate == "1066":
    if fate <= 9:
        Rel = random.choice(info.Suomemsko.types)
    else:
        info.religionList[religions]

elif finno_ugric == True and randomStartDate == "1337":
    if fate <= 8:
        Rel = random.choice(info.Suomemsko.types)
    elif fate == 9:
        Rel = random.choice(info.Christian_Catholic.types)
    else:
        info.religionList[religions]

############################################################################

if baltic == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 9:
        Rel = random.choice(info.Romuva.types)
    else:
        info.religionList[religions]
        
elif baltic == True and randomStartDate == "936" or randomStartDate == "1066":
    if fate <= 9:
        Rel = random.choice(info.Romuva.types)
    else:
        info.religionList[religions]

elif baltic == True and randomStartDate == "1337":
    if fate <= 8:
        Rel = random.choice(info.Romuva.types)
    elif fate == 9:
        Rel = random.choice(info.Christian_Catholic.types)
    else:
        info.religionList[religions]

############################################################################

if altaic == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 7:
        Rel = random.choice(info.Tengri.types)
    elif fate == 8:
        Rel = random.choice(info.Jewish.types)
    elif fate == 9:
        Rel = random.choice(info.Manichean.types)
    else:
        info.religionList[religions]
        
elif altaic == True and randomStartDate == "936" or randomStartDate == "1066":
    if fate <= 4:
        Rel = random.choice(info.Tengri.types)
    elif fate == 5:
        Rel = random.choice(info.Jewish.types)
    elif fate == 6:
        Rel = random.choice(info.Manichean.types)
    elif fate == 7:
        Rel = random.choice(info.Muslim_Sunni.types)
    elif fate == 8 or fate == 9:
        Rel = random.choice(info.Buddhist.types)
    else:
        info.religionList[religions]

elif altaic == True and randomStartDate == "1337":
    if fate <= 5:
        Rel = random.choice(info.Muslim_Sunni.types)
    elif fate >= 6 and fate <= 8:
        Rel = random.choice(info.Tengri.types)
    elif fate == 9:
        Rel = random.choice(info.Manichean.types)
    else:
        info.religionList[religions]

############################################################################

if arabic == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 7:
        Rel = random.choice(info.Muslim_Sunni.types)
    elif fate == 8:
        Rel = random.choice(info.Ibadi.types)
    elif fate == 9:
        Rel = random.choice(info.Muslim_Shia.types)
    else:
        info.religionList[religions]
        
elif arabic == True and randomStartDate == "936" or randomStartDate == "1066":
    if fate <= 4:
        Rel = random.choice(info.Muslim_Sunni.types)
    elif fate >= 5 or fate <= 7:
        Rel = random.choice(info.Muslim_Shia.types)
    elif fate == 8:
        Rel = random.choice(info.Ibadi.types)
    elif fate == 9:
        Rel = random.choice(info.Qarmatian.types)
    else:
        info.religionList[religions]

elif arabic == True and randomStartDate == "1337":
    if fate <= 7:
        Rel = random.choice(info.Muslim_Sunni.types)
    elif fate == 8:
        Rel = random.choice(info.Muslim_Shia.types)
    elif fate == 9:
        Rel = random.choice(info.Ibadi.types)
    else:
        info.religionList[religions]

############################################################################

if east_slavic == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 9:
        Rel = random.choice(info.Slavic.types)
    else:
        info.religionList[religions]
        
elif east_slavic == True and randomStartDate == "936" or randomStartDate == "1066":
    if fate <= 4:
        Rel = random.choice(info.Slavic.types)
    elif fate >= 5 or fate <= 9:
        Rel = random.choice(info.Orthodox.types)
    else:
        info.religionList[religions]

elif east_slavic == True and randomStartDate == "1337":
    if fate <= 9:
        Rel = random.choice(info.Orthodox.types)
    else:
        info.religionList[religions]

############################################################################

if west_slavic == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 9:
        Rel = random.choice(info.Slavic.types)
    else:
        info.religionList[religions]
        
elif west_slavic == True and randomStartDate == "936" or randomStartDate == "1066":
    if fate <= 5:
        Rel = random.choice(info.Slavic.types)
    elif fate >= 6 or fate <= 9:
        Rel = random.choice(info.Christian_Catholic.types)
    else:
        info.religionList[religions]

elif west_slavic == True and randomStartDate == "1337":
    if fate <= 9:
        Rel = random.choice(info.Christian_Catholic.types)
    else:
        info.religionList[religions]

############################################################################

if south_slavic == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 3:
        Rel = random.choice(info.Slavic.types)
    elif fate >= 4 or fate <= 6:
        Rel = random.choice(info.Tengri.types)
    elif fate == 7 or fate == 8:
        Rel = random.choice(info.Orthodox.types)
    elif fate == 9:
        Rel = random.choice(info.Christian_Catholic.types)
    else:
        info.religionList[religions]
        
elif south_slavic == True and randomStartDate == "936" or randomStartDate == "1066":
    if fate <= 7:
        Rel = random.choice(info.Orthodox.types)
    elif fate == 8 or fate == 9:
        Rel = random.choice(info.Christian_Catholic.types)
    else:
        info.religionList[religions]

elif south_slavic == True and randomStartDate == "1337":
    if fate <= 8:
        Rel = random.choice(info.Orthodox.types)
    elif fate == 9:
        Rel = random.choice(info.Christian_Catholic.types)
    else:
        info.religionList[religions]

############################################################################

if magyar == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 9:
        Rel = random.choice(info.Tengri.types)
    else:
        info.religionList[religions]
        
elif magyar == True and randomStartDate == "936" or randomStartDate == "1066":
    if fate <= 5:
        Rel = random.choice(info.Tengri.types)
    elif fate > 5 and fate <= 9:
        Rel = random.choice(info.Christian_Catholic.types)
    else:
        info.religionList[religions]

elif magyar == True and randomStartDate == "1337":
    if fate <= 9:
        Rel = random.choice(info.Christian_Catholic.types)
    else:
        info.religionList[religions]

###########################################################################

if iranian == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 4:
        Rel = random.choice(info.Muslim_Sunni.types)
    elif fate > 4 and fate <= 8:
        Rel = random.choice(info.Buddhist.types)
    elif fate == 9:
        Rel = random.choice(info.Zunist.types)
    else:
        info.religionList[religions]
        
elif iranian == True and randomStartDate == "936" or randomStartDate == "1066":
    if fate <= 4:
        Rel = random.choice(info.Muslim_Sunni.types)
    elif fate > 4 and fate <= 7:
        Rel = random.choice(info.Muslim_Shia.types)
    elif fate == 8:
        Rel = random.choice(info.Buddhist.types)
    elif fate == 9:
        Rel = random.choice(info.Hindu.types)
    else:
        info.religionList[religions]

elif iranian == True and randomStartDate == "1337":
    if fate <= 9:
        Rel = random.choice(info.Muslim_Sunni.types)
    else:
        info.religionList[religions]

###########################################################################

if east_african == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 7:
        Rel = random.choice(info.Miaphysite.types)
    elif fate == 8:
        Rel = random.choice(info.Jewish.types)
    elif fate == 9:
        Rel = random.choice(info.Muslim_Sunni.types)
    else:
        info.religionList[religions]
        
elif east_african == True and randomStartDate == "936" or randomStartDate == "1066":
  if fate <= 6:
      Rel = random.choice(info.Miaphysite.types)
  elif fate == 7:
      Rel = random.choice(info.Jewish.types)
  elif fate > 7 and fate <= 9:
      Rel = random.choice(info.Muslim_Sunni.types)
  else:
      info.religionList[religions]

elif east_african == True and randomStartDate == "1337":
    if fate <= 5:
        Rel = random.choice(info.Miaphysite.types)
    elif fate == 6:
        Rel = random.choice(info.Jewish.types)
    elif fate > 6 and fate <= 9:
        Rel = random.choice(info.Muslim_Sunni.types)
    else:
        info.religionList[religions]

###########################################################################

if central_african == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 9:
        Rel = random.choice(info.African.types)
    else:
        info.religionList[religions]
        
elif central_african == True and randomStartDate == "936" or randomStartDate == "1066":
  if fate <= 8:
      Rel = random.choice(info.African.types)
  elif fate == 9:
      Rel = random.choice(info.Muslim_Sunni.types)
  else:
      info.religionList[religions]

elif central_african == True and randomStartDate == "1337":
    if fate <= 7:
        Rel = random.choice(info.African.types)
    elif fate == 8 or fate == 9:
        Rel = random.choice(info.Muslim_Sunni.types)
    else:
        info.religionList[religions]

###########################################################################

if west_african == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 9:
        Rel = random.choice(info.African.types)
    else:
        info.religionList[religions]
        
elif west_african == True and randomStartDate == "936" or randomStartDate == "1066":
  if fate <= 7:
      Rel = random.choice(info.African.types)
  elif fate == 8 or fate == 9:
      Rel = random.choice(info.Muslim_Sunni.types)
  else:
      info.religionList[religions]

elif west_african == True and randomStartDate == "1337":
    if fate == 1:
        Rel = random.choice(info.African.types)
    elif fate > 1 and fate <= 9:
        Rel = random.choice(info.Muslim_Sunni.types)
    else:
        info.religionList[religions]

###########################################################################

if mesoamerican == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 9:
        Rel = random.choice(info.Aztec.types)
    else:
        info.religionList[religions]
        
elif mesoamerican == True and randomStartDate == "936" or randomStartDate == "1066":
  if fate <= 9:
      Rel = random.choice(info.Aztec.types)
  else:
      info.religionList[religions]

elif mesoamerican == True and randomStartDate == "1337":
    if fate <= 9:
        Rel = random.choice(info.Aztec.types)
    else:
        info.religionList[religions]

###########################################################################

if israelite == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 9:
        Rel = random.choice(info.Jewish_All.types)
    else:
        info.religionList[religions]
        
elif israelite == True and randomStartDate == "936" or randomStartDate == "1066":
  if fate <= 9:
      Rel = random.choice(info.Jewish_All.types)
  else:
      info.religionList[religions]

elif israelite == True and randomStartDate == "1337":
    if fate <= 9:
        Rel = random.choice(info.Jewish_All.types)
    else:
        info.religionList[religions]

###########################################################################

if indo_aryan == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 7:
        Rel = random.choice(info.Hindu.types)
    elif fate == 8 or fate == 9:
        Rel = random.choice(info.Buddhist.types)
    else:
        info.religionList[religions]
        
elif indo_aryan == True and randomStartDate == "936" or randomStartDate == "1066":
  if fate <= 8:
      Rel = random.choice(info.Hindu.types)
  elif fate == 9:
      Rel = random.choice(info.Buddhist.types)
  else:
      info.religionList[religions]

elif indo_aryan == True and randomStartDate == "1337":
    if fate <= 7:
        Rel = random.choice(info.Hindu.types)
    elif fate == 8 or fate == 9:
        Rel = random.choice(info.Muslim_Sunni.types)
    else:
        info.religionList[religions]

###########################################################################

if dravidian == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 6:
        Rel = random.choice(info.Hindu.types)
    elif fate == 7 or fate == 8:
        Rel = random.choice(info.Jain.types)
    elif fate == 9:
        Rel = random.choice(info.Buddhist.types)
    else:
        info.religionList[religions]
        
elif dravidian == True and randomStartDate == "936" or randomStartDate == "1066":
  if fate <= 4:
      Rel = random.choice(info.Hindu.types)
  elif fate > 4 and fate <= 8:
      Rel = random.choice(info.Jain.types)
  elif fate == 9:
      Rel = random.choice(info.Buddhist.types)
  else:
      info.religionList[religions]

elif dravidian == True and randomStartDate == "1337":
    if fate <= 9:
        Rel = random.choice(info.Hindu.types)
    else:
        info.religionList[religions]

###########################################################################

if tibetan == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 5:
        Rel = random.choice(info.Buddhist.types)
    elif fate > 5 or fate <= 9:
        Rel = random.choice(info.Bon.types)
    else:
        info.religionList[religions]
        
elif tibetan == True and randomStartDate == "936" or randomStartDate == "1066":
  if fate <= 5:
      Rel = random.choice(info.Buddhist.types)
  elif fate > 5 and fate <= 8:
      Rel = random.choice(info.Bon.types)
  elif fate == 9:
      Rel = random.choice(info.Taoist.types)
  else:
      info.religionList[religions]

elif tibetan == True and randomStartDate == "1337":
    if fate <= 9:
        Rel = random.choice(info.Buddhist.types)
    else:
        info.religionList[religions]

###########################################################################

if chinese == True and randomStartDate == "769" or randomStartDate == "867":
    if fate <= 4:
        Rel = random.choice(info.Buddhist.types)
    elif fate > 4 and fate <= 9:
        Rel = random.choice(info.Taoist.types)
    else:
        info.religionList[religions]
        
elif chinese == True and randomStartDate == "936" or randomStartDate == "1066":
    if fate <= 4:
        Rel = random.choice(info.Buddhist.types)
    elif fate > 4 and fate <= 9:
        Rel = random.choice(info.Taoist.types)
    else:
        info.religionList[religions]

elif chinese == True and randomStartDate == "1337":
    
    if fate <= 4:
        Rel = random.choice(info.Buddhist.types)
    elif fate > 4 and fate <= 9:
        Rel = random.choice(info.Taoist.types)
    else:
        info.religionList[religions]
        
################################################################################

print("Religion:", Rel, "\nEducation Trait:", edu_traits)

"""print("Traits: ", end="")
for x in traitNums:
    for y in info.trait_exclusions.get(theTraits, []):
        if info.trait_exclusions in info.char_traits:
            info.char_traits.remove(info.trait_exclusions)

    print(theTraits, ", ", end="")"""

print("Traits: ")

traits = []
for trait in random.sample(info.traitsList, random.randint(0, 5)):  # Pick 0..5 traits.
    if trait in info.oppositePicks:  # One of the opposing trait pairs - pick one.
        trait = random.choice(info.oppositePicks[trait])
                                       
    traits.append(trait)
    print(trait + ",")


if fate <= 3:
    print("\nHealth Traits: ", healthTraits)
if moreFate <= 3:
    print("\nSevere Health Traits: ", severeHealthTraits)
    print("Physical Appearance:", physique)
else:
    print("\nPhysical Appearance:", physique)


# DONE: Maak seker dat dit se watse culture class die mens van is etc. dutch or swedish

# TODO: Maak seker die physical appearance verander based on die traits van die character
