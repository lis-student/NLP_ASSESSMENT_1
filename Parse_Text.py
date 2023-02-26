import tika
from tika import parser
tika.initVM()

def parse_text(filename):
    parsed = parser.from_file(r"C:\Users\belmi\Downloads\{filename}.pdf".format(filename=filename))
    file = open(r"C:\Users\belmi\OneDrive\Desktop\Python Projects\{filename}.txt".format(filename=filename), 'w', encoding= "utf-8")
    file.write(parsed['content'])
    file.close()

parse_text('Harry_Potter_Complete_English')