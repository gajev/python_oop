import unittest
from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Angel", 5, 100, 20)
        self.second_hero = Hero("Gadzhev", 5, 100, 20)

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.hero.username, "Angel")
        self.assertEqual(self.hero.level, 5)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 20)

    def test_battle_with_self(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_negative_health(self):
        self.hero.health = -2
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.second_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_with_negative_health_of_second_hero(self):
        self.second_hero.health = -2
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.second_hero)
        self.assertEqual("You cannot fight Gadzhev. He needs to rest", str(ex.exception))

    def test_damage(self):
        self.hero.battle(self.second_hero)
        self.assertEqual(self.hero.health, 0)
        self.assertEqual(self.second_hero.health, 0)

    def test_draw(self):
        result = self.hero.battle(self.second_hero)
        self.assertEqual(result, "Draw")

    def test_win(self):
        self.third_hero = Hero("Loser", 2, 100, 20)
        result = self.hero.battle(self.third_hero)
        self.assertEqual(self.hero.level, 6)
        self.assertEqual(self.hero.health, 65)
        self.assertEqual(self.hero.damage, 25)
        self.assertEqual(result, "You win")

    def test_lose(self):
        self.last_hero = Hero("Winner", 10, 1000, 20)
        result = self.hero.battle(self.last_hero)
        self.assertEqual(self.last_hero.level, 11)
        self.assertEqual(self.last_hero.health, 905)
        self.assertEqual(self.last_hero.damage, 25)
        self.assertEqual(result, "You lose")

    def test_repr(self):
        result = self.hero.__str__()
        expected_result = f"Hero Angel: 5 lvl\n" \
                          f"Health: 100\n" \
                          f"Damage: 20\n"
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
