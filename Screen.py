#screen
import json
import requests

data = {
    'criteria': { 
		'elements': {'$all': ['Li']},
		'nelements':3,
	    'band_gap': {"$gte":3.5},
		'e_above_hull': {"$lte":0},
    },
    'properties': [
        'pretty_formula',
		'task_id',
		'band_gap',
		'e_above_hull',
		'formation_energy_per_atom',
		'icsd_ids',
		'spacegroup.symbol',
		'icsd_ids'
		'cif'
    ]
}
r = requests.post('https://materialsproject.org/rest/v2/query',
                 headers={'X-API-KEY': 'Your own API key'},#Generate your own key from materials projects.
                 data={k: json.dumps(v) for k,v in data.items()})
response_content = r.json() 
repo_dicts = response_content['response']
f=open(r'E:\out.txt','w')
print("num_results:",response_content['num_results'],file=f)
print("criteria:",response_content['criteria'],file=f)
print("properties:",response_content['properties'],file=f)
for repo_dict in repo_dicts:
	print(repo_dict['pretty_formula'],repo_dict['task_id'],repo_dict['e_above_hull'],repo_dict['band_gap'],repo_dict['spacegroup.symbol'],repo_dict['icsd_ids'],file=f)