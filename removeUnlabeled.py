import os
list_ = []
#enter directory with .txt labels 
for file in os.listdir('/home/vigneshdesmond/Desktop/Images/imgs'):
    if file.endswith(".txt"):
        size = len(file)
        list_.append(file[:size - 4])
listsort = [int(x) for x in list_]
listsort.sort()

missing = sorted(set(range(listsort[0], listsort[-1])) - set(listsort)) 
for i in missing:
    filepath = '/home/vigneshdesmond/Desktop/Images/imgs/' + str(i) + '.jpg'
    if os.path.isfile(filepath):
        os.remove(filepath)