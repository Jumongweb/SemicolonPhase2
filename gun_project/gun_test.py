import unittest
from gun import Gun
from SemicolonPhase2.gun_project import gun


class MyTestCase(unittest.TestCase):
    def test_ThatMyGunChamberIsEmpty(self):
        my_gun: gun = Gun()
        self.assertEqual(0, my_gun.getChamber())

    def test_ThatMyGunCanAddBullet(self):
        my_gun: gun = Gun()
        my_gun.add_bullet()
        self.assertEqual(1, my_gun.getChamber())

    def test_ThatMyGunCannotTakeMoreThan40Bullet(self):
        my_gun: gun = Gun()
        self.assertEqual(0, my_gun.getChamber())
        for _ in range(40):
            my_gun.add_bullet()
        self.assertEqual(40, my_gun.getChamber())
        my_gun.add_bullet()
        self.assertEqual(40, my_gun.getChamber())

    def test_ThatMyGunCanBeLoadedWith40BulletAtOne(self):
        my_gun: gun = Gun()
        my_gun.load_bullet()
        self.assertEqual(40, my_gun.getChamber())

    def test_ThatMyGunCanShoot(self):
        my_gun: gun = Gun()
        my_gun.load_bullet()
        self.assertEqual(40, my_gun.getChamber())
        my_gun.shoot()
        self.assertEqual(39, my_gun.getChamber())

    def test_loadAndFireThreeTimesTheRemainingBulletIs37(self):
        my_gun: gun = Gun()
        my_gun.load_bullet()
        self.assertEqual(40, my_gun.getChamber())
        my_gun.shoot()
        my_gun.shoot()
        my_gun.shoot()
        self.assertEqual(37, my_gun.getChamber())

    def test_ThatMyGunCannotShootWhenTheChamberIsEmpty(self):
        my_gun: gun = Gun()
        my_gun.shoot()
        self.assertEqual(0, my_gun.getChamber())

    def test_ThatMyGunCanReload(self):
        my_gun: gun = Gun()
        my_gun.load_bullet()
        for _ in range(20): my_gun.shoot()
        self.assertEqual(20, my_gun.getChamber())
        my_gun.reload()
        self.assertEqual(40, my_gun.getChamber())


if __name__ == '__main__':
    unittest.main()
