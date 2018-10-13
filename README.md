Module Name: POS Tagging using Viterbi Algorithm

Name:k.chetan & hemanth kancharla


1- Requirements:
----------------
 Operating System               :       LINUX (tested on >= Fedora-19 , >= Ubuntu 10.04)

 Compiler/Interpreter/Librarie(s):      Python

2- Directory Structure:
-----------------------
	|-- code

	|   |-- bin

	|   |   |-- compile.sh

	|   |   |-- HindiWMrun.sh

	|   |   |-- HindiWOMrun.sh

	|   |   |-- installib.sh

	|   |   |-- KannadaWMrun.sh

	|   |   |-- KannadaWOMrun.sh

	|   |   |-- TeluguWMrun.sh

	|   |   -- TeluguWOMrun.sh

	|   |-- lib

	|   -- src

	|       |-- hindi_morphed.out

	|       |-- hindi_multiple.fst

	|       |-- hindi.out

	|       |-- hindi_pos_wx.txt

	|       |-- hindi_test_wx.txt

	|       |-- ladakA-paradigm.lex

	|       |-- ladakI-paradigm.lex

	|       |-- postag_hindi_morph.py

	|       |-- postag_hindi.py

	|       |-- postag_telugu_morph.py

	|       |-- postag_telugu.py

	|       |-- TagSet.txt

	|       |-- telugu_morphed.out

	|       |-- telugu_multiple.fst

	|       |-- telugu.out

	|       |-- telugu_pos_wx.txt

	|       -- telugu_test_wx.txt

	|-- README.txt

	|-- Report

	|   -- 201201124_201225002.pdf

	-- Results

   	 |-- hindi.out
    
   	 |-- kannada.out
    
    	 -- telugu.out
    

6 directories, 7 files                
                      
(FOLLOW THIS DIRECTORY STRUCTURE ONLY, recreate your own tree at last)


3- How to run
---------------
   ---> bin - (bin folder contains 3 shell scripts (.sh files). The description of the following .sh files are given below.)

        ---> sh installib.sh 
			If you are using any external libraries or libraries which are not included in the standard JAVA or Python libraries, this script installs the required 				libraries, for no such libraries, this file should be left blank (the libraries should be included in the 'lib' folder)

        ---> sh compile.sh 
			This file should contain the commands to compile your program. For Java, this script should contain 'javac program_name.java' for creating the class files, cc/			gcc for C. For Python, this script should be left blank.

        ---> sh HindiWMrun.sh input_file	(Hindi with morph feature)
	     sh HindiWOMrun.sh input_file	(Hindi without morph feature)
	     sh TeluguWMrun.sh input_file	(Telugu with morph feature)
	     sh TeluguWOMrun.sh input_file	(Telugu without morph feature)
	     sh KannadaWMrun.sh input_file	(Kannada with morph feature)
	     sh KannadaWOMrun.sh input_file	(Kannada without morph feature)	
             
			This should contain the commands to run your programs
				For Java, this should contain 'java program_name input_file' (the input_file is the file to be tagged)
				For Python, this file should contain 'python program_name.py input_file'
				Make sure this shell script only has one input argument.
				#####The output of the program should be displayed on the terminal#####
				If you are using two languages for implementing the viterbi, the corresponding .sh files should be filled to run the program, one language which is not chosen should be left blank.
   
   ---> src - 
	
	This folder contains all your programs to be run, this also contains the training model as well as the input files used for training
   
   ---> lib 
	
	This folder contains all the external libraries which your programs are using. If you are not using any custom libraries, only using standard libraries of Java and Python, 	this folder should be left blank.


4- NOTE :
--------------

	Please Make sure your code will run only throw run.sh and from anywhere in the terminal. Use relative paths for running the programs, do not use absolute paths.

5 - For running the Assignment4eval.pyc :-
----------------------------------------------

	Run this following command :-
		
	python Assignment4eval.pyc [-h] [-g GOLDPOS] [-t TESTPOS]
	
	GOLDPOS is the Gold standard POS tagged data which is annotated manually, TESTPOS is the tagged file which your program generates.
	After executing the program, you will get the % accuracy of your implementation.

