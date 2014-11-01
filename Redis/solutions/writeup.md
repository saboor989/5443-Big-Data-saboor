1) What are the number of unique food "items" in the file. You might be tempted to count the number of lines, since we assume that each line contains one food item. I will warn you that this is an incorrect solution. Just by chance, there might be a few duplicated rows in the file, therefore line counting would be wrong.

In my solution I opted to use a redis "sets" since all keys must be unique. I used the "description" field as the "key" ,(e.g. SADD Key).
I could then use SCARD to count the number of unique items's in the hash, thereby giving me the number of unique values in the data set.

2) How many unique nutrients are there?

In my solution i opted to use redis "sets" since all keys must be unique. I used the tagname field as the key. 
i could then use scard to count the number of unique nutrients by going inside the array "NUTRIENTS",
thereby giving me the number of unique values in the data set.

3) What are the top 5 most commonly occuring nutrient?

In my solution i used the hashes to add and increment the values of the nutrients in a hash called "taghash" which are occurring again , by incrementing
i can count the number of times it is occurring. then using scard to get the lenght of the hash(taghash) and then using zrange to get the values of the 
elements in the given range. then using while to print all the values from the zrange variable. and using zscore to print the value of the member or element. 


4) Given a specific nutrient, what percentage of food items contain this nutrient?

In my solution first we get the sets to get the food items . then using the zincrby to get the "taghash" with the nutrients . 
then calculating using scard to get the number of items and zscore to get the values. then using percentage formulae for calculating the percentage. 
and displaying it.  

5) This problem is more about size of the database depending on how data is stored. I want the size of the data base on disk (remember info && human readable). You will also need to make sure you run flushall before loading this structure.You can make multiple passes on the data, and I'm not looking for extremely efficient processing, I just want it loaded as prescribed. You don't have to perform tasks in the order asked either. I just want to final resulting data structures, and size of all of them on disk.

Store all id's for nutrients in a set.
Store all nutrients in a hash with thier id's as keys.
Store all tagnames in a set.
Store all nutrients in a hash with tagnames as keys.
Store all nutrient id's in a list with the item id (top level _id) as the key.

In my solution we do for loop to get all the requirement by using sadd add values to the set, hset to set the values to the hash . 
calling the function totalmemoryfunction to print the total memoryused. 