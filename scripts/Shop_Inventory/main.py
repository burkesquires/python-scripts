import csv 

def check_unique_Product_ID(Product_ID):

	with open('ProductRecords.csv','r',newline = '') as file:
		Reader_obj = csv.DictReader(file)
		count = sum(line['Product_ID'] == Product_ID for line in Reader_obj)

		if count == 0:
			return Product_ID   										

		print('The Product_ID already exists..!!')
		print()
		Product_ID = input('Enter unique Product ID: ')
		return check_unique_Product_ID(Product_ID)


def Entry():
	Product_ID = (input('Enter the ID of the Product: '))
	Data = [check_unique_Product_ID(Product_ID)]
	Product_Name 	 = input('Enter the Name of the Product: ')
	Product_Price 	 = int(input('Enter the Price of the Product: '))
	Product_Quantity = int(input('Enter the Quantity of the Product: '))

	Data.extend([Product_Name, Product_Price, Product_Quantity])	

	with open('ProductRecords.csv', 'a',newline = '') as file:
		writer_obj = csv.writer(file)
		writer_obj.writerow(Data)
	print('Entered data has been successfully recorded..!!!')
	print()

def Extract_Data(Product_ID):										
	print()
	with open('ProductRecords.csv','r',newline = '') as file:
		Reader_obj = csv.DictReader(file)

		for line in Reader_obj:

			if line['Product_ID'] == str(Product_ID):					
				for i in line.keys() :

					print(i , ':' , line[i])							

	print()


def Extract_Quantity(Product_ID):
	print()
	with open('ProductRecords.csv','r',newline = '') as file:
		Reader_obj = csv.DictReader(file)
		for line in Reader_obj:

			if line['Product_ID'] == str(Product_ID):					
				print('Quantity of',										
					line['Product_Name'] ,
					':',
					line['Product_Quantity'])
	print()

def Delete_Record(Product_ID):
	with open ('ProductRecords.csv','r+',newline = '') as file:
		Reader_obj  = csv.reader(file)
		records = list(Reader_obj)[1:]
		temp_records = [
			record for record in records if record != [] and record[0] != Product_ID
		]
														

	with open ('ProductRecords.csv','w+',newline = '') as file:
		writer_obj = csv.writer(file)
		writer_obj.writerow(['Product_ID','Product_Name','Product_Price','Product_Quantity'])
		writer_obj.writerows(temp_records)
		print('Record deleted successfully.')


def Update_Price(Product_ID,New_Price):
	with open('ProductRecords.csv','r') as file:
		Reader_obj = csv.DictReader(file, fieldnames = ['Product_ID','Product_Name','Product_Price','Product_Quantity'])

		Temp_records = list(Reader_obj)
	for record in Temp_records :
		if record['Product_ID'] == Product_ID :
			record['Product_Price'] = New_Price						

	Temp_records = Temp_records[1:]
	with open('ProductRecords.csv','w+',newline = '') as file:
		Writer_obj = csv.DictWriter(file, fieldnames = ['Product_ID','Product_Name','Product_Price','Product_Quantity'])
		Writer_obj.writeheader()
		Writer_obj.writerows(Temp_records)
	print('Price has been Updated successfully !!!')


def Update_Quantity(Product_ID,New_Quantity):
	with open('ProductRecords.csv','r') as file:
		Reader_obj = csv.DictReader(file, fieldnames = ['Product_ID','Product_Name','Product_Price','Product_Quantity'])

		Temp_records = list(Reader_obj)
	for record in Temp_records :
		if record['Product_ID'] == Product_ID :
			record['Product_Quantity'] = New_Quantity				

	Temp_records = Temp_records[1:]
	with open('ProductRecords.csv','w+',newline = '') as file:
		Writer_obj = csv.DictWriter(file, fieldnames = ['Product_ID','Product_Name','Product_Price','Product_Quantity'])
		Writer_obj.writeheader()
		Writer_obj.writerows(Temp_records)
	print('Quantity has been Updated successfully !!!')


while True: 														

	print()
	print('Press 1 to Insert Product Details: ')
	print('Press 2 to Fetch Product Details using Product_ID: ')
	print('Press 3 to Fetch Quantity of the Product using Product_ID: ')
	print('Press 4 to Delete Product Details using Product_ID: ')
	print('Press 5 to Update Product Price using Product_ID: ')
	print('Press 6 to Update Product Quantity using Product_ID: ')
	print('Press 0 to Exit: ')
	print()

	Answer = int(input('Press desired number: '))

	if Answer == 0:
		print('Thank You !!')
		exit()

	elif Answer == 1:
		n = int(input('Enter the number of entries to be entered: '))
		for _ in range(n):
			Entry()

	elif Answer == 2:
		Product_ID = input('Enter the Product ID: ')
		Extract_Data(Product_ID)

	elif Answer == 3:
		Product_ID = input('Enter the Product ID: ')
		Extract_Quantity(Product_ID)

	elif Answer == 4:
		Product_ID = input ('Enter the ID of the product to be deleted : ')
		Delete_Record(Product_ID)

	elif Answer == 5:
		Product_ID = input('Enter the Product ID: ')
		New_Price  = int(input('Enter the New Price of the Product: '))
		Update_Price(Product_ID,New_Price)

	elif Answer == 6:
		Product_ID = input('Enter the Product ID: ')
		New_Quantity  = int(input('Enter the New Quantity of the Product: '))
		Update_Quantity(Product_ID,New_Quantity)

	else:
		print('No such option exists..!!')
		exit()

  