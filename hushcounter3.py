/* a scrpit that calculates the sha256 hash of a file or directory and saves it to a file */


import os
import hashlib

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def has_hash_file(file_path):
    """Check if a hash file already exists for the given file"""
    hash_filename = f"{os.path.basename(file_path)}_sha256.txt"
    hash_filepath = os.path.join(os.path.dirname(file_path), hash_filename)
    return os.path.exists(hash_filepath)

def process_path(path):
    """Process a file or directory recursively"""
    if os.path.isdir(path):
        # Calculate directory hash by combining all file hashes
        dir_hash = hashlib.sha256()
        for item in sorted(os.listdir(path)):  # Sort to ensure consistent hash
            item_path = os.path.join(path, item)
            if not item.endswith('_sha256.txt'):  # Skip hash files
                dir_hash.update(calculate_sha256(item_path).encode())
        return dir_hash.hexdigest()
    else:
        return calculate_sha256(path)

def main():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Iterate through all items in the directory
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        
        # Skip if it's the script itself or already has a hash file
        if item == os.path.basename(__file__) or item.endswith('_sha256.txt'):
            continue
        
        if has_hash_file(item_path):
            continue
            
        # Calculate hash
        try:
            file_hash = process_path(item_path)
            
            # Create hash file name
            hash_filename = f"{item}_sha256.txt"
            hash_filepath = os.path.join(current_dir, hash_filename)
            
            # Save hash to file
            with open(hash_filepath, 'w') as f:
                f.write(f"{'Directory' if os.path.isdir(item_path) else 'File'}: {item}\nSHA256: {file_hash}")
                
        except Exception as e:
            print(f"Error processing {item}: {str(e)}")

if __name__ == "__main__":
    main()
