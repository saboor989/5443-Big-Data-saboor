
Converting  .csv File format to .json file format
====================================================

Java  as a developing language has many advantages with few implementation dependencies ,Many applications 
in todays time are written in java. Its  a widely known language.

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

* import the csv module for reading the data nad json module for writing the data.
* we can read the file.csv which is comma separated . 
* read the file name as to be the object of the file.
  like say a file .csv is having data like 
  file name "Result"
  Data in file Example:
  
  Name | Age |    DOB  | Result
  -----|-----|---------|--------
  sam  | 15  | 12-09-70|  B    
  tina | 15  | 11-07-70|  A    

The Object will be the "Result" and 
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

Mostly the .csv file contains the headings for the columns and rows of data . 

* reading the first line to be considered as the headings or key-value pairs for each object
* ceate object for the key-value pairs to be as main object into the file 
* read line by line for the data from the csv file till the end of file
* and read the "commas" as to considered as an value to create key-value in json file
* in the json file open and close and write the particular data as shown by inserting the proper "{}" and "[]"
  "" : and , to represent the json file format. 
* for looping for the dynamic number of rows and columns to be written in json
* in the end the the closing flower brace to indicate the end of object with many arrays with key value paris.

The important thing here is the reading line by line of the file which helps in preventing some problems






Zip and Gzip the files 

The original size: of files : 

* GpsFilePoints.csv	-	484M	 
* GpsFilePoints.sql	-	467M	 
* GpsFilePoints.xml.gz -	75M	 
* GpsFilePoints.yml.gz	-	60M	 

The file size after gzip is : 

* GpsFilePoints.csv.gz	-	58.28M reduced by :87.9%	 
* GpsFilePoints.sql.gz	-	59.09M	reduced by :87.34%
* GpsFilePoints.xml.gz -	65.92M	reduced by :12%
* GpsFilePoints.yml.gz	-	57.1M	 reduced by :5%

The file size after zip is : 

* GpsFilePoints.csv.zip	-	58.28M	 reduced by :87.9%
* GpsFilePoints.sql.zip	-	59.09M	 reduced by :87.34%
* GpsFilePoints.xml.zip -	65.92M	 reduced by :12%
* GpsFilePoints.yml.zip	-	57.1M	  reduced by :5%


zip or Gzip
=============

zip :-

Simply putting zip is a file format which compresses the files or reduce the file size. 
widely used in windows os .


Gzip:-

Gzip is a file format which also compresses the files or reduce the file size . 
widely used in Uinx os.

if both reduces the file size what is the difference?
 
 This both zip and gzip compress and reduce the file size but both are programming techniques to reduce the size so 
 both are different in implementation but they both do the same thing reduce the size. 
 
The ZIP format supports several compression methods:
-----------------------------------------------------

0 - The file is stored (no compression)
1 - The file is Shrunk
2 - The file is Reduced with compression factor 1
3 - The file is Reduced with compression factor 2
4 - The file is Reduced with compression factor 3
5 - The file is Reduced with compression factor 4
6 - The file is Imploded
7 - Reserved for Tokenizing compression algorithm
8 - The file is Deflated
9 - Enhanced Deflating using Deflate64(tm)
10 - PKWARE Data Compression Library Imploding (old IBM TERSE)
11 - Reserved by PKWARE
12 - File is compressed using BZIP2 algorithm
13 - Reserved by PKWARE
14 - LZMA (EFS)
15 - Reserved by PKWARE
16 - Reserved by PKWARE
17 - Reserved by PKWARE
18 - File is compressed using IBM TERSE (new)
19 - IBM LZ77 z Architecture (PFS)
97 - WavPack compressed data
98 - PPMd version I, Rev 1


zip:- is a all in one technique means it compress and archive but 
gzip is a purely compressing technique it uses tarball for archiving  . 

* zip is a software use algorithms which compresses and archieve the file.
  we can retrieve or extract the files from the compressed folder one by one 
* In zip, individual files are compressed and then archive is done which enable us to pull a single file 
  from the zip, it is simple it extract the file and then decompress it. 
  
  * The advantage is the disadvantage of zip . It can do both compression and archive
    but this make the file use more space as when compared with gzip but it compress 
    the file  properly . As both zip and gzip can be used with any kind of operating system
    The zip is incorporated with the windows as a internal function of os. 
    The extension of compressed file is " .zip". 

Gzip:- It is the technique mainly used for compression it uses TAR for archiveing. 

* Gzip archive all the files into a single tarball before compression. 
  It then compresses the whole tarball into one compressed file. 
* Whole file need to be decompressed before you can extract the file we want from the archieve.
  
  * The disadvantage is the biggest advantage of gzip the compression algorithm in gzip 
    compresses one large file instead of multiple smaller ones, it takes advantage of the 
    redundancy in the file to reduce the file size even further. 
    gzip has a lot of followers from Unix operating system. such as many linux distributions.
    The extension of compressed file is " .tar.gz" or ".tgz".
 

 
