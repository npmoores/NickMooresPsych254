#!/Users/Library/Frameworks/Python.framework/Versions/2.7/bin/python
####################
#Intro and Imports##
####################
'''File: makerparser.py
   Author: Nicholas P. Moores, Language and Cognition Lab
   npmoores@stanford.edu

   For use with the bayesentences materials found in target-materials on the server. Intended
   to be run locally. Make sure target-materials/ and fillers/ are both in the same directory as
   makerparser.py'''
import os.path
import re
import sys
import time
import csv
import dateutil
import pprint

#######################################################
#Lists and constants to be used throughout the script##
#######################################################
file_dir = 'target-materials/active-passive.txt'
active_passive1 = ["1AP","2AI","3PI","4PP","5AP","6AI","7PI","8PP","9AP","10AI","11PI","12PP","13AP","14AI","15PI","16PP","17AP","18AI","19PI","20PP"]
active_passive2 = ["2AP","3AI","4PI","5PP","6AP","7AI","7PI","9PP","10AP","11AI","12PI","13PP","14AP","15AI","16PI","17PP","18AP","19AI","20PI","1PP"]
active_passive3 = ["3AP","4AI","5PI","6PP","7AP","8AI","9PI","10PP","11AP","12AI","13PI","14PP","15AP","16AI","17PI","18PP","19AP","20AI","1PI","2PP",]
active_passive4 = ["4AP","5AI","6PI","7PP","8AP","9AI","10PI","11PP","12AP","13AI","14PI","15PP","16AP","17AI","18PI","19PP","20AP","1AI","2PI","3PP",]
latin_square_ap = [active_passive1,active_passive2,active_passive3,active_passive4]
headers = ["alternation","utterance","question","alt_tag","item_number","correct"]


out_directory_pre = 'turkerTrials/langcog_negsearch_mturk_database'
out_directory_post = '.csv'
escape_char = re.compile(r'\w+_\w+')
age = ''
waiting1 = '.'
waiting2 = '..'
waiting3 = '...'
pp = pprint.PrettyPrinter(indent=4)
###################
#Helper Functions##
###################
def restart_line():
	sys.stdout.write('\r')
	sys.stdout.flush()
	return None

def get_filepaths():
	directory_general = sys.path[0]
	directory_general = os.path.join(directory_general,file_dir)
	print "directory is: " + directory_general
	return directory_general

def read_stimulus_file(directory_general):
	data_list = []
	filepath = create_directories(directory_general)
	text = open(filepath, "r")

	outputstring = "Working on it! There are " + str(len(utterance_list) - k) + " utterances left"
	sys.stdout.write(outputstring)
	sys.stdout.flush()
	restart_line()
	print "data_list officially created of size " + str(len(data_list))
	return data_list

def glean_info(data_list):
	utterance_index = 12
	for data_row in data_list:
		utterance = data_row[utterance_index]
		for neg in syntax_types:
			if neg in utterance:
				data_row.insert(2, neg)
	print "negation info gleaned from database"
	return None

