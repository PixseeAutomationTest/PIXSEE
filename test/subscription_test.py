# check popup dialog
try:
	self.assertTrue(subscription_page.is_in_prize_plan_dialog())
	print("gold star button works, in prize plan dialog")
except AssertionError:
	print("gold star button not works, not in prize plan dialog")
	raise AssertionError("Not in prize plan dialog")
