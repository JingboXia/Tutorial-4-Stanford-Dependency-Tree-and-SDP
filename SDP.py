"""
Tutorial codes for SDP.
"""



print("Importing spacy and networkx...\n")
import spacy
import networkx as nx


print("Be sure to download en_core_web_sm first\n>python3 -m spacy download en_core_web_sm\n...\n\n")
print("Load en_core_web_sm, please wait.\n")
nlp = spacy.load("en_core_web_sm")

doc = nlp(u'Jingbo who dresses a green T-Shirt was instructed by Chen.')
for token in doc:
  print((token.head.text, token.text, token.dep_))
#('instructed', 'Jingbo', 'nsubjpass')
#('dresses', 'who', 'nsubj')
#('Jingbo', 'dresses', 'relcl')
#('Shirt', 'a', 'det')
#('Shirt', 'green', 'amod')
#('Shirt', 'T', 'compound')
#('Shirt', '-', 'punct')
#('dresses', 'Shirt', 'dobj')
#('instructed', 'was', 'auxpass')
#('instructed', 'instructed', 'ROOT')
#('instructed', 'by', 'agent')
#('by', 'Chen', 'pobj')
#('instructed', '.', 'punct')

  
# Load spacy's dependency tree into a networkx graph
edges = []
for token in doc:
    for child in token.children:
        edges.append(('{0}'.format(token.lower_),
                      '{0}'.format(child.lower_)))
#[('jingbo', 'dresses'), ('dresses', 'who'), ('dresses', 'shirt'), ('shirt', 'a'), ('shirt', 'green'), ('shirt', 't'), ('shirt', '-'), ('shirt', ' '), ('instructed', 'jingbo'), ('instructed', 'was'), ('instructed', 'by'), ('instructed', '.'), ('by', 'chen'), ('jingbo', 'dresses'), ('dresses', 'who'), ('dresses', 'shirt'), ('shirt', 'a'), ('shirt', 'green'), ('shirt', 't'), ('shirt', '-'), ('shirt', ' '), ('instructed', 'jingbo'), ('instructed', 'was'), ('instructed', 'by'), ('instructed', '.'), ('by', 'chen')]



graph = nx.Graph(edges)

entity1 = 'Jingbo'.lower()
entity2 = 'Chen'.lower()      


print("The SDP instance between entity1 and entity2 is:\n")
print(nx.shortest_path_length(graph, source=entity1, target=entity2))
#3
print(nx.shortest_path(graph, source=entity1, target=entity2))               
#['jingbo', 'instructed', 'by', 'chen']
