import os

folder_path = '.'

def process_filename(filename):
    filename = filename.replace('-', ' ').replace('_', ' ').replace('jar', '').replace('+', '')
    return filename

output_file = 'Mod List.txt'

if os.path.exists(output_file):
    os.remove(output_file)

with open(output_file, 'w') as f:
    f.write('Ваши моды:' + '\n' + '\n')
    for file in os.listdir(folder_path):
        if file.endswith('.jar'):
            processed_name = process_filename(file)
            f.write(processed_name + '\n')