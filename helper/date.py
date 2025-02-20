from datetime import timedelta, date ,datetime
import time

def add_date():
	today = date.today()
	ex_date = today + timedelta(days=30)
	pattern = '%Y-%m-%d'
	epcho = int(time.mktime(time.strptime(str(ex_date), pattern)))
	normal_date = datetime.fromtimestamp(epcho).strftime('%Y-%m-%d')
	return epcho , normal_date

def add_date1():
	today = date.today()
	ex_date = today + timedelta(days=60)
	pattern = '%Y-%m-%d'
	epcho = int(time.mktime(time.strptime(str(ex_date), pattern)))
	normal_date = datetime.fromtimestamp(epcho).strftime('%Y-%m-%d')
	return epcho , normal_date

def add_date2():
	today = date.today()
	ex_date = today + timedelta(days=90)
	pattern = '%Y-%m-%d'
	epcho = int(time.mktime(time.strptime(str(ex_date), pattern)))
	normal_date = datetime.fromtimestamp(epcho).strftime('%Y-%m-%d')
	return epcho , normal_date

def add_date3():
	today = date.today()
	ex_date = today + timedelta(days=180)
	pattern = '%Y-%m-%d'
	epcho = int(time.mktime(time.strptime(str(ex_date), pattern)))
	normal_date = datetime.fromtimestamp(epcho).strftime('%Y-%m-%d')
	return epcho , normal_date

def free_tear():
	today = date.today()
	ex_date = today + timedelta(days=2)
	pattern = '%Y-%m-%d'
	epcho = int(time.mktime(time.strptime(str(ex_date), pattern)))
	normal_date = datetime.fromtimestamp(epcho).strftime('%Y-%m-%d')
	return epcho , normal_date

def check_expi(saved_date):
	today = date.today()
	pattern = '%Y-%m-%d'
	epcho = int(time.mktime(time.strptime(str(today), pattern)))
	then = saved_date - epcho
	print(then)
	if then > 0:
		return True
	else:
		return False
