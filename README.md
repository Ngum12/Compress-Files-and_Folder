
# File Compression Script

## Description
This Python script file allows users to compress files and folders to any compressed file type they choose (e.g., .zip, .tar, .tgz, etc.). It prompts the user to select the folder to compress and then displays a list of available compressed file types. The user can select the desired compressed file type from the list, and the program compresses the selected folder using the chosen file type. If the user selects .zip, the compressed file will be saved as "name_of_the_folder_date_month_year.zip".

## How to Run
- Run the file by executing the following command in your terminal or command prompt:

    ```bash
    compressor.py
    ```

- Follow the prompts to select the folder to compress and choose the desired compressed file type.

## Group Members
- [Ngum Dieudonne]
- [Jules Gatete]
- [Inès IKIREZ]
- [Bosco Ishimwe]
- [Adedigba Adediwura]

## Notes
- This file script uses the `tarfile` library to create tar archives and the `zipfile` library to create zip.tar, .tgz, etc. archives.
