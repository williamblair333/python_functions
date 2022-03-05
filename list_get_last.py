from pathlib import Path
#data = ["infy", "tcs", "affle", "dixon", "astral"] 

dir_home = str(Path.home()) + "/dir1/subdir1/subdir2"
data = dir_home.split("/")
last_element = data[-1]
print(last_element)
