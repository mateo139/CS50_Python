file_name = input("Please enter full name of the file (with extension) ")
#file_name = file_name.lower().replace(" ","")
#file_name = file_name.split(".")

file_name = file_name.lower().replace(" ","").split(".")

n = len (file_name)
file_name = file_name[n-1]

match file_name:
    case "gif":
        print ("image/gif")

    case "jpg" | "jpeg":
        print ("image/jpeg")

    case "png":
        print ("image/png")

    case "pdf":
        print ("application/pdf")

    case "txt":
        print ("text/plain")

    case "zip":
        print ("application/zip")

    case _:
        print("application/octet-stream")