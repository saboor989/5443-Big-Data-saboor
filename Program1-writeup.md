
Converting  .csv File format to .json file format
====================================================

I would certainly choose .csv but the xml format is much to advantage plus the useage of xml is a factor. xml which
makes it an important one to opt for. 

The .csv file format is the simplest of all , where data is in comma separated instead of Curly braces or
square brackets etc...
The csv file is simple ,supported by almost all spreadsheets and database management systems. 
Many programming languages have libraries available that support CSV files.
Many implementations projects support changing the field-separator character and some quoting conventions,
although it is a safe and simplest  conventions, to increase or maximize the recipient's or users
chances of handling csv. 
 
The Json format is object and array based. JavaScript Object Notation, an open standard format that is human-readable. Is an attribute–value pairs. It is basically used to transmit data between a server and web application.

I choosen python as an preffered language for converting the data from one format to other Like csv to json.
because of the libraries ,modules , and easy conversion of data etc...

* import the csv module for reading the data and json module for writing the data.
* we can read the file.csv which is comma separated . 
* read the file name as to be the object of the file.
  like say a file .csv is having data like 
  file name "Result"
  Data in file Example:
  
  Name | Age |    DOB  | Result
  -----|-----|---------|--------
  sam  | 15  | 12-09-70|  B    
  tina | 15  | 11-07-70|  A    

The Object will be  "Result" and 
the Data in file become the array with key value pairs

Json file:
like 
{
"Result":[
"Name":"sam",
"age":"15",
"DOB":"12-09-70",
"Result":"B",
]
[
"Name":"tina".
"age":"15",
"DOB":"11-07-70",
"Result":"A",
]
}

Mostly the .csv file contains first line as headings for the columns and rows with the values of data . 

* Reading the first line to be considered as the headings or key-value pairs for each object
* Ceate object for the key-value pairs to be as main object into the file 
* Read line by line for the data from the csv file till the end of file one at time optimizing usage of memory 
* Read the "commas" as to considered as an value to create key-value in json file and commas as delimiter for taking     values. 
* The json file open and close and write the particular data as shown by inserting the proper "{}" and "[]"
  "" : and , to represent the json file format. 
* for looping for the dynamic number of rows and columns to be written in json
* in the end the the closing flower brace to indicate the end of object with many arrays with key value pairs.

The important thing here is , reading line by line of the file which helps in preventing some data handling problems.
The memory useage and time consumption to convert big files are a factor to be considered while implementing and converting the files. 


Zip and Gzip the files 
---------------------------------------------
The original size: of files : 

File| Original size
----|---------------
* GpsFilePoints.csv	|	484M	 
* GpsFilePoints.sql	|	467M	 
* GpsFilePoints.xml.gz |	75M	 
* GpsFilePoints.yml.gz	|	60M	 

The file size after gzip is : 

  File | Original size | Percentage Reduced
  -----|---------------|---------------------
* GpsFilePoints.csv.gz	|	58.28M reduced by |87.9%	 
* GpsFilePoints.sql.gz	|	59.09M	reduced by |87.34%
* GpsFilePoints.xml.gz |	65.92M	reduced by |12%
* GpsFilePoints.yml.gz	|	57.1M	 reduced by |5%

The file size after zip is : 

File| original size | Percentage Reduced
-----|--------------|---------------------
* GpsFilePoints.csv.zip	|	58.28M	 reduced by |87.9%
* GpsFilePoints.sql.zip	|	59.09M	 reduced by |87.34%
* GpsFilePoints.xml.zip |	65.92M	 reduced by |12%
* GpsFilePoints.yml.zip	|	57.1M	  reduced by |5%


After doing the zip and gzip . The files size are same for both zip and gzip files. 
The difference observed is only in few 100 bytes . when calculating the percentage 
The 100 bytes comes around .001 % or .003 % only.

The .csv the gzip reduces size by few 100's bytes compared to zip. 
The .sql the gzip reduces size by few 100's bytes compared to zip.
The .xml the gzip reduces size by few 100's bytes compared to zip.
The .yml the gzip reduces size by few 100's bytes compared to zip.

zip or Gzip
=============

zip :-

Simply putting zip is a file format which compresses the files or reduce the file size. 
widely used in windows os .


Gzip:-

Gzip is a file format which also compresses the files or reduce the file size . 
widely used in Uinx os.

