fileToReadFrom = open("lcl_emails.txt", "r")
fileToWriteIn = open("lcl_emails_write.txt", "a")

line2 = 'https://lh3.googleusercontent.com/-XdUIqdMkCWA/AAAAAAAAAAI/AAAAAAAAAAA/4252rscbv5M/photo.jpg^M'

for line in fileToReadFrom:
        if not "https://lh3.googleusercontent.com/-XdUIqdMkCWA/AAAAAAAAAAI/AAAAAAAAAAA/4252rscbv5M/photo.jpg" in line:
		fileToWriteIn.write('<a href="' + str(line) + '" data-gallery><img src="' + str(line) + '"></a>')

fileToReadFrom.close();
fileToWriteIn.close();
