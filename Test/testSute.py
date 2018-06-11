import unittest


class UCTestCase(unittest.TestCase):
    def setUp(self):
        # 测试前需执行的操作
        print("setUp")

    def tearDown(self):
        # 测试用例执行完后所需执行的操作
        print("tearDown")

    # 测试用例1
    def testCreateFolder(self):
        # 具体的测试脚本
        print("testCreateFolder")
        # 测试用例2

    def testDeleteFolder(self):
        # 具体的测试脚本
        print("testDeleteFolder")


if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(UCTestCase("testCreateFolder"))
    #suite.addTest(UCTestCase("testCreateFolder"))
    # 执行测试
    runner = unittest.TextTestRunner()
    re=runner.run(suite)