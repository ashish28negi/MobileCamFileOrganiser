from pathlib import Path
import os, shutil

# Source and target directories to be configured
src_dir = r"C:\Users\Ashish\Desktop\Pics\Goa Trip\Srilekha's Camera"
tgt_dir = r'C:\Users\Ashish\Desktop\Pics\TGT'

# Configurable lists of years and month required
list_year=["2015","2016","2017","2018","2019","2020","2021","2022"]
list_month=["January","February","March","April","May","June","July","August","September","October","November","December"]

#function to create directories for each year and month in list
def create_tgt_dirs():
    for y in list_year:
        for m in list_month:
            tgt_path=Path(tgt_dir)/y/m
            #print(type(tgt_path))
            print(f"Creating folder {tgt_path}")
            if tgt_path.is_dir():
                print("Folder already exists")
            else:
                os.makedirs(tgt_path)


def getyear(filename):
    f_year=(filename[4:8])
    for i  in list_year:
        #print(f"i is :{i}... f_year is:{f_year}")
        if f_year ==i:
            return(f_year)

    print("Not a valid year")
    return("ERROR")



def getmonthname(filename):
    mon = (filename[8:10])
    if mon == "01":
        month_name = "January"
    elif mon == "02":
        month_name = "February"
    elif mon == "03":
        month_name = "March"
    elif mon == "04":
        month_name = "April"
    elif mon == "05":
        month_name = "May"
    elif mon == "06":
        month_name = "June"
    elif mon == "07":
        month_name = "July"
    elif mon == "08":
        month_name = "August"
    elif mon == "09":
        month_name = "September"
    elif mon == "10":
        month_name = "October"
    elif mon == "11":
        month_name = "November"
    elif mon == "12":
        month_name = "December"
    else:
        month_name = "ERROR"
        print(f"Invalid Month {mon}")
    return (month_name)


print(f" Home directory path : {Path.home()}")
print(f" Source directory path : {src_dir}")

#main script execution starts here
print(f"Creating target directories ")
create_tgt_dirs()
for f in os.listdir(src_dir):
    print(f)
    print(f[8:10])
    m=getmonthname(f)
    y=getyear(f)
    #print(m)
    #print(y)
    if m=="ERROR" or y=="ERROR":
        print(f"Error in filename format cannot move file {f}")
    else:
        tgt_file_path=Path(tgt_dir)/y/m
        print(f"target file path: {tgt_file_path}")
        shutil.move(Path(src_dir)/f, Path(tgt_file_path)/f )
        print(f"Sucessfully moved  {f} in {tgt_file_path} ")


