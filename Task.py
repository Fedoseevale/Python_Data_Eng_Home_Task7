import os

def files_rename(my_new_name, digits, source_ext, dest_ext, range_name, path='.'):
    counter = 1
    for filename in os.listdir(path):
        if filename.endswith(source_ext):
            old_name = os.path.splitext(filename)[0]
            old_name_substring = old_name[range_name[0]:range_name[1]] if range_name else ""
            new_filename = f"{old_name_substring}{my_new_name}{str(counter).zfill(digits)}{dest_ext}"
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
            counter += 1

files_rename('new_doc', 6, '.txt', '.md', [3, 6], './my_new_folder')