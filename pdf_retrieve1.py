#To install fitz pip command on ubuntu is:  sudo pip install PyMuPDF
import fitz
import sys
### READ IN PDF

doc = fitz.open(sys.argv[1])   #("/home/narendrachintala/Downloads/style_gan.pdf")
text = ["NVIDIA","generator"]

###To loop through each page:
for count in range(len(doc)): #len(doc) gives number_of_pages in document
	page = doc[count]
	multi_instances=[]
	##Finding the words in pdf
	for tex in text:
		text_instances = page.searchFor(tex)
		multi_instances.append(text_instances)
	### HIGHLIGHT
	for instance in multi_instances:
		for inst in instance:
			highlight = page.addHighlightAnnot(inst)
doc.save(sys.argv[2], garbage=4, deflate=True, clean=False)
#("output.pdf", garbage=4, deflate=True, clean=False)



