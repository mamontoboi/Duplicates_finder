import os
import hashlib


def find_duplicates(path):
    """Function is used to check the contents of all files and folders inside
    chosen folder and to return path to the files that are repeated more than once"""
    file_hashes = {}

    # Loop over all files and directories inside folder
    for root, dirs, files in os.walk(path):
        for filename in files:
            file_path = os.path.join(root, filename)
            # Calculate the hash of each file
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()

            # Add path to each file as a value for the hash, serving as the key
            if file_hash in file_hashes:
                file_hashes[file_hash].append(file_path)

            else:
                file_hashes[file_hash] = [file_path]

    # Run through the dict of hashes and notify if value contain more than one path:
    count = 0
    with open('list_of_duplicates.txt', 'w') as f:
        for file_hash, file_paths in file_hashes.items():
            if len(file_paths) > 1:
                f.write(f"Duplicate files for {file_hash} in locations: \n")
                count += 1
                number_of_reps = 0
                for file_path in file_paths:
                    number_of_reps += 1
                    f.write(f" + {number_of_reps} - {file_path} \n")
                f.write('\n')

    if not count:
        print("No duplicates of files were found")


if __name__ == '__main__':
    user_path = input('Write your path here: \n')
    find_duplicates(user_path)