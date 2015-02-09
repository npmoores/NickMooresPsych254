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
syntax_types = [" no ","\tno "," no: ","\tno: "," oh+no ","\toh+no "," not ","\tnot ","n't "]
neg_categories = ["ASSERTIVE","DIRECTIVE","OTHER/UNCLEAR","REPEAT"]
category_abbreviations = ["A","D","X","R"]
noncritical_ages = ["1;1","1;2","1;3","1;4","1;5","1;6","1;7","1;8","1;9","1;10","1;11","1;12","2;0","2;1","2;2","2;3","2;4","2;5"]
labels = neg_categories + category_abbreviations
indexes = ["line.number","is.tagged","filename","age","before1","before2","before3","before4","before5","before6","before7","before8","before9","before10","utterance","after1","after2","after3"]
curr_limit = 20
child_marker = '*CHI:'
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
	directory_general = sys.path[0] + "/" + "Providence/"
	print "directory is: " + directory_general
	return directory_general

def create_directories(directory_general):
	folder_list = []
	for folder in os.listdir(directory_general):
		if ('metadata' in folder):
			pass
		elif ('.DS_Store' in folder):
			pass
		else:
			filepath = os.path.join(directory_general, folder)
			folder_list.append(filepath)
	print "create_directories success!"
	return folder_list

def read_chat_files(directory_general):
	folder_list = create_directories(directory_general)
	data_list = []
	utterance_list = []
	speech_marker = '*'
	for folder in folder_list: #iterates through the children's folder
		for filename in os.listdir(folder): #iterates through each chat file in the folder
			filepath = os.path.join(folder, filename)
			if filepath.endswith(".cha"): #checks it's a chat file
				text = open(filepath, "r") #opens the chat file
				j = 0
				age_utterance_pair = []
				for index in range(5):
					next_line = text.next()
				age = re.search('providence\|CHI\|(.+?)\|', next_line).group(1)
				for each_line in text: #iterates through each line in the file
					if speech_marker in each_line: #exclude phonetic lines
						j_string = str(j)
						line = str(filename + " " + age + " " + j_string + " " + each_line)
						utterance_list.append(line) #adds the line to our list of data
						j = j+1
				text.close() #closes the current chat file
	print "size of utterance list is " + str(len(utterance_list))
	k = 0
	for utterance in utterance_list: #iterates through our list of every line in the files
		if any(neg in utterance for neg in syntax_types):
			if child_marker in utterance:
				utterance_index = utterance_list.index(utterance)
				utterance = utterance.strip(' ')
				which_file = utterance.split(' ',2)[0]
				child_age = utterance.split(' ',2)[1]
				utterance = utterance.split(' ',2)[2]
				try:
					before_line_1 = utterance_list[utterance_index - 1].strip(' ').split(' ',2)[2] #line at j - 1
					before_line_2 = utterance_list[utterance_index - 2].strip(' ').split(' ',2)[2] #line at j - 1
					before_line_3 = utterance_list[utterance_index - 3].strip(' ').split(' ',2)[2] #line at j - 1
					before_line_4 = utterance_list[utterance_index - 4].strip(' ').split(' ',2)[2] #line at j - 1
					before_line_5 = utterance_list[utterance_index - 5].strip(' ').split(' ',2)[2] #line at j - 5
					before_line_6 = utterance_list[utterance_index - 6].strip(' ').split(' ',2)[2] #line at j - 6
					before_line_7 = utterance_list[utterance_index - 7].strip(' ').split(' ',2)[2] #line at j - 7
					before_line_8 = utterance_list[utterance_index - 8].strip(' ').split(' ',2)[2] #line at j - 8
					before_line_9 = utterance_list[utterance_index - 9].strip(' ').split(' ',2)[2] #line at j - 9
					before_line_10 = utterance_list[utterance_index - 10].strip(' ').split(' ',2)[2] #line at j - 10
				except IndexError: #if there is no line before, doesn't go looking for context
					before_line_1 = utterance_list[utterance_index].strip(' ').split(' ',2)[2]
					before_line_2 = utterance_list[utterance_index].strip(' ').split(' ',2)[2]
					before_line_3 = utterance_list[utterance_index].strip(' ').split(' ',2)[2]
					before_line_4 = utterance_list[utterance_index].strip(' ').split(' ',2)[2]
					before_line_5 = utterance_list[utterance_index].strip(' ').split(' ',2)[2]
					before_line_6 = utterance_list[utterance_index].strip(' ').split(' ',2)[2]
					before_line_7 = utterance_list[utterance_index].strip(' ').split(' ',2)[2]
					before_line_8 = utterance_list[utterance_index].strip(' ').split(' ',2)[2]
					before_line_9 = utterance_list[utterance_index].strip(' ').split(' ',2)[2]
					before_line_10 = utterance_list[utterance_index].strip(' ').split(' ',2)[2]
				instance = [which_file, child_age, before_line_10, before_line_9, before_line_8, before_line_7, before_line_6]
				instance.extend([before_line_5, before_line_4, before_line_3, before_line_2, before_line_1, utterance])
				try:
					after_line_1 = utterance_list[utterance_index + 1].strip(' ').split(' ',2)[2] #line at j + 1
					after_line_2 = utterance_list[utterance_index + 2].strip(' ').split(' ',2)[2] #line at j + 2
					after_line_3 = utterance_list[utterance_index + 3].strip(' ').split(' ',2)[2] #line at j + 3
				except IndexError: #if there is no line after, doesn't go looking for context
					after_line_1 = utterance_list[utterance_index].strip(' ').split(' ',2)[2]
					after_line_2 = utterance_list[utterance_index].strip(' ').split(' ',2)[2]
					after_line_3 = utterance_list[utterance_index].strip(' ').split(' ',2)[2]
				instance.extend([after_line_1, after_line_2, after_line_3])
				instance = [clean_utterance(item) for item in instance]
				data_list.append(instance)
		k = k + 1
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
	'''
	for data_row in almostcleaned_df:
		name = data_row[name_index]
		if "ale" in name:
			if alex_counter < curr_limit:
				cleaned_df.append(data_row)
			alex_counter = alex_counter + 1
		if "lil" in name:
			if lily_counter < curr_limit:
				cleaned_df.append(data_row)
			lily_counter = lily_counter + 1
		if "nai" in name:
			if naima_counter < curr_limit:
				cleaned_df.append(data_row)
			naima_counter = naima_counter + 1
		if "vio" in name:
			if violet_counter < curr_limit:
				cleaned_df.append(data_row)
			violet_counter = violet_counter + 1
		if "wil" in name:
			if william_counter < curr_limit:
				cleaned_df.append(data_row)
			william_counter = william_counter + 1'''
	print "data trimmed for current preferences"
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
	data_list = read_chat_files(directory_general)
	#glean_info(data_list) only if you want negations put out separately
	data_list = trim_data(data_list) #takes ethan out
	print "data trimmed for current preferences (no ethan else all): size = " + str(len(data_list))
	data_list = augment_data_list(data_list)
	print "data augmented to include flag for coding and utterance number"
	hit_list = chunk_data(data_list)
	print "data chunked into separate HITs; size of hit list is " + str(len(hit_list))
	write_data_files(hit_list)
	return None
	
main()