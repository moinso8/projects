import os
import shutil

#cleans up files in path into respective folders based on file extensions

print("""
	'images' moves all images into a new folder called images \n
	'documents' moves all documents into a new folder called documents\n
	'videos' moves all videos into a new folder called videos\n
	'everything' moves all files into their respective folders\n
	""")

file_type = str(input("which type of files would you like to move? "))

path = "/home/david/Downloads/"
files = os.listdir(path)

extensions = {
	"documents": (".pdf", ".txt", ".odt", ".docx", ".doc", ".ppt", ".rtf"),
	"images": (".tif", ".jpg", ".gif", ".png"),
	"videos": (".avi", ".mkv", "mp4")
}

def create_folder(file_type):
	"""creates a folder for desired file type. If existant, prints out a message"""
	if file_type in files:
		print("movin all {} type files into their folder".format(file_type))
	else:
		print("created a folder {} and moved all {} type files into it".format(file_type,file_type))
		os.mkdir(path + file_type)

def cleanup_files(f_type):
	"""moves desired file type into a newly created, or existant folder"""
	f_type = file_type

	if f_type == "documents":
		exts = extensions["documents"]
	if f_type == "images":
		exts = extensions["images"]
	if f_type == "videos":
		exts = extensions["videos"]

	create_folder(file_type)

	for file in files:
		if file.endswith(exts):
			shutil.move(path+file,path+ file_type+"/"+file)

def cleanup_all():
	"""moves all file types into their respective folders"""
	file_types = ("documents", "videos", "images")

	for file_type in file_types:
		create_folder(file_type)
		for file in files:
			if file.endswith(extensions[file_type]):
				shutil.move(path+file,path+ file_type+"/"+file)


if file_type == "everything":
	cleanup_all()
else:
	cleanup_files(file_type)


