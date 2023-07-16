## Data Structures in PySpark

### Resilient Distributed Dataset (RDD)

- An object that is not restricted to a type. 
- It can support any data type and is considered as immutable. 
    - It cannot be changed once it has been created. 
- It is fault-tolerant meaning that even if a partition breaks, it will still continue to operate. 
    - Can be distributed into multiple partitions within a single node or a cluster.

![](https://editor.analyticsvidhya.com/uploads/905441_2uwvLC1HsWpOsmRw4ZOp2w%20(1).png)

### Distributed DataFrame

- Similar to how a pandas DataFrame works where the data is organized into rows and columns, but also has the ability to leverage partitions in order for the cluster to tell workers how to perform actions on each partition. Eventually, the partitions can be combined back into a single DataFrame or it can stay as individual partitions to be loaded in parts into any other system.
    - Example: Migrating to SQL Database
        - Load in `append` mode instead of replacing everything in one transaction.