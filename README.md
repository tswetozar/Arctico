# Arctico
min - max temperature extracting script for a Arctico freezer payload

# This script extracts the min-max temperature pair for a 24 hour period of given time interval from the export log of a 'ARCTIKO ULUF 65®' freezer ( https://www.arctiko.com/products/86-c-ultra-low-temperature-freezers/uluf-65/ ). It's writen on the fly, and it's not refactored properly neither is intended ot be used efficiently, but got the job done for me multiple times, so I thought of sharing it. To use it please follow the these:

1. clone it in it's own directory
2. have the export from the freezer on a tumb drive
3. empty the data_output.txt with a simple text editor
4. change the name of the exported file to -> data_input.txt and replace the original with yours with copy/paste
5. make sure you have "python 3" installed on your system. (if not check for How to in google.com).
6. with a text editor change the values of: "start_date = date(2019, 7, 11)" and "end_date = date(2020, 3, 10)" to suit your case
7. save before close
8. from the terminal go to the directory you cloned the thing
9. start with 'python3 main.py'
10. data_output.txt holds the data. Use copy/paste to use it in a formatted document

HINT: for a long logs the process may take several minutes and may seemed like it's stalled wut ut's not. When the script is done it writes 'Done' on the console
HINT_2: you may want to start with a simple log of 2-3 days to be able to verify the consistency of the output data
