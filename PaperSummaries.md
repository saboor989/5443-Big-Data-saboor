Compression of Big Data
========================
Compressibility is a main factory dealing with large amount of data. Data generation is increasing in every few months with lots of Data getting generated , it is very important to store data which is a very complex problem. Using compression algorithms and techniques to compress and store data is a solution used for compression of data for storage. 
Summaries :
------------
- 1.Migration compression: Coarse-grained Data reordering to improve compressibility
A solution Migratory Compression(MC) is used to compress the data in modern storage systems, 
it mc the similar data chunks is relocated together  and at decompression the chunks return to their original place. It is a reorganization approach followed , this technique is compared with delta compression which is more complex . Migratory compression found to be more effective compared to traditional compression by 11% to 105% having low impact on run time performance. when added to gzip the result we get is more effective with compression by 44-157% . so MC can be used broadly in our storage systems.

- 2.Compression-AwareI/O Performace Analysis for Big Data Clustering
With increasing volume of data the input/output of data has become a big problem . It a great challenge for data analysis with bottleneck situations. Proposes a compression-aware performance improvement model for big-data clustering. The model analyzes the effects of factors related to compression during computational process. The results validates that using compression the input output performance improves significantly.The models determine when and how to use the techinique for big data analysis.

- 3.Clost : A Hadoop-based Storage System for Big Spatio-Temporal Data Analytics  
Gps-equipped devices generated large amount of data with time and location information, refered as Big Spatio-temporal data . The design and implementation of CloSt , a scalable big spatio-temporal data storage system to support data analytics using hadoop. CloSt uses a spatio-temporal range for scan which avoid scanning whole data set. The model presented has three special treatment on three core attributes an Object id, Location, and Time. CloST hierarchically partitions data using all core attributes for efficient parallel procession of spatio-temporal range scans. a compact storage structure is devised which reducesthe storage size very well. An algorithm used for incrementally adding new data into system. In this paper experiments are conducted on large Gps log dataset and the result show CloST is fast data loading speed ,desired scalablity query prosessing, as well as high data compression ratio.
- 4.Virtual Chunks: On Supporting Random Access to in Scientific Data in Compressible Storage Systems
Data compressions can deplete the I/O pressure of scientific applications on high performance computing systems. Data compression on file brings a dilemma between efficency of random accesses and high compression ratio. File level compression cannot support efficient random access to compressed data any request trigger decompressing whole file. Block level compression has flexible random access but increases overhead when applying which results in degraded compression ratio. Virtual chunks a concept is introduced which support efficient random access to scientific application data without compromizing on compression. virtual blocks are logical block identified by an appended reference without breaking the physical continuity of file content , an appended reference is used for decompressing  from an arbitrary position without effecting the file content to achieve high compression ratio.Virtual chunks are implemented in two forms here middleware  to the GPFS parallel file system and a module in the fusionFS distributed file system.Evaluation shows virtualchunks help impre the input output throughput by 2X speed up.

- 5.Evolutionary Lossless Compression with GP-ZIP*
Gp-zip is the predessor of Gp-Zip* , gp-zip divides the files into blocks of predefined types and then each data block of linear fixed lenght ,is compressed with different algorithms for specific data block. This system given a very good compression ratio. An improvement GP-Zip* is proposed uses a new intelligent crossover and mutation operator to evolve different size blocks. GP-Zip*  uses different algorithm technique for each block. Gp-Zip* uses primitive set of compression algorithms and two transformation techniques . This technique achieved improved compression ration of heterogeneous files in comparison with other techniques. 









Reference  
[1] Lin .X, Lu. G, Dourglis.F,Shilane.P,Wallace.G.
      Migratory compression:Coarse-grained Data reordering to Improve Compressibility,
      12th USENIX Conference on file and Storage Technologie(Fast'14)
[2] Xue. Z, Shen. G, Li. J, Xu .Q , Zhang. Y, Shao. J 
     Compression-aware I/O performance analysis for big data clustering,
     BigMine'12:Proceedings of the 1st International workshop on Big data, Streams and         
     Heterogeneous Source Mining : Algorithms,Systems,Programming Models and
     Applications,August 2012.
[3] Tan.H, Luo.W, M.Ni L.
       ClosT: A Hadoop-based storage system for big spatio-temporal data analytics,
       October 2012 CIKM'12: Proceedings of the 21st ACM international conference on   
        information and knowledge management.
[4] Zhao.D, Yin.J,Qiao.K,and Raicu.I
      Virtual Chunks: On Supporting random Accesses to scientific Data in Compressible Storage         
      Systems,International Conference for High Performance Computing,Networking Storage and    
      Analysis(SC'13) poster session, 2013.
[5] Kattan.A, and Poli.R.
      Evolutionary Lossless Compression with GP-ZIP*, July 2008,GECCO '08:Proceedings of the  
      10th annual conference on Genetic and evolutionary computation. 





