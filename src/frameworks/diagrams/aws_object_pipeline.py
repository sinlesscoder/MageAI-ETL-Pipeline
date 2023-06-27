from diagrams import Diagram, Cluster, Edge
from diagrams.programming.language import Python
from diagrams.custom import Custom
from diagrams.aws.storage import SimpleStorageServiceS3Bucket

from os import getcwd

# Path to save diagrams
diagram_path = getcwd() + "/docs/frameworks/diagrams"

custom_path = getcwd() + "/src/frameworks/diagrams"

with Diagram(filename=f'{diagram_path}/aws_object_pipeline', outformat='jpg', direction='TB', graph_attr={'bgcolor': 'limegreen'}, node_attr={'fontsize': '10'}):
    
    # Custom Edges
    edge_one = Edge(label='input_data', color='gray', style='dashed')

    # Custom Nodes
    database_node = Custom('raw_data', icon_path=f'{custom_path}/db_storage.png')
    mage_ai = Custom('etl_pipeline', icon_path=f'{custom_path}/mage_ai.jpeg')

    # Amazon
    s3_node = SimpleStorageServiceS3Bucket('raw_data_objects')
    
    # Another Context Manager for the Cluster
    with Cluster("Mage Python Scripts", graph_attr={'bgcolor': 'yellow'}):
        # Node for Python
        python_node_1 = Python("retrieve_db.py")

        # Node for Transformation
        python_node_2 = Python("transform_data.py")

        # Node for export_s3
        python_node_3 = Python('export_s3.py')
    
    database_node >> edge_one >> mage_ai >> python_node_2 >> s3_node

    
