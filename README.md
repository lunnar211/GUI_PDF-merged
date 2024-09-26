# GUI_PDF-merged
DF merging tool to allow uploading unlimited PDF files for merging! The current implementation already supports adding multiple PDFs, but let's clarify and enhance it a bit more for a smoother experience.
Step-by-Step Enhancements for Unlimited PDF Uploading
Add Functionality: The tool allows you to add as many PDF files as you want without a limit.
Display Information: Update the interface to give feedback on the number of files added.
Optimize Merging: Ensure that merging large numbers of files is handled efficiently.

Explanation of Enhancements
Unlimited PDF Selection:

The add_pdfs function uses askopenfilenames, which allows the user to select multiple files. These files are appended to the pdf_files list.
Each time you add PDFs, the listbox is cleared and updated with the latest selections.
Clear List After Merging:

After the merge is successful, the listbox is cleared, and the pdf_files list is reset. This makes it clear to the user that they can start fresh with new PDFs.
File Handling:

Each PDF file is opened in a with statement to ensure they are properly closed after processing, which is a good practice in file handling.
User Feedback:

Using message boxes (messagebox.showinfo, messagebox.showwarning, and messagebox.showerror) gives users feedback on actions and any potential issues.
How to Use:
Click "Add PDFs" to select multiple PDF files. You can select any number of files you want.
Once you have added your files, click "Merge PDFs" to combine them. You will be prompted to choose where to save the merged file.
You can clear the list of selected PDFs at any time by clicking "Clear List".
Final Thoughts
This implementation effectively allows you to upload and merge an unlimited number of PDF files. The user interface is straightforward, and it provides useful feedback throughout the process.

If you have any more questions or need further assistance, feel free to ask!
 Here’s a step-by-step guide on how to run the PDF merging tool and what packages you need to install.

Step 1: Install Required Packages
For this project, you need to install the PyPDF2 package for PDF manipulation. The tkinter library is included by default in Python installations, so you usually don’t need to install it separately.

Install PyPDF2
You can install the PyPDF2 package using pip. Open your command line or terminal and run the following command:

bash
Copy code
pip install pypdf2
Step 2: Save the Code
Open a Text Editor: Use any text editor or IDE (like Notepad, Visual Studio Code, PyCharm, etc.) to write your Python code.
Copy the Code: Copy the complete Python code for the PDF merging tool from the previous response.
Paste the Code: Paste it into your text editor.
Save the File: Save the file with a .py extension (for example, pdf_merger.py).
Step 3: Run the Application
Using Command Line or Terminal
Open Command Line/Terminal:

Windows: Press Win + R, type cmd, and press Enter.
Mac/Linux: Open the Terminal application.
Navigate to the Directory: Use the cd command to change the directory to where you saved the pdf_merger.py file. For example:

bash
Copy code
cd path\to\your\directory
Replace path\to\your\directory with the actual path where you saved your script.

Run the Script: Type the following command to run your Python script:

bash
Copy code
python pdfmerged.py
If you are using Python 3 specifically, you might need to use:

bash
Copy code
python3 pdfmerged.py
Using an IDE
If you're using an IDE like PyCharm or Visual Studio Code:

Open the IDE and create a new project or file.
Paste the code into the editor.
Run the script using the "Run" button or the corresponding shortcut (usually Shift + F10 in PyCharm or F5 in Visual Studio Code).
Step 4: Using the PDF Merger Tool
Add PDFs: Click the "Add PDFs" button to open a file dialog where you can select multiple PDF files.
Merge PDFs: After selecting your files, click the "Merge PDFs" button. You'll be prompted to choose a location and filename to save the merged PDF.
Clear List: If you want to start over, click "Clear List" to remove all selected files from the list.
Troubleshooting
If you get a "Module Not Found" error: Ensure that you installed PyPDF2 correctly. You can check your installed packages using the command:

bash
Copy code
pip list
If tkinter is not found: If you're using a minimal Python installation, you might need to install tkinter. On Debian-based systems (like Ubuntu), you can install it with:

bash
Copy code
sudo apt-get install python3-tk
Summary
Install the PyPDF2 package.
Save the provided Python code to a .py file.
Run the script using the command line or an IDE.
Use the GUI to merge your PDF files.
