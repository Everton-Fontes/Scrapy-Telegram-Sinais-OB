import json


def save_file(data, file, tp):
    try:
        with open(f'{file}.{tp}', 'w') as f:
            if tp == 'json':
                f.write(json.dumps(data))
            elif tp == 'txt':
                for line in data:
                    f.write(f'{line}\n')
    except:
        print(f"Can't save the file {file}.{tp}")
