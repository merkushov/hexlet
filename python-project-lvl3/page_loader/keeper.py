'''
    The module responsible for the process of saving data
    to local storage
'''

import os


def save_source_locally(filename, output_dir, content) -> bool:
    '''
        The function of saving data to the specified directory
        by the specified name
    '''
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    file_path = os.path.join(output_dir, filename)
    with open(file_path, 'w') as file_object:
        file_object.write(content)

    return True
