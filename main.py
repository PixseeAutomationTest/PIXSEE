import unittest
from htmltestreport import HTMLTestReport

from tests.login_test import LoginCase
from tests.add_baby_test import AddBabyTest
from tests.edit_baby_test import EditBabyTestWithAdding
from tests.edit_baby_test import EditBabyTestWithoutAdding
from tests.pixsee_settings_test import PixseeSettingsTest
from tests.pixsee_settings_tests.pixsee_profile_test import PixseeProfileTest
from tests.pixsee_settings_tests.wifi_settings_test import WifiSettingsCase
from tests.pixsee_settings_tests.pixsee_friends_detection_test import PixseeFriendsDetectionCase
from tests.pixsee_settings_tests.environment_settings_test import EnvironmentSettingsCase
from tests.pixsee_settings_tests.cry_detection_test import CryDetectionCase
from tests.pixsee_settings_tests.area_detection_tests.area_detection_reset_test import AreaDetectionCase1
from tests.pixsee_settings_tests.area_detection_tests.area_detection_no_reset_test import AreaDetectionCase2
from tests.pixsee_settings_tests.covered_face_detection_tests.covered_face_detection_reset_test import CoveredFaceDetectionCase1
from tests.pixsee_settings_tests.covered_face_detection_tests.covered_face_detection_no_reset_test import CoveredFaceDetectionCase2
from tests.pixsee_settings_tests.time_lapse_video_test import TimeLapseVideoCase
from tests.pixsee_settings_tests.voice_service_test import VoiceServiceTest
from tests.pixsee_settings_tests.SD_card_test import SDcardCase
from tests.about_test import AboutTest
from tests.new_photo_check_test import NewPhotoCheckCase
from tests.subscription_tests.havent_subscription_test import SubscriptionCase1
from tests.subscription_tests.already_subscription_test import SubscriptionCase2
from tests.assistant_tests.assistant_test import AssistantTest
from tests.assistant_tests.pixsee_cloud_test import PixseeCloudTest


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Include all test cases in the suite
    suite.addTests(loader.loadTestsFromTestCase(AddBabyTest))
    suite.addTests(loader.loadTestsFromTestCase(EditBabyTestWithAdding))
    suite.addTests(loader.loadTestsFromTestCase(EditBabyTestWithoutAdding))
    suite.addTests(loader.loadTestsFromTestCase(PixseeProfileTest))
    suite.addTests(loader.loadTestsFromTestCase(VoiceServiceTest))
    suite.addTests(loader.loadTestsFromTestCase(AboutTest))

    suite.addTests(loader.loadTestsFromTestCase(LoginCase))
    suite.addTests(loader.loadTestsFromTestCase(AreaDetectionCase1))
    suite.addTests(loader.loadTestsFromTestCase(AreaDetectionCase2))
    suite.addTests(loader.loadTestsFromTestCase(NewPhotoCheckCase))
    suite.addTests(loader.loadTestsFromTestCase(WifiSettingsCase))
    suite.addTests(loader.loadTestsFromTestCase(PixseeFriendsDetectionCase))
    suite.addTests(loader.loadTestsFromTestCase(CoveredFaceDetectionCase1))
    suite.addTests(loader.loadTestsFromTestCase(CoveredFaceDetectionCase2))
    suite.addTests(loader.loadTestsFromTestCase(EnvironmentSettingsCase))
    suite.addTests(loader.loadTestsFromTestCase(CryDetectionCase))
    suite.addTests(loader.loadTestsFromTestCase(SDcardCase))
    suite.addTests(loader.loadTestsFromTestCase(SubscriptionCase1))
    suite.addTests(loader.loadTestsFromTestCase(PixseeCloudTest))
    suite.addTests(loader.loadTestsFromTestCase(TimeLapseVideoCase))
    suite.addTests(loader.loadTestsFromTestCase(SubscriptionCase2))
    suite.addTests(loader.loadTestsFromTestCase(PixseeSettingsTest))
    suite.addTests(loader.loadTestsFromTestCase(AssistantTest))


    # Run the test suite
    runner = HTMLTestReport("results/chinese/20250812-2.html", title="Pixsee Test Results")
    runner.run(suite)