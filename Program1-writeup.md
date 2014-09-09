
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
an sample code i found for converting xml to json format
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

and one from other source : an problem faced 

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


The 
