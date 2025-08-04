import unittest
from tests.login_test import LoginCase
from tests.pixsee_settings_test import PixseeSettingsTest
from tests.pixsee_settings_tests.pixsee_profile_test import PixseeProfileTest
from tests.pixsee_settings_tests.wifi_settings_test import WifiSettingsCase
from tests.pixsee_settings_tests.pixsee_friends_detection_test import PixseeFriendsDetectionCase
from tests.pixsee_settings_tests.environment_settings_test import EnvironmentSettingsCase
from tests.pixsee_settings_tests.cry_detection_test import CryDetectionCase
from tests.pixsee_settings_tests.area_detection_test import AreaDetectionCase
from tests.pixsee_settings_tests.covered_face_detection_test import CoveredFaceDetectionCase
from tests.pixsee_settings_tests.time_lapse_video_test import TimeLapseVideoCase
from tests.pixsee_settings_tests.voice_service_test import VoiceServiceTest
from tests.pixsee_settings_tests.SD_card_test import SDcardCase
from tests.about_test import AboutTest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Include all test cases in the suite
    suite.addTests(loader.loadTestsFromTestCase(PixseeProfileTest))
    suite.addTests(loader.loadTestsFromTestCase(VoiceServiceTest))
    suite.addTests(loader.loadTestsFromTestCase(AboutTest))

    suite.addTests(loader.loadTestsFromTestCase(LoginCase))
    suite.addTests(loader.loadTestsFromTestCase(PixseeSettingsTest))
    suite.addTests(loader.loadTestsFromTestCase(WifiSettingsCase))
    suite.addTests(loader.loadTestsFromTestCase(PixseeFriendsDetectionCase))
    suite.addTests(loader.loadTestsFromTestCase(EnvironmentSettingsCase))
    suite.addTests(loader.loadTestsFromTestCase(CryDetectionCase))
    suite.addTests(loader.loadTestsFromTestCase(AreaDetectionCase))
    suite.addTests(loader.loadTestsFromTestCase(CoveredFaceDetectionCase))
    suite.addTests(loader.loadTestsFromTestCase(TimeLapseVideoCase))
    suite.addTests(loader.loadTestsFromTestCase(SDcardCase))
    # Run the test suite
    unittest.TextTestRunner(verbosity=2).run(suite)