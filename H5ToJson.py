import h5py
import json


def h5_to_json(h5_file, json_file):
    data = {}
    with h5py.File(h5_file, 'r') as f:
        def recursively_load_h5_group(group):
            result = {}
            try:
                for key, item in group.items():
                    if isinstance(item, h5py.Dataset):
                        result[key] = item[()].tolist()  # Convert to list for JSON serialization
                    elif isinstance(item, h5py.Group):
                        result[key] = recursively_load_h5_group(item)
            except Exception as e:
                print(f"Error processing group {group.name}: {e}")
            return result
        
        data = recursively_load_h5_group(f)
    
    
    with open(json_file, 'w') as json_f:
        json.dump(data, json_f, indent=4)


h5_to_json('modelo_extraido\\model.weights.h5', 'modelo_extraido\\model.json')

    # Listar as camadas disponíveis
    