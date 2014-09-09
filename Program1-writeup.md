
Converting  .csv File format to .json file format
====================================================

Java  as a developing language has many advantages with few implementation dependencies ,Many applications i
n todays time are written in the java 
its  a widely known language.

I would certainly choose .csv but the xml format is much to advantage plus the useage of xml is a factor for xml which
makes it an important one to opt for. 

xml file for conversion to json. 

The .csv file format i believe to be the simplest of all , where data is in comma separated instead of Curly braces or
 square brackets etc...
 The csv file is simple ,supported by almost all spreadsheets and database management systems. 
 Many programming languages have libraries available that support CSV files.
 Many implementations projects support changing the field-separator character and some quoting conventions,
 although it is a safe and simplest  conventions, to increase or maximize the recipient's or users
 chances of handling the data.
 
 I could find a javascript for a specific rows conversion, shown below
 
 Example: 
 
var fs = require('fs');
var csv = require('csv');
var data ="proteins.csv";

/* Uses csv nodejs module to parse the proteins.csv file.
* Parses the csv file row by row and updates the peptide_arr.
* For new entries creates a peptide object, for similar entries it updates the
* counts in the peptide object with the same AGI#.
* Uses a peptide object to store protein ID AGI#, and the associated data.
* Writes all formatted peptide objects to a txt file - output.txt.
*/

// Tracks current row
var x = 0;
// An array of peptide objects stores the information from the csv file
var peptide_arr = [];

// csv module reads row by row from data 
csv()
.from(data)
.to('debug.csv')
.transform(function(row, index) {
    // For the first entry push a new peptide object with the AGI# (row[0]) 
    if(x == 0) {
    // cur is the current peptide read into row by csv module
    Peptide cur = new Peptide( row[0] );

    // Add the assoicated data from row (1-5) to cur
    cur.data.peptides.push({
        "sequence" : row[1];
        "mod_sequence" : row[2];
        if(row[5]){
        "mod_indeces" : "[" + row[3] + ", " + row[4] + "]";
        "spectral_count" : row[5];  
        } else {
        "mod_indeces" : row[3];
        "spectral_count" : row[4];  
        }
    });

    // Add the current peptide to the array
    peptide_arr.push(cur);
    }

    // Move to the next row
    x++;
});

// Loop through peptide_arr and append output with each peptide's AGI# and its data
String output = "";
for(var peptide in peptide_arr) 
{
    output = output + peptide.toString()
}
// Write the output to output.txt
fs.writeFile("output.txt", output);

/* Peptide Object :
 *  - id:AGI#
 *  - data: JSON Array associated
 */
function Peptide(id) // this is the actual function that does the ID retrieving and data 
                    // storage
{
    this.id = id;
    this.data = {
        peptides: []
    };
}

/* Peptide methods :
 *  - toJson : Returns the properly formatted string
 */
Peptide.prototype = {
    toString: function(){
        return this.id + "," + JSON.stringify(this.data, null, " ") + "/n"
    }
};
============================================================================================

In terms of the memory used to store xml is a good option for the json . The xml files uses less amount of space or
storeage space.

I prefer java codes , because it is widely used, 
An sample code i found for converting xml to json format
-------------------------------------------------------------
Copying XML to JSON via XSL Transformation
package de.odysseus.staxon.sample.copy;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import javax.xml.stream.XMLInputFactory;
import javax.xml.stream.XMLStreamException;
import javax.xml.stream.XMLStreamReader;
import javax.xml.stream.XMLStreamWriter;
import javax.xml.transform.Result;
import javax.xml.transform.Source;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.stax.StAXResult;
import javax.xml.transform.stax.StAXSource;

import de.odysseus.staxon.json.JsonXMLConfig;
import de.odysseus.staxon.json.JsonXMLConfigBuilder;
import de.odysseus.staxon.json.JsonXMLOutputFactory;

