import pandas as pd

import glob

def load_found_excel_files ():
	return glob.glob("excel/found/*")

def load_made_excel_files ():
	return glob.glob("excel/made/*")


def read_found():
	files =load_found_excel_files()
	list_for_emna=[]
	my_year=2015
	for f in files :
		print ("filename")
		print (f)
		df=pd.read_excel(f)
		print ("number of rows: ",df.shape[0] )

		etablissements=df["Etablissement d’accueil du PFE"].tolist()
		emails=df["Email du tuteur de stage à l'établissement"].tolist()
		
		df_to_export = df[["Email du tuteur de stage à l'établissement","Etablissement d’accueil du PFE"]]
		print (df_to_export)
		my_filename=str(my_year)+".xlsx"
		my_year+=1
		df_to_export.to_excel(my_filename)
		for i in range(1,len(etablissements)):
			unit={}
			unit["etablissement"]=etablissements[i]
			unit["email"]=emails[i]
			
			list_for_emna.append(unit)
	return list_for_emna

def read_made():
	files = load_made_excel_files()
	list_for_emna=[]
	for f in files :
		df=pd.read_excel(f)
	
		etablissements=df["Nom de l'entreprise"].tolist()
		emails=df["Mail"].tolist()
		
	
		for i in range(1,len(etablissements)):
			unit={}
			unit["etablissement"]=etablissements[i].rstrip('\xa0')
			print (emails[i])
			unit["email"]=emails[i].rstrip('\xa0')
			
			list_for_emna.append(unit)
		return list_for_emna

def read_english():
	filename="English/Contacts.xlsx"
	english_list=[]
	df=pd.read_excel(filename)
	
	etablissements=df["Nom de l'entreprise"].tolist()
	emails=df["Mail"].tolist()
	
	
	for i in range(1,len(etablissements)):
		unit={}
		unit["etablissement"]=etablissements[i].strip().strip('\xa0')
		unit["email"]=emails[i].strip().strip('\xa0')
		
		english_list.append(unit)
	return english_list

def read_french():
	filename="./fghons/fghons.xlsx"
	french_list=[]
	df=pd.read_excel(filename)
	
	etablissements=df["Nom de l'entreprise"].tolist()
	emails=df["Mail"].tolist()
	
	
	for i in range(1,len(etablissements)):
		unit={}
		unit["etablissement"]=etablissements[i].strip().strip('\xa0')
		unit["email"]=emails[i].strip().strip('\xa0')
		
		french_list.append(unit)
	return french_list

print(read_french())