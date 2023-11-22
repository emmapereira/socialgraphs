import networkx as nx
import pickle
import re 
def remove_number_dot_space(s):
    re.sub(r'^\d+\.\s*', '', s)

def get_first_N_item(d, n):
    items = list(d.items())[:n]
    return dict(items)



with open(r"C:\Users\petno\Documents\nyback\Documents\SocialGraphs\movies_cast_new.pkl", 'rb') as fp:
    data = pickle.load(fp)
    
new_data = get_first_N_item(data, 150)
movie_titles = list(new_data.keys())
G = nx.Graph()
temp_names = new_data.values()
all_names = []
top_cast_nr = 10
for i in temp_names:
    if len(i) > top_cast_nr:
        i = i[:top_cast_nr]
    all_names += i

unique_items = set(all_names)

unique_list = list(unique_items)
G.add_nodes_from(unique_list)
#%%
data = new_data

actor_dict = {}
keys = data.keys()

for actor in list(G.nodes()):
    movies_list = [movie for movie, actors_list in data.items() if actor in actors_list]
    actor_dict[actor] = movies_list


print(actor_dict)
for names in new_data.values():
    if len(names) > top_cast_nr:
        names = names[:top_cast_nr]
    
    for i in range(len(names)):
        for j in range(len(names)):
            if names[i] != names[j]:
                G.add_edge(names[i], names[j])
                
                
degrees = dict(G.degree())
all_degrees = [degrees[i] for i in G.nodes()]
#%%
pos = nx.kamada_kawai_layout(G)
nx.draw(G, pos, node_size = all_degrees)