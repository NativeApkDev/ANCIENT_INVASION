import glob
import unittest
from unittest.mock import patch
from ancient_invasion import *


class MyTestCase(unittest.TestCase):
    ################################################################################################################
    # Tests for user input to ensure that the game does not crash when the user input sequences as in the tests
    # below are entered
    @patch("ancient_invasion.input")
    def test_input_main_01(self, mocked_input):
        mocked_input.side_effect = ["player 1", "player 1", "N"]
        self.assertEquals(main(), 0)

    @patch("ancient_invasion.input")
    def test_input_main_02(self, mocked_input):
        mocked_input.side_effect = ["player 2", "player 2", "Y", "BUY ITEM", 53, "Y", "SUMMON LEGENDARY CREATURE",
                                    "N"]
        self.assertEquals(main(), 0)

    @patch("ancient_invasion.input")
    def test_input_main_03(self, mocked_input):
        mocked_input.side_effect = ["player 3", "player 3", "Y", "VIEW STATS", "N"]
        self.assertEquals(main(), 0)

    @patch("ancient_invasion.input")
    def test_input_main_04(self, mocked_input):
        mocked_input.side_effect = ["player 4", "player 4", "Y", "BUY ITEM", 1, "N"]
        self.assertEquals(main(), 0)

    @patch("ancient_invasion.input")
    def test_input_main_05(self, mocked_input):
        mocked_input.side_effect = ["player 5", "player 5", "Y", "BUY ITEM", 1, "Y", "BUY ITEM", 2, "N"]
        self.assertEquals(main(), 0)

    @patch("ancient_invasion.input")
    def test_input_main_06(self, mocked_input):
        mocked_input.side_effect = ["player 6", "player 6", "Y", "MANAGE PLAYER BASE", "N", 1, "BUILD BUILDING",
                                    0, 0, 12, "N"]
        self.assertEquals(main(), 0)

    @patch("ancient_invasion.input")
    def test_input_main_07(self, mocked_input):
        mocked_input.side_effect = ["player 7", "player 7", "Y", "MANAGE PLAYER BASE", "N", 1, "BUILD BUILDING",
                                    0, 0, 12, "Y", "BUY ITEM", 53, "Y", "SUMMON LEGENDARY CREATURE", 1, 1, "N"]
        self.assertEquals(main(), 0)

    @patch("ancient_invasion.input")
    def test_input_main_08(self, mocked_input):
        mocked_input.side_effect = ["player 8", "player 8", "Y", "MANAGE PLAYER BASE", "N", 1, "BUILD BUILDING",
                                    0, 0, 12, "Y", "BUY ITEM", 53, "N"]
        self.assertEquals(main(), 0)

    @patch("ancient_invasion.input")
    def test_input_main_09(self, mocked_input):
        mocked_input.side_effect = ["player 9", "player 9", "Y", "MANAGE PLAYER BASE", "N", 1, "BUILD BUILDING",
                                    0, 0, 12, "Y", "BUY ITEM", 53, "Y", "SUMMON LEGENDARY CREATURE", 1, 1, "Y",
                                    "BUY ITEM", 1, "Y", "BUY ITEM", 2, "Y", "PLACE RUNE", 1, "Y", 1, "Y",
                                    "PLACE RUNE", 1, "Y", 1, "N"]
        self.assertEquals(main(), 0)

    @patch("ancient_invasion.input")
    def test_input_main_10(self, mocked_input):
        mocked_input.side_effect = ["player 10", "player 10", "Y", "MANAGE PLAYER BASE", "N", 1, "BUILD BUILDING",
                                    0, 0, 12, "Y", "BUY ITEM", 53, "Y", "SUMMON LEGENDARY CREATURE", 1, 1, "Y",
                                    "BUY ITEM", 1, "Y", "BUY ITEM", 2, "Y", "PLACE RUNE", 1, "Y", 1, "Y",
                                    "PLACE RUNE", 1, "Y", 1, "Y", "REMOVE RUNE", 1, 2, "N"]
        self.assertEquals(main(), 0)

    @patch("ancient_invasion.input")
    def test_input_main_11(self, mocked_input):
        mocked_input.side_effect = ["player 11", "player 11", "Y", "MANAGE PLAYER BASE", "N", 1, "BUILD BUILDING",
                                    0, 0, 12, "Y", "BUY ITEM", 53, "Y", "SUMMON LEGENDARY CREATURE", 1, 1, "Y",
                                    "BUY ITEM", 1, "Y", "BUY ITEM", 2, "Y", "PLACE RUNE", 1, "Y", 1, "Y",
                                    "PLACE RUNE", 1, "Y", 1, "Y", "MANAGE BATTLE TEAM", "Y", 1, "N"]
        self.assertEquals(main(), 0)

    @patch("ancient_invasion.input")
    def test_input_main_12(self, mocked_input):
        mocked_input.side_effect = ["player 12", "player 12", "Y", "MANAGE PLAYER BASE", "N", 1, "BUILD BUILDING",
                                    0, 0, 12, "Y", "BUY ITEM", 53, "Y", "SUMMON LEGENDARY CREATURE", 1, 1, "Y",
                                    "BUY ITEM", 1, "Y", "BUY ITEM", 2, "Y", "PLACE RUNE", 1, "Y", 1, "Y",
                                    "PLACE RUNE", 1, "Y", 1, "Y", "MANAGE LEGENDARY CREATURE INVENTORY", 1, "N"]
        self.assertEquals(main(), 0)

    @patch("ancient_invasion.input")
    def test_input_main_13(self, mocked_input):
        mocked_input.side_effect = ["player 13", "player 13", "Y", "MANAGE PLAYER BASE", "N", 1, "BUILD BUILDING",
                                    0, 0, 12, "Y", "BUY ITEM", 53, "Y", "SUMMON LEGENDARY CREATURE", 1, 1, "Y",
                                    "BUY ITEM", 1, "Y", "BUY ITEM", 2, "Y", "PLACE RUNE", 1, "Y", 1, "Y",
                                    "MANAGE ITEM INVENTORY", "Y", 2, "Y", 1, "N"]
        self.assertEquals(main(), 0)

    @patch("ancient_invasion.input")
    def test_input_main_14(self, mocked_input):
        mocked_input.side_effect = ["player 14", "player 14", "Y", "MANAGE PLAYER BASE", "N", 1, "BUILD BUILDING",
                                    0, 0, 14, "Y", "MAKE A WISH", 1, "N"]
        self.assertEquals(main(), 0)

    ################################################################################################################
    # Tests in loading users' data from the newly saved files to check whether correct data is represented or not
    def test_load_user_01(self):
        user1_data: Game = load_game_data("SAVED ANCIENT INVASION GAME DATA - PLAYER 1")
        user1: Player = user1_data.player_data
        self.assertEquals(user1.name, "player 1")
        self.assertEquals(user1.level, 1)
        self.assertEquals(len(user1.item_inventory.get_items()), 0)

    def test_load_user_02(self):
        user2_data: Game = load_game_data("SAVED ANCIENT INVASION GAME DATA - PLAYER 2")
        user2: Player = user2_data.player_data
        self.assertEquals(user2.name, "player 2")
        self.assertEquals(user2.level, 1)
        self.assertEquals(len(user2.item_inventory.get_items()), 1)

    def test_load_user_03(self):
        user3_data: Game = load_game_data("SAVED ANCIENT INVASION GAME DATA - PLAYER 3")
        user3: Player = user3_data.player_data
        self.assertEquals(user3.name, "player 3")
        self.assertEquals(user3.level, 1)
        self.assertEquals(len(user3.item_inventory.get_items()), 0)

    def test_load_user_04(self):
        user4_data: Game = load_game_data("SAVED ANCIENT INVASION GAME DATA - PLAYER 4")
        user4: Player = user4_data.player_data
        self.assertEquals(user4.name, "player 4")
        self.assertEquals(user4.level, 1)
        self.assertEquals(len(user4.item_inventory.get_items()), 1)

    def test_load_user_05(self):
        user5_data: Game = load_game_data("SAVED ANCIENT INVASION GAME DATA - PLAYER 5")
        user5: Player = user5_data.player_data
        self.assertEquals(user5.name, "player 5")
        self.assertEquals(user5.level, 1)
        self.assertEquals(len(user5.item_inventory.get_items()), 2)

    def test_load_user_06(self):
        user6_data: Game = load_game_data("SAVED ANCIENT INVASION GAME DATA - PLAYER 6")
        user6: Player = user6_data.player_data
        self.assertEquals(user6.name, "player 6")
        self.assertEquals(user6.level, 1)
        self.assertEquals(user6.gold, 4900000)
        self.assertEquals(len(user6.item_inventory.get_items()), 0)
        self.assertTrue(isinstance(user6.player_base.get_islands()[0].get_tile_at(0, 0).building, Summonhenge))
        self.assertEquals(user6.gold_per_second, 0)
        self.assertEquals(len(user6.legendary_creature_inventory.get_legendary_creatures()), 0)

    def test_load_user_07(self):
        user7_data: Game = load_game_data("SAVED ANCIENT INVASION GAME DATA - PLAYER 7")
        user7: Player = user7_data.player_data
        self.assertEquals(user7.name, "player 7")
        self.assertEquals(user7.level, 1)
        self.assertEquals(user7.gold, 3900000)
        self.assertEquals(len(user7.item_inventory.get_items()), 0)
        self.assertTrue(isinstance(user7.player_base.get_islands()[0].get_tile_at(0, 0).building, Summonhenge))
        self.assertEquals(user7.gold_per_second, 0)
        self.assertEquals(len(user7.legendary_creature_inventory.get_legendary_creatures()), 1)

    def test_load_user_08(self):
        user8_data: Game = load_game_data("SAVED ANCIENT INVASION GAME DATA - PLAYER 8")
        user8: Player = user8_data.player_data
        self.assertEquals(user8.name, "player 8")
        self.assertEquals(user8.level, 1)
        self.assertEquals(user8.gold, 3900000)
        self.assertEquals(len(user8.item_inventory.get_items()), 1)
        self.assertTrue(isinstance(user8.player_base.get_islands()[0].get_tile_at(0, 0).building, Summonhenge))
        self.assertEquals(user8.gold_per_second, 0)
        self.assertEquals(len(user8.legendary_creature_inventory.get_legendary_creatures()), 0)

    def test_load_user_09(self):
        user9_data: Game = load_game_data("SAVED ANCIENT INVASION GAME DATA - PLAYER 9")
        user9: Player = user9_data.player_data
        self.assertEquals(user9.name, "player 9")
        self.assertEquals(user9.level, 1)
        self.assertEquals(user9.gold, 1900000)
        self.assertEquals(len(user9.item_inventory.get_items()), 2)
        self.assertTrue(isinstance(user9.player_base.get_islands()[0].get_tile_at(0, 0).building, Summonhenge))
        self.assertEquals(user9.gold_per_second, 0)
        self.assertEquals(len(user9.legendary_creature_inventory.get_legendary_creatures()), 1)
        self.assertEquals(len(user9.legendary_creature_inventory.get_legendary_creatures()[0].get_runes().values()), 2)

    def test_load_user_10(self):
        user10_data: Game = load_game_data("SAVED ANCIENT INVASION GAME DATA - PLAYER 10")
        user10: Player = user10_data.player_data
        self.assertEquals(user10.name, "player 10")
        self.assertEquals(user10.level, 1)
        self.assertEquals(user10.gold, 1900000)
        self.assertEquals(len(user10.item_inventory.get_items()), 2)
        self.assertTrue(isinstance(user10.player_base.get_islands()[0].get_tile_at(0, 0).building, Summonhenge))
        self.assertEquals(user10.gold_per_second, 0)
        self.assertEquals(len(user10.legendary_creature_inventory.get_legendary_creatures()), 1)
        self.assertEquals(len(user10.legendary_creature_inventory.get_legendary_creatures()[0].get_runes().values()), 1)

    def test_load_user_11(self):
        user11_data: Game = load_game_data("SAVED ANCIENT INVASION GAME DATA - PLAYER 11")
        user11: Player = user11_data.player_data
        self.assertEquals(user11.name, "player 11")
        self.assertEquals(user11.level, 1)
        self.assertEquals(user11.gold, 1900000)
        self.assertEquals(len(user11.item_inventory.get_items()), 2)
        self.assertTrue(isinstance(user11.player_base.get_islands()[0].get_tile_at(0, 0).building, Summonhenge))
        self.assertEquals(user11.gold_per_second, 0)
        self.assertEquals(len(user11.legendary_creature_inventory.get_legendary_creatures()), 1)
        self.assertEquals(len(user11.legendary_creature_inventory.get_legendary_creatures()[0].get_runes().values()), 2)
        self.assertEquals(len(user11.battle_team.get_legendary_creatures()), 1)

    def test_load_user_12(self):
        user12_data: Game = load_game_data("SAVED ANCIENT INVASION GAME DATA - PLAYER 12")
        user12: Player = user12_data.player_data
        self.assertEquals(user12.name, "player 12")
        self.assertEquals(user12.level, 1)
        self.assertEquals(user12.gold, 1900000)
        self.assertEquals(len(user12.item_inventory.get_items()), 2)
        self.assertTrue(isinstance(user12.player_base.get_islands()[0].get_tile_at(0, 0).building, Summonhenge))
        self.assertEquals(user12.gold_per_second, 0)
        self.assertEquals(len(user12.legendary_creature_inventory.get_legendary_creatures()), 0)

    def test_load_user_13(self):
        user13_data: Game = load_game_data("SAVED ANCIENT INVASION GAME DATA - PLAYER 13")
        user13: Player = user13_data.player_data
        self.assertEquals(user13.name, "player 13")
        self.assertEquals(user13.level, 1)
        self.assertEquals(user13.gold, 1100000)
        self.assertEquals(len(user13.item_inventory.get_items()), 1)
        self.assertTrue(isinstance(user13.player_base.get_islands()[0].get_tile_at(0, 0).building, Summonhenge))
        self.assertEquals(user13.gold_per_second, 0)
        self.assertEquals(user13.item_inventory.get_items()[0].level, 2)
        self.assertEquals(len(user13.legendary_creature_inventory.get_legendary_creatures()), 1)
        self.assertEquals(len(user13.legendary_creature_inventory.get_legendary_creatures()[0].get_runes().values()), 1)

    def test_load_user_14(self):
        user14_data: Game = load_game_data("SAVED ANCIENT INVASION GAME DATA - PLAYER 14")
        user14: Player = user14_data.player_data
        self.assertEquals(user14.name, "player 14")
        condition1: bool = user14.level == 1 or user14.level == 2
        condition2: bool = user14.exp >= 0 or user14.gold >= 0 or user14.gems >= 0
        condition3: bool = len(user14.item_inventory.get_items()) > 0
        self.assertTrue(condition1 or condition2 or condition3)

    ################################################################################################################
    # Checking whether the number of saved data files is correct or not
    def test_number_of_files(self):
        self.assertEquals(len([filename for filename in os.listdir(".") if filename[0:5] == "SAVED"]), 14)

    ################################################################################################################
    # Delete all the created files with "SAVED DATA" in their name from the directory "ANCIENT_INVASION" in the
    # project after test execution is complete. This is to ensure that all other test cases pass
    def test_remove_all_files(self):
        for f in os.listdir("."):
            if f[0:5] == "SAVED":
                os.remove(f)


if __name__ == '__main__':
    unittest.main()
