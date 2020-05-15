'''
Nose tests for acp_times.py
'''

from acp_times import open_time
from acp_times import close_time
import nose
import logging
import arrow

logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.WARNING)
log = logging.getLogger(__name__)


def test_less():
	'''
	Tests a brevet control which is less than or equal to the first value 
	in the acp table.
	'''
	date = arrow.Arrow(2019,5,5)
	
	assert open_time(150, 200, arrow.get(date)) == (date.shift(hours=4,minutes=25)).isoformat()
	assert close_time(150, 200, arrow.get(date)) == (date.shift(hours=10)).isoformat()

def test_bounds():
	'''
	Tests a brevet control that is exactly equal to one of the distance 
	values in the table.
	'''
	
	date = arrow.Arrow(2019,5,5)
	
	assert open_time(600, 600, arrow.get(date)) == (date.shift(hours=18,minutes=48)).isoformat()
	assert close_time(600, 600, arrow.get(date)) == (date.shift(hours=40)).isoformat()

def test_mult():
	'''
	Tests a brevet control which contains multiple markers in the acp table.
	'''
	date = arrow.Arrow(2019,5,5)
	
	assert open_time(700, 1000, arrow.get(date)) == (date.shift(hours=22,minutes=22)).isoformat()
	assert close_time(700, 1000, arrow.get(date)) == (date.shift(hours=48,minutes=45)).isoformat()

def test_odd():
	'''
	Tests an odd brevet control length.
	'''
	
	date = arrow.Arrow(2019,5,5)

	assert open_time(311, 400, arrow.get(date)) == (date.shift(hours=9,minutes=21)).isoformat()
	assert close_time(311, 400, arrow.get(date)) == (date.shift(hours=20,minutes=44)).isoformat()


def test_mid():
	'''
	Tests a nonboundary brevet control.
	'''

	date = arrow.Arrow(2019,5,5)

	assert open_time(550, 600, arrow.get(date)) == (date.shift(hours=17,minutes=8)).isoformat()
	assert close_time(550, 600, arrow.get(date)) == (date.shift(hours=36,minutes=40)).isoformat()
