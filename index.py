import tkinter as tk
from tkinter import filedialog
from Levenshtein import distance


def compare_files():
    file1 = filedialog.askopenfilename(title="Select first file")
    file2 = filedialog.askopenfilename(title="Select second file")

    with open(file1, mode='r') as f1, open(file2, mode='r') as f2:
        file1_text = f1.read()
        file2_text = f2.read()

    file1_lines = file1_text.split('\n')
    file2_lines = file2_text.split('\n')
    similarities = []
    for line1 in file1_lines:
        for line2 in file2_lines:
            # Levenshtein distance infers how similar the 2 strings are
            if distance(line1, line2) < 2:
                similarities.append((line1, line2))

    if similarities:
        result = tk.Toplevel(root)
        result.title("Similarities Found")
        similarities_text = ""
        counter = 0
        for sim in similarities:
            if len(sim[0]) > 3 and len(sim[1]) > 3:
                counter += 1
                similarities_text += "File 1: " + \
                    sim[0] + "\nFile 2: " + sim[1] + "\n\n"
        similarities_counter = tk.Label(
            result, text=f"Similarities Found: {counter}")
        similarities_counter.pack()
        scrollbar = tk.Scrollbar(result)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        similarities_label = tk.Text(result, yscrollcommand=scrollbar.set)
        similarities_label.pack()
        similarities_label.insert(tk.END, similarities_text)

        scrollbar.config(command=similarities_label.yview)

        close_button = tk.Button(result, text="Close", command=result.destroy)
        close_button.pack()
    else:
        print("No similarities found between the two files.")


root = tk.Tk()
root.title("File Comparator")
root.geometry("500x100")

compare_button = tk.Button(root, text="Compare Files", command=compare_files)
compare_button.pack()

root.mainloop()
