from pathlib2 import Path
import glob



"""Creating a function to replace the text"""
def replacetext(input1, input2):
    """Grabs sales file from same directory and assigns it a variable"""
    file_grab = glob.glob("*.txt")
    sales_file = file_grab[0]

    """Opening the file using the Path function"""
    file = Path(sales_file)

    """Reading and storing the content of the file in a data variable"""
    data = file.read_text()

    """Replacing the text using the replace function"""
    data = data.replace(input1, input2)

    """Writing the replaced data in the text file"""
    file.write_text(data)

    """Return "Text replaced" string"""
    return "Text replaced"

"""Gets old code with spaces appended"""
input1 = input("Enter state code to replace: ") + "   "

""""Gets new code with spaces appended"""
input2 = input("Enter correct state code: ") + "   "

"""Calling the replacetext function"""
replacetext(input1, input2)

print("File corrected")