import os
from pathlib import Path
import re

# tokens to search for in the file
token_title = "title:"
token_title_expression = rf"{re.escape(token_title)}\s*'([^']+)'"
token_date = "date:"  
token_date_expression = rf"{re.escape(token_date)}\s*(\S+)"

# number of words to include in the new name
num_words = 4

def rename_files_in_folder(folder_path):
    """
    Automatically renames files in the specified directory based on the content of the files.
    
    Args:
        folder_path (str): The path to the directory containing the files to rename.
    """
    # Get a list of all files in the folder
    try:
        files = os.listdir(folder_path)
        # Loop through each file
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)

            # Check if it's a file (ignore directories)
            if os.path.isfile(file_path):
                # Read the contents of the file (assuming it's a text file)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                # # Search for the token and the name next to it
                match_title = re.search(token_title_expression, content)
                match_date = re.search(token_date_expression, content)
                
                if match_title:
                    sentences = match_title.group(1).strip()
                    words = '-'.join(sentences.split()[:num_words])
                    title = words.lower().replace(':', '')

                if match_date:
                    date = match_date.group(1)

                new_name = f"{date}-{title}.md" if match_date and match_title else f"{file_name}"

                if file_name == new_name:
                    print(f"File {file_name} already has the correct name.")
                    continue

                # Ensure the new name does not already exist
                new_file_path = os.path.join(folder_path, new_name)
                counter = 1
                while os.path.exists(new_file_path):
                    new_name = f"{date}-{title}_{counter}.md" if match_date and match_title else f"{file_name}"
                    new_file_path = os.path.join(folder_path, new_name)
                    counter += 1

                # Rename the file
                os.rename(file_path, new_file_path)
                print(f"Renamed: {file_name} to {new_name}")
            else:
                print(f"Token not found in {file_name}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    

if __name__ == "__main__":
    post_folder_path = Path('./_posts/').resolve()
    project_folder_path = Path('./_projects/').resolve()

    rename_files_in_folder(post_folder_path)
    rename_files_in_folder(project_folder_path)
