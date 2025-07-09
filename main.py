import unittest
from test.familyPhoto import FamilyAlbumCase

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # 新增測試項目
    suite.addTests(loader.loadTestsFromTestCase(FamilyAlbumCase))
    # 執行測試項目
    unittest.TextTestRunner(verbosity=2).run(suite)