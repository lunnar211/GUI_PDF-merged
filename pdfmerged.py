import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

# Create the main application window
root = tk.Tk()
root.title("PDF Merger")
root.geometry("400x300")

# List to store selected PDF files
pdf_files = []

# Function to add PDF files
def add_pdfs():
    files = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF Files", "*.pdf")])
    if files:
        pdf_files.extend(files)
        listbox.delete(0, tk.END)  # Clear the listbox
        for file in pdf_files:
            listbox.insert(tk.END, file)  # Display all selected files

# Function to merge the PDF files
def merge_pdfs():
    if len(pdf_files) < 2:
        messagebox.showwarning("Warning", "Please select at least 2 PDF files to merge.")
        return

    output_filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    
    if output_filename:
        pdf_writer = PyPDF2.PdfWriter()
        try:
            for pdf in pdf_files:
                with open(pdf, 'rb') as pdf_file:  # Open each file in read mode
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    for page_num in range(len(pdf_reader.pages)):
                        pdf_writer.add_page(pdf_reader.pages[page_num])
            
            with open(output_filename, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

            messagebox.showinfo("Success", f"PDFs merged successfully into {output_filename}")
            listbox.delete(0, tk.END)  # Clear the listbox after merging
            pdf_files.clear()  # Clear the pdf_files list

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Function to clear the PDF file list
def clear_list():
    listbox.delete(0, tk.END)
    pdf_files.clear()

# Create a button to add PDF files
add_button = tk.Button(root, text="Add PDFs", command=add_pdfs)
add_button.pack(pady=10)

# Create a listbox to show the selected PDFs
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Create a button to merge the selected PDFs
merge_button = tk.Button(root, text="Merge PDFs", command=merge_pdfs)
merge_button.pack(pady=10)

# Create a button to clear the list
clear_button = tk.Button(root, text="Clear List", command=clear_list)
clear_button.pack(pady=10)

# Run the application
root.mainloop()
