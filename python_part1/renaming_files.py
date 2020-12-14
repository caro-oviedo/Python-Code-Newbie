import re, shutil, os 

date_pattern = re.compile(r"""^(.*?) 
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)\d\d)
(.*?)$
""", re.VERBOSE)


for filename in os.listdir('.'):
    files_to_edit = date_pattern.search(filename)

    if files_to_edit == None: 
        continue 

    before_part = files_to_edit.group(1)
    month_part = files_to_edit.group(2)
    day_part = files_to_edit.group(4)
    year_part = files_to_edit.group(6)
    after_part = files_to_edit.group(8)

    euro_file_name = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    abs_working_dir = os.path.abspath('.')
    filename = os.path.join(abs_working_dir, filename)
    euro_file_name = os.path.join(abs_working_dir, euro_file_name)

    print(f"Renaming '{files_to_edit}' to '{euro_file_name}'...")
    #shutil.move(files_to_edit, euro_file_name)

