 # Extract-Bytes-Can-Log

If you don't know how to run it,open a cmd in the location where the Extract_Bytes is and run python Extract_Bytes.py

This Python script, exact_bytes.py, helps you extract and process CAN bus data from a log file. It identifies unique CAN frames, which consist of a CAN ID and up to 8 data bytes.

The script then formats this data into a specific C-style function call, CanSend(), and exports the results to a new text file. This is useful for anyone who needs to quickly parse CAN log data and generate code for replaying specific messages.

Features:
Parses CAN Log Files: It reads a text file and uses a regular expression to find lines that contain a CAN ID followed by up to 8 hexadecimal data bytes.

Handles Variable Data Length: The script automatically pads data frames with zeros if they have fewer than 8 bytes and truncates them if they have more, ensuring a consistent 8-byte format.

Removes Duplicates: It uses a set to store only unique CAN ID and data byte combinations, preventing redundant entries in the output.

Generates C-Style Code: The output is formatted as <code style="color : #FFB347;">CanSend</code><code style="color : #79BAEC;">(CAN_ID, BYTE1, BYTE2, BYTE3, BYTE4, BYTE5, BYTE6, BYTE7, BYTE8);</code>, which is perfect for generating a script to send specific CAN messages.

User-Friendly Output: The script provides a summary of the number of unique frames exported and the name of the output file.

How to Use:
Set your filename: In the script, change the filename variable to the name of your log file.

Run the script: Execute the script from your terminal: python exact_bytes.py

Check the output: A new file will be created with the same base name as your log file, but with _ExactBytes.txt appended. This file contains the formatted CanSend calls.

