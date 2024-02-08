import os
import shutil
import datetime

def compress_folder(folder_path, compress_type):
    try:
        # Get the name of the folder
        folder_name = os.path.basename(folder_path)
        
        # Get current date for naming the compressed file
        today = datetime.date.today()
        date_str = today.strftime("%Y_%m_%d")
        
        # Determine the compressed file name
        compressed_file_name = f"{folder_name}_{date_str}.{compress_type}"
        
        # Compress the folder based on the selected compress type
        if compress_type == 'zip':
            shutil.make_archive(compressed_file_name, 'zip', folder_path)
        elif compress_type == 'tar':
            shutil.make_archive(compressed_file_name, 'tar', folder_path)
        elif compress_type == 'tgz':
            shutil.make_archive(compressed_file_name, 'gztar', folder_path)
        else:
            print("Unsupported compression type.")
            return False
        
        print(f"Folder compressed successfully. Compressed file saved as {compressed_file_name}")
        return True
    except Exception as e:
        print(f"Compression failed: {str(e)}")
        return False

def main():
    folder_path = input("Enter the path of the folder to compress: ")
    compress_types = ['zip', 'tar', 'tgz']
    
    print("Available compression types:")
    for i, compress_type in enumerate(compress_types, start=1):
        print(f"{i}. {compress_type}")
    
    choice = int(input("Enter the number corresponding to the desired compression type: "))
    
    if 1 <= choice <= len(compress_types):
        compress_type = compress_types[choice - 1]
        compress_folder(folder_path, compress_type)
    else:
        print("Invalid choice. Please select a number corresponding to the compression type.")

if __name__ == "__main__":
    main()

