from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep

# Message constants
DATA_NOT_FOUND = "Error: We couldn't find the following data:"
FETCH_SUCCESS = "Success! Records fetched."

# Options for different webdrivers
options = Options()
options.headless = True

class UserProgress():
	def __init__(self, username):
		self.username = username
		self.url = 'https://www.freecodecamp.org/' + self.username

	def fetch_data(self):
		self.data = {}

		print('Hang on, skimming the records for user "{}"...'.format(self.username))
		# Creates a Firefox webdriver object and load it using our options
		driver = webdriver.Firefox(options=options)
		driver.get(self.url)
		# A short delay for complete page render, increase for slower internet connections
		sleep(3)
		# To-do: Except each related settings individually for more specific instructions
		try:
			self.data['name'] = driver.find_element_by_css_selector("p.text-center:nth-child(5)").text
		except:
			print('FETCH_FAILED: name')

		try:
			self.data['bio'] = driver.find_element_by_css_selector(".bio").text
		except:
			print('FETCH_FAILED: bio')
		
		try:
			if len(self.data) == 2:
				self.data['points'] = driver.find_element_by_css_selector("p.text-center:nth-child(8)").text
			elif len(self.data) == 1:
				self.data['points'] = driver.find_element_by_css_selector("p.text-center:nth-child(7)").text
			else:
				self.data['points'] = driver.find_element_by_css_selector("p.text-center:nth-child(6)").text
		except:
			print('FETCH_FAILED: points')

		try:
			self.data['longest_streak'] = driver.find_element_by_css_selector("span.streak:nth-child(1)").text.split(":")[1].strip()
			self.data['current_streak'] = driver.find_element_by_css_selector("span.streak:nth-child(2)").text.split(":")[1].strip()
		except:
			print('FETCH_FAILED: longest_streak, current_streak')

		try:
			recent_activity = []
			for i in range(3):
				a = {}
				a['challenge'] = driver.find_element_by_css_selector("tr.timeline-row:nth-child({}) > td:nth-child(1) > a:nth-child(1)".format(i+1)).text
				a['date'] = driver.find_element_by_css_selector("tr.timeline-row:nth-child({}) > td:nth-child(2) > time:nth-child(1)".format(i+1)).text
				recent_activity.append(a)
			self.data['recent_activity'] = recent_activity
			self.data['last_activity'] = recent_activity[0]
			self.data['last_time_active'] = recent_activity[0]['date']
		except:
			print('FETCH_FAILED: recent_activity, last_activity, last_time_active')
		else:
			print(FETCH_SUCCESS)
		finally:
			print("Fetching complete, returning records.")
		
		driver.quit()
		del driver

	def print_all_data(self):
		intro = 'freeCodeCamp stats for @' + self.username
		print(intro)
		print(len(intro) * '-')
		# NAME
		try:
			print('Full name:', self.data['name'])
		except KeyError:
			print(DATA_NOT_FOUND, '"name"')
		# BIO
		try:
			print('Bio:', self.data['bio'])
		except KeyError:
			print(DATA_NOT_FOUND, '"bio"')
		# POINTS
		try:
			print('Points:', self.data['points'])
		except KeyError:
			print(DATA_NOT_FOUND, '"points"')
		# STREAKS
		try:
			print('Longest streak:', self.data['longest_streak'])
			print('Current streak:', self.data['current_streak'])
		except KeyError:
			print(DATA_NOT_FOUND, '"longest_streak", "current_streak"')
		# ACTIVITY
		try:
			print('Last activity: "{}" on {}'.format(self.data['last_activity']['challenge'], self.data['last_activity']['date']))
		except KeyError:
			print(DATA_NOT_FOUND, '"last_activity"')

		# SEPARATOR
		print('-' * 50)

if __name__ == '__main__':

	adham = UserProgress('aelmosalamy')
	moha = UserProgress('moha09')

	adham.fetch_data()
	moha.fetch_data()

	input('Press Enter to proceed...')

	adham.print_all_data()
	moha.print_all_data()