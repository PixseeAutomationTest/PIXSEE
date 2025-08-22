import unittest
from htmltestreport import HTMLTestReport
from datetime import datetime

from tests.login_test import LoginCase
from tests.user_profile_test import UserProfileTest
from tests.add_baby_test import AddBabyTest
from tests.edit_baby_test import EditBabyTestWithAdding, EditBabyTestWithoutAdding
from tests.pixsee_settings_test import PixseeSettingsTest
from tests.pixsee_settings_tests.pixsee_profile_test import PixseeProfileTest
from tests.pixsee_settings_tests.wifi_settings_test import WifiSettingsCase1, WifiSettingsCase2, WifiSettingsCase3
from tests.pixsee_settings_tests.pixsee_friends_detection_test import PixseeFriendsDetectionCase1, PixseeFriendsDetectionCase2
from tests.pixsee_settings_tests.environment_settings_test import EnvironmentSettingsCase1, EnvironmentSettingsCase2
from tests.pixsee_settings_tests.cry_detection_test import CryDetectionCase1, CryDetectionCase2
from tests.pixsee_settings_tests.area_detection_tests.area_detection_reset_test import AreaDetectionCase1
from tests.pixsee_settings_tests.area_detection_tests.area_detection_no_reset_test import AreaDetectionCase2, AreaDetectionCase3
from tests.pixsee_settings_tests.covered_face_detection_tests.covered_face_detection_reset_test import CoveredFaceDetectionCase1
from tests.pixsee_settings_tests.covered_face_detection_tests.covered_face_detection_no_reset_test import CoveredFaceDetectionCase2, CoveredFaceDetectionCase3
from tests.pixsee_settings_tests.time_lapse_video_test import TimeLapseVideoCase1, TimeLapseVideoCase2,TimeLapseVideoCase3
from tests.pixsee_settings_tests.voice_service_test import VoiceServiceTest
from tests.pixsee_settings_tests.SD_card_test import SDcardCase
from tests.about_test import AboutTest
from tests.new_photo_check_test import NewPhotoCheckCase
from tests.subscription_tests.havent_subscription_test import SubscriptionCase1
from tests.subscription_tests.already_subscription_test import SubscriptionCase2
from tests.assistant_tests.assistant_test import AssistantTest
from tests.assistant_tests.pixsee_cloud_test import PixseeCloudTest1, PixseeCloudTest2
from tests.baby_care_test import BabyCareCase
from tests.tutor_test import TutorCase


def make_test_class(testcase, language, locale):
    class CustomTestCase(testcase):
        def __init__(self, methodName='runTest'):
            super().__init__(methodName, language=language, locale=locale)

    CustomTestCase.__name__ = testcase.__name__
    CustomTestCase.__qualname__ = testcase.__qualname__
    return CustomTestCase

if __name__ == '__main__':
    language = ["en", "zh", "zh"]
    locale = ["US", "TW", "CN"]
    for i in range(len(language)):
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        # Include all test cases in the suite
        suite.addTest(loader.loadTestsFromTestCase(make_test_class(UserProfileTest, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(AddBabyTest, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(EditBabyTestWithAdding, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(EditBabyTestWithoutAdding, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(PixseeProfileTest, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(VoiceServiceTest, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(AboutTest, language[i], locale[i])))

        suite.addTests(loader.loadTestsFromTestCase(make_test_class(LoginCase, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(TutorCase, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(BabyCareCase, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(NewPhotoCheckCase, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(AreaDetectionCase1, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(AreaDetectionCase2, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(AreaDetectionCase3, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(WifiSettingsCase1, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(WifiSettingsCase2, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(WifiSettingsCase3, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(PixseeFriendsDetectionCase1, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(PixseeFriendsDetectionCase2, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(CoveredFaceDetectionCase1, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(CoveredFaceDetectionCase2, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(CoveredFaceDetectionCase3, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(EnvironmentSettingsCase1, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(EnvironmentSettingsCase2, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(CryDetectionCase1, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(CryDetectionCase2, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(SDcardCase, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(SubscriptionCase1, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(PixseeCloudTest1, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(PixseeCloudTest2, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(TimeLapseVideoCase1, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(TimeLapseVideoCase2, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(TimeLapseVideoCase3, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(SubscriptionCase2, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(PixseeSettingsTest, language[i], locale[i])))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(AssistantTest, language[i], locale[i])))

        # Run the test suite
        date_str = datetime.now().strftime("%Y%m%d")
        runner = HTMLTestReport(f"./results/{language[i]}-{locale[i]}/{date_str}.html", title=f"Pixsee Test Results ({language[i]}-{locale[i]})")
        runner.run(suite)
