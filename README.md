# ETL-Database
This project presents the practcal usage of multi threading
In this, we made changes in the csv file
For making changes, we converted the file first to txt, made changes and then converted back to csv
We made the following changes in csv:
1) Added +91 before every phone number
2)Deleted second column for every entry
3)We changes the naming of gender from M/F to 1/0
For a file of size of about 5MB, data lines around 10k and the above mentioned changes, without implementing multi threading took around 12 secs
But time taken with multi threading=9.13 secs
Here we made 3 threads:
1)Converting .csv to txt
2)To make changes in txt
3) to convert txt back to csv
