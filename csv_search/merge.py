import pandas as pd
import csv


def plus(_df):
	header_path = "/home/gwangsik/python_csv_project/csv_search/result_txt/header_field.txt"
	header_line = []
	d_list = [[]]
	add_list = [[]]

	f = open(header_path, 'r')

	i = 0
	j = 0

	lines = f.readline()
	lines = lines.split(",")
	
	for data in _df:
		d_list[i].append(data)
		j += 1
		if j == 169:
			d_list.extend([[]])
			i += 1
			j = 0

	
	d_list.insert(0,[])
	k = 0
	for h_lines in lines:
		d_list[0].append(h_lines)
	
	
	f.close()
	OutputCsv(d_list)


def OutputCsv(_data):
	with open("../result_search/output_csv.csv", 'w', newline='') as f:
		writer = csv.writer(f)
		for data_list in _data:
			writer.writerow(data_list)


