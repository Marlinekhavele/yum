import xlrd
import MySQLdb

book = xlrd.open_workbook(data_test.xlsx)
 Establish a MySQL connection
database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "famers")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the INSERT INTO sql query
query = """INSERT INTO orders (name, managment, crop, variety, croppingsystem, plotsize, spacing, harvestingdate, samplingdate, standcount, plantsharvest, biomass, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
		name		= sheet.cell(r,).value
		managment	= sheet.cell(r,1).value
		crop			= sheet.cell(r,2).value
		variety		= sheet.cell(r,3).value
		croppingsystem		= sheet.cell(r,4).value
		plotsize	= sheet.cell(r,5).value
		spacing		= sheet.cell(r,6).value
		harvestingdate		= sheet.cell(r,7).value
		samplingdate		= sheet.cell(r,8).value
		standcount		= sheet.cell(r,9).value
		plantsharvest		= sheet.cell(r,10).value
		biomass		= sheet.cell(r,11).value
		total	= sheet.cell(r,12).value

		# Assign values from each row
		values = (name, managment, crop, variety, croppingsystem, plotsize, spacing, harvestingdate, samplingdate, standcount, plantsharvest, biomass, total)

		# Execute sql Query
		cursor.execute(query, values)

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print ""
print "All Done! Bye, for now."
print ""
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print "I just imported " %2B columns %2B " columns and " %2B rows %2B " rows to MySQL!"