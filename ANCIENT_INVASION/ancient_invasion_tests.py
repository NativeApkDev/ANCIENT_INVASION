import unittest
from unittest.mock import patch
from ancient_invasion import *


class MyTestCase(unittest.TestCase):
    ################################################################################################################
    # Tests for user input to ensure that the game does not crash when the user input sequences as in the tests
    # below are entered
    @patch("ancient_invasion.input")
    def test_main_input_01(self, mocked_input):
        mocked_input.side_effect = ["sample user 1", "sample user 1", "N"]
        self.assertEquals(main(), 0)

    @patch("ancient_invasion.input")
    def test_main_input_02(self, mocked_input):
        mocked_input.side_effect = ["i am new", "i am new", "Y"]
        self.assertEquals(main(), 0)

    @patch("ancient_invasion.input")
    def test_main_input_03(self, mocked_input):
        mocked_input.side_effect = ["newbie", "newbie", "Y", "VIEW STATS", "N"]
        self.assertEquals(main(), 0)

    @patch("ancient_invasion.input")
    def test_main_input_04(self, mocked_input):
        mocked_input.side_effect = ["player 1", "player 1", "Y", "BUY ITEM", 1, "N"]
        self.assertEquals(main(), 0)

    @patch("ancient_invasion.input")
    def test_main_input_05(self, mocked_input):
        mocked_input.side_effect = ["player 2", "player 2", "Y", "BUY ITEM", 1, "Y", "BUY ITEM", 2, "N"]
        self.assertEquals(main(), 0)

    ################################################################################################################
    # Tests in loading users' data from the newly saved files to check whether correct data is represented or not
    def test_load_user_01(self):
        user1_data: Game = load_game_data("SAVED_DATA/SAVED ANCIENT INVASION GAME DATA - SAMPLE USER 1")
        user1: Player = user1_data.player_data
        self.assertEquals(user1.name, "sample user 1")
        self.assertEquals(user1.level, 1)
        self.assertEquals(len(user1.item_inventory.get_items()), 0)

    def test_load_user_02(self):
        user2_data: Game = load_game_data("SAVED_DATA/SAVED ANCIENT INVASION GAME DATA - I AM NEW")
        user2: Player = user2_data.player_data
        self.assertEquals(user2.name, "i am new")
        self.assertEquals(user2.level, 1)
        self.assertEquals(len(user2.item_inventory.get_items()), 0)

    def test_load_user_03(self):
        user3_data: Game = load_game_data("SAVED_DATA/SAVED ANCIENT INVASION GAME DATA - NEWBIE")
        user3: Player = user3_data.player_data
        self.assertEquals(user3.name, "newbie")
        self.assertEquals(user3.level, 1)
        self.assertEquals(len(user3.item_inventory.get_items()), 0)

    def test_load_user_04(self):
        user4_data: Game = load_game_data("SAVED_DATA/SAVED ANCIENT INVASION GAME DATA - PLAYER 1")
        user4: Player = user4_data.player_data
        self.assertEquals(user4.name, "player 1")
        self.assertEquals(user4.level, 1)
        self.assertEquals(len(user4.item_inventory.get_items()), 1)

    def test_load_user_05(self):
        user5_data: Game = load_game_data("SAVED_DATA/SAVED ANCIENT INVASION GAME DATA - PLAYER 2")
        user5: Player = user5_data.player_data
        self.assertEquals(user5.name, "player 2")
        self.assertEquals(user5.level, 1)
        self.assertEquals(len(user5.item_inventory.get_items()), 2)

    ################################################################################################################
    # Checking whether the number of saved data files is correct or not
    def test_number_of_files(self):
        self.assertEquals(len(os.listdir("SAVED_DATA")), 5)


if __name__ == '__main__':
    unittest.main()
