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
from tests.pixsee_settings_tests.time_lapse_video_test import TimeLapseVideoCase1
from tests.pixsee_settings_tests.voice_service_test import VoiceServiceTest
from tests.pixsee_settings_tests.SD_card_test import SDcardCase
from tests.about_test import AboutTest
from tests.new_photo_check_test import NewPhotoCheckCase
from tests.subscription_tests.havent_subscription_test import SubscriptionCase1
from tests.assistant_tests.assistant_test import AssistantTest
from tests.assistant_tests.pixsee_cloud_test import PixseeCloudTest1, PixseeCloudTest2
from tests.baby_care_test import BabyCareCase
from tests.tutor_test import TutorCase


def make_test_class(testcase, language, locale):
    class CustomTestCase(testcase):
        @classmethod
        def setUpClass(cls):
            cls.language = language
            cls.locale = locale
            super().setUpClass()

    CustomTestCase.__name__ = f"{testcase.__name__}_{language}_{locale}"
    return CustomTestCase

if __name__ == '__main__':
    languages = ["en"]
    locales = ["US"]
    languages += ["zh", "zh"]
    locales += ["TW", "CN"]

    for lang, loc in zip(languages, locales):
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()

        suite.addTests(loader.loadTestsFromTestCase(make_test_class(LoginCase, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(TutorCase, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(BabyCareCase, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(UserProfileTest, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(AddBabyTest, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(EditBabyTestWithAdding, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(EditBabyTestWithoutAdding, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(NewPhotoCheckCase, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(PixseeProfileTest, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(WifiSettingsCase1, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(WifiSettingsCase2, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(WifiSettingsCase3, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(PixseeFriendsDetectionCase1, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(PixseeFriendsDetectionCase2, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(CryDetectionCase1, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(CryDetectionCase2, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(EnvironmentSettingsCase1, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(EnvironmentSettingsCase2, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(VoiceServiceTest, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(SDcardCase, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(AreaDetectionCase1, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(AreaDetectionCase2, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(AreaDetectionCase3, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(CoveredFaceDetectionCase1, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(CoveredFaceDetectionCase2, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(CoveredFaceDetectionCase3, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(SubscriptionCase1, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(PixseeCloudTest1, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(PixseeCloudTest2, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(TimeLapseVideoCase1, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(PixseeSettingsTest, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(AssistantTest, lang, loc)))
        suite.addTests(loader.loadTestsFromTestCase(make_test_class(AboutTest, lang, loc)))

        date_str = datetime.now().strftime("%Y%m%d")
        runner = HTMLTestReport(
            f"./results/{lang}-{loc}/{date_str}(unsub).html",
            title=f"Pixsee Test Results (unsub)({lang}-{loc})"
        )
        runner.run(suite)
