import unittest
from htmltestreport import HTMLTestReport
from datetime import datetime

from tests.pixsee_settings_tests.time_lapse_video_test import TimeLapseVideoCase2,TimeLapseVideoCase3
from tests.subscription_tests.already_subscription_test import SubscriptionCase2
from tests.assistant_tests.pixsee_cloud_after_sub_test import PixseeCloudTest3, PixseeCloudTest4


def make_test_class(testcase, language, locale):
	class CustomTestCase(testcase):
		@classmethod
		def setUpClass(cls):
			cls.language = language
			cls.locale = locale
			super().setUpClass()

	CustomTestCase.__name__ = testcase.__name__
	CustomTestCase.__qualname__ = testcase.__qualname__
	return CustomTestCase

if __name__ == '__main__':
	languages = ["en"]
	locales = ["US"]
	languages += ["zh", "zh"]
	locales += ["TW", "CN"]

	for lang, loc in zip(languages, locales):
		loader = unittest.TestLoader()
		suite = unittest.TestSuite()

		suite.addTests(loader.loadTestsFromTestCase(make_test_class(TimeLapseVideoCase2, lang, loc)))
		suite.addTests(loader.loadTestsFromTestCase(make_test_class(TimeLapseVideoCase3, lang, loc)))
		suite.addTests(loader.loadTestsFromTestCase(make_test_class(SubscriptionCase2, lang, loc)))
		suite.addTests(loader.loadTestsFromTestCase(make_test_class(PixseeCloudTest3, lang, loc)))
		suite.addTests(loader.loadTestsFromTestCase(make_test_class(PixseeCloudTest4, lang, loc)))

		date_str = datetime.now().strftime("%Y%m%d")
		runner = HTMLTestReport(
			f"./results/{lang}-{loc}/{date_str}(subscription).html",
			title=f"Pixsee Test Results (Subscription)({lang}-{loc})"
		)
		runner.run(suite)