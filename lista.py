def list_a(path):
	import csv
	users = ['John', 'Amy', 'Brad']
	ages = [12, 24, 36]
	rows = zip(users, ages)
	with open(path, 'w+') as file:
		f = csv.writer(file)
		f.writerow(("Name", "ID"))
		for row in rows:
			f.writerow(row)
		file.close()
