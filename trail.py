import json , sys , hashlib , os , time , marshal, getpass 


reload (sys)
sys . setdefaultencoding ( 'utf8' )

def banner():
	print '''

		         ___                       
		       _(((,|    What's DNA??         
		      /  _-\\                       
		     / C o\o \                     
		   _/_    __\ \     __ __     __ __     __ __     __
		  /   \ \___/  )   /--X--\   /--X--\   /--X--\   /--
		  |    |\_|\  /   /--/ \--\ /--/ \--\ /--/ \--\ /--/
		  |    |#  #|/          \__X__/   \__X__/   \__X__/ 
		  (   /     | 
		   |  |#  # | 
		   |  |    #|                      
		   |  | #___n_,_                  
		,-/   7-' .     `\                 
		`-\...\-_   -  o /                 
		   |#  # `---U--'                  
		   `-v-^-'\/                       
		     \  |_|_ Wny                  
		     (___mnnm

'''	
banner()

print"{ --------------------------------------------------------- }".center(100)	
print""
print"{ BIOINFORMATICS LAZYSCRIPT}".center(100)
print""
print"{ --------------------------------------------------------- }".center(100)	
print""
print"{ Coded By: Mohammed Banyamer }".center(100)
print""
print"{ --------------------------------------------------------- }".center(100)	
print""
print""

def program_info():
	print '''

O    O
  \\ /
    P
   / \
--O   O            NH2 ..... O      N
     /            /           \\   / \\        |
    <         ----             ----   \\    ---+
     \       //  \\           /   \\   |   /   |
      +--O  <      N ...... HN      >--N--<    |
      |   \  \    /           \    /       \   |
      |    >--N---             ===N         O--+
      |   /      \\           /                 \
      +---         O ..... H2N                   >
      |                                         /
                                               O   O--
                                                \ /
                                                 P
                                                / \\
                { Mohammed Banyamer }          O    O
 ------------------------------------------------------
    Author     Mohammed Banyamer
    Name       BIO-JO 'BIOINFORMATICS LAZYSCRIPT'
    CodeName   NASHMI01
    version    Trial version
    Date       16/12/2019 09:35:12
    Team       N4SHMI-JO
    Email      Mohammed.banyamer@firstinfosec.com
    Instagram  @mbani3amer
    Phone      +962781008061/+96894849593 
     
* CONTACT ME IF YOU FIND ERRORS OR TO GIVE ME FEEDBACK 

'''
def Fasta():
	print '''
 
  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || |      __      | || |    _______   | || |  _________   | || |      __      | |
| | |_   ___  |  | || |     /  \     | || |   /  ___  |  | || | |  _   _  |  | || |     /  \     | |
| |   | |_  \_|  | || |    / /\ \    | || |  |  (__ \_|  | || | |_/ | | \_|  | || |    / /\ \    | |
| |   |  _|      | || |   / ____ \   | || |   '.___`-.   | || |     | |      | || |   / ____ \   | |
| |  _| |_       | || | _/ /    \ \_ | || |  |`\____) |  | || |    _| |_     | || | _/ /    \ \_ | |
| | |_____|      | || ||____|  |____|| || |  |_______.'  | || |   |_____|    | || ||____|  |____|| |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

'''	
	print"{ ----------------------------------------------------------------------------------------------------- }".center(100)	
	print""
	print"{ Open Fasta File }".center(100)
	print""
	print"{ ----------------------------------------------------------------------------------------------------- }".center(100)	
	print""
	print""
	print""

	selection=int(input("\n Bio01>>Write Down The path Of File\nPath:"))
	from Bio import SeqIO
	fasta_sequences = SeqIO.parse(open(path),'fasta')
	with open(output_file) as out_file:
	    for fasta in fasta_sequences:
	        name, sequence = fasta.id, str(fasta.seq)
	        new_sequence = some_function(sequence)
	        write_fasta(out_file)

def GeneBank():
	print '''
 
		$$$$$$\                                $$$$$$$\                      $$\       
		$$  __$$\                               $$  __$$\                     $$ |      
		$$ /  \__| $$$$$$\  $$$$$$$\   $$$$$$\  $$ |  $$ | $$$$$$\  $$$$$$$\  $$ |  $$\ 
		$$ |$$$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$$$$$$\ | \____$$\ $$  __$$\ $$ | $$  |
		$$ |\_$$ |$$$$$$$$ |$$ |  $$ |$$$$$$$$ |$$  __$$\  $$$$$$$ |$$ |  $$ |$$$$$$  / 
		$$ |  $$ |$$   ____|$$ |  $$ |$$   ____|$$ |  $$ |$$  __$$ |$$ |  $$ |$$  _$$<  
		\$$$$$$  |\$$$$$$$\ $$ |  $$ |\$$$$$$$\ $$$$$$$  |\$$$$$$$ |$$ |  $$ |$$ | \$$\ 
		\______/  \_______|\__|  \__| \_______|\_______/  \_______|\__|  \__|\__|  \__|

'''	
	print"{ ----------------------------------------------------------------------------------------------------- }".center(100)	
	print""
	print"{ Analysis Of GeneBank File }".center(100)
	print""
	print"{ ----------------------------------------------------------------------------------------------------- }".center(100)	
	print""
	print""
	print""

	selection=int(input("\n Bio01>>Write Down The path Of File\nPath:"))
	from Bio import SeqIO
	fasta_sequences = SeqIO.parse(open(path),'fasta')
	with open(output_file) as out_file:
	    for fasta in fasta_sequences:
	        name, sequence = fasta.id, str(fasta.seq)
	        new_sequence = some_function(sequence)
	        write_fasta(out_file)	


def maiMenu():
	print("1. Fasta files ")
	print("2. GeneBank files  ")
	print("3. Complement ")
	print("4. Reverse_complement ")
	print("5. Translation ")
	print("6. Transcription ")
	print("7. Translation Tables ")
	print("8. Sequnce length  ")
	print("9. About ")
	print("10. Exit ")
	selection=int(input("\n Bio01>>"))
	if selection ==1:
		Fasta()
		maiMenu()
	elif selection==2:
		GeneBank()
	elif selection==3:
		Complement()
	elif selection==4:
		Reverse_complement()
	elif selection==5:
		Translation()
	elif selection==6:
		Transcription()
	elif selection==7:
		Translation_Tables()
	elif selection==8:
		Sequnce_length()
	elif selection==9:
		program_info()
		maiMenu()
					
maiMenu()














