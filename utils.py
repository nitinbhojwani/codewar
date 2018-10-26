from datetime import timedelta

HOLIDAYS = []
SDD = 6
EDD = 2

def cal_delivery_date(del_type, date):
	date += timedelta(days=1) # ignore today's day
	delivery_date = date
	day = 0
	total_days = SDD if del_type == 'standard' else (EDD if del_type == 'express' else None)

	if total_days is None:
		raise Exception('Invalid del_type')

	while(day < total_days or (delivery_date in HOLIDAYS or delivery_date.weekday() > 4)):
		delivery_date += timedelta(days=1)
		day += 1

	return delivery_date
