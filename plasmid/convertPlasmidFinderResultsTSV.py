
import argparse
from enum import IntEnum
import json
from pathlib import Path

# Column indices
class Column(IntEnum):
   Database	= 0
   Plasmid = 1
   Identity	= 2
   QueryTemplateLength = 3
   Contig = 4
   Position_in_contig = 5
   Note = 6
   Accession_number = 7


# Read a data.json file and write a new TSV.
def processJSON(inputFilename, outputFilename):

   with open(inputFilename, 'r') as file:

      try:
         strJSON = file.read()
         if strJSON in (None, ""):
            raise Exception(f"The {inputFilename} file is empty")
         
         # JSON
         JSON = json.loads(strJSON)
         if JSON is None or not JSON or len(JSON) < 1:
            raise Exception("Invalid JSON (empty)")
      
         # plasmidfinder
         if "plasmidfinder" not in JSON:
            raise KeyError("Invalid plasmidfinder key")
         
         plasmidfinder = JSON["plasmidfinder"]
         if plasmidfinder is None or not plasmidfinder or len(plasmidfinder) < 1:
            raise Exception("Invalid plasmidfinder object")

         # user_input
         if "user_input" not in plasmidfinder:
            raise KeyError("Invalid user_input key")
         
         userInput = plasmidfinder["user_input"]
         if userInput is None or not userInput or len(userInput) < 1:
            raise Exception("Invalid user_input object")

         # filename(s)
         if "filename(s)" not in userInput:
            raise KeyError("No filenames are available")
         
         filenames = userInput["filename(s)"]
         if filenames is None or not filenames or len(filenames) < 1:
            raise Exception("No filenames were found")

         # plasmidfinder.user_input.filename(s)[0]
         fileAndPath = filenames[0]
         if fileAndPath in (None, ""):
            raise Exception("Invalid file and path value")
         
         # The genome accession is the directory immediately above the FASTA file.
         directories = Path(fileAndPath).parts
         genomeAccession = directories[len(directories)-2]

         with open(outputFilename, "w") as outputFile:

            # Results
            if "results" not in plasmidfinder:
               raise KeyError("Invalid results key")
            
            results = plasmidfinder["results"]
            if results is None or not results or len(results) < 1:
               raise Exception("Invalid results object")

            # Iterate over all results
            for resultKey in results:
               
               if resultKey == "Gram Positive" or resultKey == "Gram negative":
                  continue
           
               # Get and validate databases.
               databases = results[resultKey]
               if databases is None or not databases or len(databases) < 1:
                  continue

               # Iterate over all database keys.
               for dbKey in databases:

                  # Get and validate the database.
                  database = databases[dbKey]
                  if database is None or not database or len(database) < 1:
                     continue
                  
                  if isinstance(database, str):
                     print(f"No hits found for {dbKey}")
                     continue

                  for contigKey in database:

                     data = database[contigKey]
                     if data is None or not data or len(data) < 1:
                        continue

                     contig = data["contig_name"]
                     if contig in (None, ""):
                        continue

                     identity = data["identity"]
                     
                     # Write a row of TSV to the output file.
                     writeOutputTSV(outputFile, contig, genomeAccession, identity)

      except Exception as e:
         print(f"The following error occurred: {e}")

   outputFile = Path(outputFilename)
   if not outputFile.exists():
      outputFile.touch()

# Trim a string that's possibly null and always return a non-null value.
def safeTrim(text: str):
   if not text or text != text:
      return ""
   
   trimmedText = text.strip()
   if len(trimmedText) < 1:
      return ""
   
   return trimmedText


# Format input parameters as a line of TSV and append to the output file.
def writeOutputTSV(outputFile, contig, genomeAccession, identity):

   # For now, all results are plasmids.
   call = "PL"

   # Validate the contig parameter.
   contig = safeTrim(contig)
   if len(contig) < 1:
      # TODO: raise an exception?
      return
   
   # If "guided" is in Contig, it's a guided file. Otherwise, (or if it contains "denovo") it's denovo.
   guidedIndex = contig.find(".guided.")
   if guidedIndex > -1:
      asmType = "guided"
   else:
      asmType = "denovo"

   # contig_acc is the first token of Contig.
   spaceIndex = contig.find(" ")
   contigAccession = contig[0:spaceIndex]
   
   # Trim the genome accession parameter.
   genomeAccession = safeTrim(genomeAccession)

   # Use identity to calculate the score.
   if identity != identity:
      score = 0
   else:
      score = identity / 100.0

   # Add a line of TSV to the output file.
   outputFile.write(f"{genomeAccession}\t{contigAccession}\t{asmType}\t{call}\t{score}\n")


   

if __name__ == '__main__':

   parser = argparse.ArgumentParser(description="Filter and reformat the data.json file generated by PlasmidFinder and save the results as a TSV file.")

   parser.add_argument("--input", dest="inputFile", metavar='INPUT_FILE', nargs=1, required=True, help="The JSON input filename")
   parser.add_argument("--output", dest="outputFile", metavar='OUTPUT_FILE', nargs=1, required=True, help="The TSV output filename")

   args = parser.parse_args()

   # Validate the input file parameter.
   inputFile = safeTrim(args.inputFile[0])
   if len(inputFile) < 1:
      raise Exception("Invalid inputFile parameter")
   elif not inputFile.endswith(".json"):
      raise Exception("The input file must end in .json")
   
   # Validate the output file parameter.
   outputFile = safeTrim(args.outputFile[0])
   if len(outputFile) < 1:
      raise Exception("Invalid outputFile parameter")

   # Process the input file.
   processJSON(inputFile, outputFile)

