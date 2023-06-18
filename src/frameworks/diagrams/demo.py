# Employee Hierarchy
from diagrams import Diagram, Node, Edge
from diagrams.custom import Custom
from os import getcwd

# Create a path to the diagrams folder
diagram_path = getcwd() + "/docs/frameworks/diagrams"

#Node 1 : AliExpress Api Call
#aliexpress_api_call = Node("AliExpress Api Call")

# Node 2 : Senior Engineer
#export_api_results_mongodb = Node("Export API Results MongoDB")

# Node 3: MongoDB
#mongoDB = Node("MongoDB")
with Diagram(filename=f'{diagram_path}/employee_hierarchy', outformat="pdf", direction='LR', node_attr={'fontsize': '12', 'color': 'gold'},
             edge_attr={'labeldistance': '0.7'}, graph_attr={'bgcolor': 'skyblue'}, show = False):

    
    # # Node 1 : Boss
    # boss = Node("Boss")

    # # Node 2 : Senior Engineer
    # senior_engineer = Node("Senior Engineer")

    # # Node 3: Junior Engineer
    # junior_engineer = Node("Junior Engineer")

    # # Edge 1
    # edge_one = Edge(label='just today', color='silver', style='dashed')

    # # Edge 2
    # edge_two = Edge(label='not forever', color='red', style='dotted')

    # boss >> edge_one >> senior_engineer >> edge_two >> junior_engineer
    diagram_path = getcwd() + "/docs/frameworks/diagrams"

    custom_path = getcwd() + "/src/frameworks/diagrams"

    database_node = Custom('AliExpress Api Call', icon_path=f'{custom_path}/db_storage.png')
    mage_ai = Custom('Export API Results MongoDB', icon_path=f'{custom_path}/mage_ai.jpeg')
    mongoDB_1 = Custom('MongoDB', icon_path=f'{custom_path}/mongoDB.png')




    # Edge 1
    edge_one = Edge(label='Data Loader', color='silver', style='dashed')

    # Edge 2
    edge_two = Edge(label='Data Exporter', color='red', style='dotted')

    database_node >> edge_one >> mage_ai >> edge_two >> mongoDB_1

