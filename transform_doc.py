import json
from os.path import join, dirname
from watson_developer_cloud import DocumentConversionV1

document_conversion = DocumentConversionV1(
username='1556c8b8-2abe-4d65-8fa4-a1f79b72cf28',
password='palA1cmt4FaH',
version='2016-02-09')


path = input('please enter the path name: ') 
name = input('please enter the name of your new file with appending .json: ')

# Example with JSON
o = open(name, 'w')
f = open(path, 'r+')

config = {
	'conversion_target' : DocumentConversionV1.ANSWER_UNITS
}
json.dump(document_conversion.convert_document(document=f, config=config), o, indent= 2)

f.close()
o.flush()
o.close()