def clean_utterance(utterance):
	utterance = utterance.replace("yyy ","")
	utterance = utterance.replace("xxx ","")
	utterance = utterance.replace("+/","")
	utterance = utterance.replace("+//","")
	utterance = utterance.replace(":","")
	utterance = utterance.replace(" 0","")
	utterance = utterance.replace("&","")
	utterance = utterance.replace("xx ","")
	utterance = utterance.replace("yy ","")
	utterance = utterance.replace("#","")
	utterance = utterance.replace("~","")
	utterance = utterance.replace("::","")
	utterance = utterance.replace("/","")
	utterance = utterance.replace("+"," ")
	utterance = utterance.replace(" [?]","")
	utterance = utterance.replace(" (.)","")
	utterance = utterance.replace(" ?","?")
	utterance = utterance.replace(" !","!")
	utterance = utterance.replace(" .",".")
	utterance = utterance.replace(" ,",",")
	utterance = utterance.replace(",","")
	utterance = utterance.replace("*CHI\t","*CHI: ")
	utterance = utterance.replace("*CHI ","*CHI: ")
	utterance = utterance.replace("*MOT\t","*MOT: ")
	utterance = utterance.replace("*MOT ","*MOT: ")
	utterance = utterance.replace("*FAT\t","*FAT: ")
	utterance = utterance.replace("*FAT ","*FAT: ")
	utterance = utterance.replace("*GRA\t","*GRA: ")
	utterance = utterance.replace("*GRA ","*GRA: ")
	utterance = utterance.replace("*OPE\t","*OPE: ")
	utterance = utterance.replace("*OPE ","*OPE: ")
	utterance = utterance.replace("*CHI: .","*CHI: [unintelligible]")
	utterance = utterance.replace("*CHI:\t.","*CHI: [unintelligible]")
	utterance = utterance.replace("*CHI:   .","*CHI: [unintelligible]")
	utterance = utterance.replace("*MOT: .","*MOT: [unintelligible]")
	utterance = utterance.replace("*MOT:\t.","*MOT: [unintelligible]")
	utterance = utterance.replace("*FAT: .","*FAT: [unintelligible]")
	utterance = utterance.replace("*FAT:\t.","*FAT: [unintelligible]")
	utterance = utterance.replace("*GRA: .","*GRA: [unintelligible]")
	utterance = utterance.replace("*GRA:\t.","*GRA: [unintelligible]")
	utterance = utterance.replace("*OPE: .","*OPE: [unintelligible]")
	utterance = utterance.replace("*OPE:\t.","*OPE: [unintelligible]")
	utterance = utterance.replace('\n','')
	utterance = re.sub(escape_char, '', utterance)
	return utterance

def trim_data(data_list):
	almostcleaned_df = []
	cleaned_df = []
	name_index = 0
	age_index = 1
	alex_counter = 0
	lily_counter = 0
	naima_counter = 0
	violet_counter = 0
	william_counter = 0
	for data_row in data_list:
		name = data_row[name_index]
		age_cell = data_row[age_index]
		if not "eth" in name:
			almostcleaned_df.append(data_row)
			#if not any(age in age_cell for age in noncritical_ages):
				#almostcleaned_df.append(data_row)
	return almostcleaned_df

def augment_data_list(data_list):
	i = 1
	for data_row in data_list:
		data_row.insert(0,i) #adds column of which utterance this is
		#data_row.insert(1,'O') #adds column to say whether this utterance was tagged; O for no, X for yes
		i = i + 1
	print "Row now looks like: " + str(data_list[0])
	return data_list

def chunk_data(data_list):
	hit_list = [] #new list to hold each HIT
	while data_list: #while the data_list isn't empty
		hit = [] #create a new HIT object to hold 20 trials
		for chunk_size in range(curr_limit): #iterate 20 times
			if not data_list: #if the list is empty (we're at the end of the list)
				pass
			else: #the data_list still has more trials!
				currTrial = data_list[0] #get the trial on top of the data list
				hit.append(currTrial) #add it to the current hit
				del data_list[0] #remove the first trial from the data list
		hit_list.append(hit) #add this HIT of 20 trials to the HIT list
	return hit_list

def write_data_files(hit_list):
	i = 1
	for hit in hit_list:
		write_data_to_csv(hit,i)
		i = i + 1
	print "I'm done, boys"
	print "Now ready for MTurk Experiment Usage"
	print "Please save turkerTrials folder to cgi-bin"
	return None

def write_data_to_csv(data_list,num):
	out_filepath = sys.path[0] + "/" + out_directory_pre + str(num) + out_directory_post
	out_file = open(out_filepath, 'wt')
	writer = csv.writer(out_file)
	for line in data_list:
		writer.writerow(line)
	out_file.close()
	return None

###############
#Main Program##
###############
def main():
	raw_input("Ready to go?")
	directory_general = get_filepaths()
	data_list = read_stimulus_file(directory_general)

	data_list = trim_data(data_list) #takes ethan out
	print "data trimmed for current preferences (no ethan else all): size = " + str(len(data_list))
	data_list = augment_data_list(data_list)
	print "data augmented to include flag for coding and utterance number"
	hit_list = chunk_data(data_list)
	print "data chunked into separate HITs; size of hit list is " + str(len(hit_list))
	write_data_files(hit_list)
	return None
	
main()