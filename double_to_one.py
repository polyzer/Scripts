import copy, sys
from pyPdf import PdfFileReader, PdfFileWriter

def double_to_one(filename):
	infile = PdfFileReader(file(filename, "rb"))
	out_1 = PdfFileWriter()
	for p in [infile.getPage(i) for i in range(0, infile.getNumPages())]:
		q = copy.copy(p)
		(w, h) = p.mediaBox.upperRight
		p.mediaBox.upperRight = (w/2, h)
		q.mediaBox.upperLeft = (w/2, h)
		out_1.addPage(p)
		out_1.addPage(q)
	out_1.write(open("out.pdf", "wb"))
	print "OK."


filename = raw_input("Insert filename: ")
double_to_one(filename)
