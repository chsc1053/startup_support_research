# Startup Support Research
This repository contains research and Python code for a multi-step process to extract insights for [Startup Support](https://github.com/chsc1053/startup_support).

Steps:
1. Extract relevant documents from Scopus based on user-provided keywords.
	
   Input: Keywords
	
   Output: CSV containing documents related to Input.

2. Identify key terms from the extracted documents.

   Input: Output of 1

   Output: Keywords
   
3. Group identified keywords into meaningful clusters.
	
   Input: Output of 2
	
   Output: Clusters

4. Retrieve documents related to the identified clusters from Scopus using Scopus API.
	
   Input: Output of 3
	
   Output: CSV containing documents related to Input.

5. Summarize the content of the retrieved documents.
	
   Input: Output of 4
	
   Output: Summarized text
   
6. Translate the text into various ;anguages using Microsoft translate API.

   Input: Text

   Output: Translated Text, Audio


Python codes for each step, along with supporting research materials are present in respective directories.
