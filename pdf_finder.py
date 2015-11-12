#! python3 
# pdf_finder.py - Locates pdf files within a given folder 
# then copies these files over to another folder, while creating a text file outlining
# each files original location

import os, shutil

def pdf_finder(folder):
# TODO: Make storage directory
	pdf_folder = os.makedirs(os.getcwd() + '/' +'PDFs')
	pdf_folder_name = os.getcwd()+ '/' + 'PDFs'

# TODO: Find the PDF files in the given folder
	for foldername, subfolders, filenames in os.walk(folder):
		print('Searching for pdfs in {0}...').format(foldername)
	
		for filename in filenames:
			if filename.endswith('.pdf'):
				print('We\'ve found the following pdf: %s' % filename)
				pdflocation = os.path.join(folder, filename)
				print('In the following location %s' % pdflocation)
				
				
				shutil.copy(pdflocation, pdf_folder_name)		
				print('File has been copied to %s' % pdf_folder_name)
				
				# create a pdf locator txt file that tells the user where all the pdfs 
				# were copied from
				pdf_history = open(folder + '/' + 'NewPDFfolder', 'a')
				pdf_history.write("""We found the following pdf: \t %s\nIn the following location: \t%s\n\n""" % (filename, pdflocation))
		
		pdf_history.close()
		
pdf_finder('/Users/Pesanteur/Downloads')