import unittest
from tests.pixsee_settings_tests.SD_card_test import SDcardCase

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Include all test cases in the suite
    # suite.addTests(loader.loadTestsFromTestCase(PixseeProfileTest))
    # suite.addTests(loader.loadTestsFromTestCase(VoiceServiceTest))
    # suite.addTests(loader.loadTestsFromTestCase(AboutTest))
    #
    # suite.addTests(loader.loadTestsFromTestCase(LoginCase))
    # suite.addTests(loader.loadTestsFromTestCase(PixseeSettingsTest))
    # suite.addTests(loader.loadTestsFromTestCase(WifiSettingsCase))
    # suite.addTests(loader.loadTestsFromTestCase(PixseeFriendsDetectionCase))
    # suite.addTests(loader.loadTestsFromTestCase(EnvironmentSettingsCase))
    # suite.addTests(loader.loadTestsFromTestCase(CryDetectionCase))
    # suite.addTests(loader.loadTestsFromTestCase(AreaDetectionCase))
    # suite.addTests(loader.loadTestsFromTestCase(CoveredFaceDetectionCase))
    # suite.addTests(loader.loadTestsFromTestCase(TimeLapseVideoCase))
    suite.addTests(loader.loadTestsFromTestCase(SDcardCase))
    # Run the test suite
    unittest.TextTestRunner(verbosity=2).run(suite)