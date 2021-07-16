import mysql.connector
try:
	cnt = mysql.connector.connect(user='kanti', password='Kikuanone1234!', host='192.168.1.46', database='PSM')
	cursor1 = cnt.cursor(buffered=True)
	query = ("SELECT identitySchoolNumber, firstName, lastName, first_name_eng, last_name_eng, mobile, email, lineId FROM student_m2_m5_63 WHERE firstName='" + name + "'")
	m2_5 = cursor1.execute(query)
	query2 = ("SELECT identitySchoolNumber, firstName, lastName, first_name_eng, last_name_eng, mobile, email, lineId FROM student_m4_63 WHERE firstName='" + name + "'")
	m4 = cursor1.execute(query2)
	for idsn, fn, ln, fne, lne, mb, em, line in m2_5:
		print(f"> st_id: {idsn}\nname_th: {fn} {ln}\nname_en: {fne} {lne}\nmobile: {mn}\nemail: {em}\nline: {line}")
except (mysql.connector.Error, FileNotFoundError) as err:
	print(err)
	raise