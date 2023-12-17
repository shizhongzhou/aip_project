import unittest
from five_pieces import ai_play, check

class TestFiveInRow(unittest.TestCase):

    def setUp(self):
        # 初始化测试所需的环境或数据
        self.board = [[0 for _ in range(19)] for _ in range(19)]

    def test_ai_play(self):
        # 测试AI下棋功能

        result = ai_play(self.board)
        self.assertIsNotNone(result)  # 检查AI是否成功下棋并返回有效的结果

    def test_check_win(self):
        # 测试检查胜利条件功能
        # 设置一个五子连珠的情况
        for i in range(5):
            self.board[0][i] = 1

        # 检查是否检测到胜利
        self.assertTrue(check(0, 2, "black", self.board))



if __name__ == '__main__':
    unittest.main()
