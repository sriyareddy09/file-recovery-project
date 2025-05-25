# File Recovery Project

## Overview
This project demonstrates recovering deleted files and filtering them from a forensic disk image using Autopsy, FTK Imager and Python.

- A disk image of the evidence is made using FTK Imager in raw format (.dd)
- Autopsy was used to analyze the disk image and generate a comprehensive CSV report (`autopsy_report.csv`) containing metadata about all files, including deleted ones.
- A Python script (`filter_deleted_files.py`) filters the CSV to identify deleted/unallocated files based on `Flags(Dir)`.
- The identified files were manually or programmatically recovered and stored in the `recovered_files/` directory.
- Screenshots documenting the steps in Autopsy are included in the `screenshots/` folder.

## Project Structure

├── recover_deleted.py
├── ftk_imager_report.txt
├── autopsy_report.xlsx
├── recovered_files/
├── screenshots/
├── forensic_findings.txt
├── README.md


## How to Use

1. A folder must be made in external drive containing documents in different formats as you wish.
2. The contents of this folder must be deleted.
3. Using ftk imager, we must create a disk image of the drive.
4. Load the file into the Autopsy tool for analysis.
5. Open the CSV report exported from Autopsy.
6. Run the Python script to filter deleted files:
   python filter_deleted_files.py
7. Open the file to check the documents and recover them into a new folder (namely recovered_files).

## Tools Used
1. FTK Imager by Exterro
2. Autopsy (Digital Forensics Tool)
3. Python 3.x with pandas library

## Notes
> Ensure pandas is installed (pip install pandas).
> The script filters based on keywords in the Flags(Dir) column such as "unallocated", "orphan", and "deleted".
> Modify the script as needed to adjust filters or automate copying of files.