public class XML2JSON1 {
    /**
     * Copy/format XML as JSON using {@link Transformer#transform(Source, Result)}.
     * @param args ignored
     * @throws TransformerException
     * @throws XMLStreamException
     */
    public static void main(String[] args) throws TransformerException, XMLStreamException, IOException {
        InputStream input = XML2JSON1.class.getResourceAsStream("input.xml");
        OutputStream output = System.out;
        /*
         * If we want to insert JSON array boundaries for multiple elements,
         * we need to set the <code>autoArray</code> property.
         * If our XML source was decorated with <code>&lt;?xml-multiple?&gt;</code>
         * processing instructions, we'd set the <code>multiplePI</code>
         * property instead.
         * With the <code>autoPrimitive</code> property set, element text gets
         * automatically converted to JSON primitives (number, boolean, null).
         */
        JsonXMLConfig config = new JsonXMLConfigBuilder()
            .autoArray(true)
            .autoPrimitive(true)
            .prettyPrint(true)
            .build();
        try {
            /*
             * Create source (XML).
             */
            XMLStreamReader reader = XMLInputFactory.newInstance().createXMLStreamReader(input);
            Source source = new StAXSource(reader);

            /*
             * Create result (JSON).
             */
            XMLStreamWriter writer = new JsonXMLOutputFactory(config).createXMLStreamWriter(output);
            Result result = new StAXResult(writer);

            /*
             * Copy source to result via "identity transform".
             */
             TransformerFactory.newInstance().newTransformer().transform(source, result);
        } finally {
            /*
             * As per StAX specification, XMLStreamReader/Writer.close() doesn't close
             * the underlying stream.
             */
            output.close();
            input.close();
        }
    }
}

and one from other source : 

package {
	
	public class XML2JSON {
		
		private static var _arrays:Array;
		
		public static function parse(node:*):Object {
			var obj:Object = {};
			var numOfChilds:int = node.children().length();
			for(var i:int = 0; i<numOfChilds; i++) {
				var childNode:* = node.children()[i];
				var childNodeName:String = childNode.name();
				var value:*;
				if(childNode.children().length() == 1 && childNode.children()[0].name() == null) {
					if(childNode.attributes().length() > 0) {
						value = {
							_content: childNode.children()[0].toString()
						};
						var numOfAttributes:int = childNode.attributes().length();
						for(var j:int=0; j<numOfAttributes; j++) {
							value[childNode.attributes()[j].name().toString()] = childNode.attributes()[j];
						}
					} else {
						value = childNode.children()[0].toString();
					}
				} else {
					value = parse(childNode);
				}
				if(obj[childNodeName]) {
					if(getTypeof(obj[childNodeName]) == "array") {
						obj[childNodeName].push(value);
					} else {
						obj[childNodeName] = [obj[childNodeName], value];
					}
				} else if(isArray(childNodeName)) {
					obj[childNodeName] = [value];
				} else {
					obj[childNodeName] = value;
				}
			}
			numOfAttributes = node.attributes().length();			
			for(i=0; i<numOfAttributes; i++) {
				obj[node.attributes()[i].name().toString()] = node.attributes()[i];
			}
			if(numOfChilds == 0) {
				if(numOfAttributes == 0) {
					obj = "";
				} else {
					obj._content = "";
				}
			}
			return obj;
		}
		public static function get arrays():Array {
			if(!_arrays) {
				_arrays = [];
			}
			return _arrays;
		}
		public static function set arrays(a:Array):void {
			_arrays = a;
		}
		private static function isArray(nodeName:String):Boolean {
			var numOfArrays:int = _arrays ? _arrays.length : 0;
			for(var i:int=0; i<numOfArrays; i++) {
				if(nodeName == _arrays[i]) {
					return true;
				}
			}
			return false;
		}
		private static function getTypeof(o:*):String {
			if(typeof(o) == "object") {
				if(o.length == null) {
					return "object";
				} else if(typeof(o.length) == "number") {
					return "array";
				} else {
					return "object";
				}
			} else {
				return typeof(o);
			}
		}
		
	}
	
}

Sql to Json:
-------------- 
 Here is a code i found 
 A link to a nice forum , generating the json with optimised way . 
 
  http://stackoverflow.com/questions/6514876/most-effecient-conversion-of-resultset-to-json
 

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
 
