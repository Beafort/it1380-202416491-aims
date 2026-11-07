import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class CartOperation(unittest.TestCase):
    
    def setUp(self):
        """Runs before every test method to set up fresh state."""
        self.cart = Cart()

    def test_add_dvd_success(self):
        """Test adding DVDs successfully returns True and updates count."""
        dvd1 = DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95)
        dvd2 = DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 121, 24.95)
        
        # add_dvd should return True when successful
        self.assertTrue(self.cart.add_dvd(dvd1))
        self.assertTrue(self.cart.add_dvd(dvd2))

    def test_add_dvd_capacity_limit(self):
        """Test that adding past 20 DVDs returns False and stops adding."""
        # Fill the cart up to the 20th item
        for i in range(20):
            dvd = DigitalVideoDisc(f"Title {i}", "Category", 10.0)
            added = self.cart.add_dvd(dvd)
            self.assertTrue(added, f"DVD {i+1} should be added successfully.")
        
        # The 21st DVD should exceed the limit and return False
        extra_dvd = DigitalVideoDisc("Extra DVD", "Category", 10.0)
        self.assertFalse(self.cart.add_dvd(extra_dvd))
    def test_twenty_percent_off(self):
      self.cart.add_dvd(DigitalVideoDisc("X", "Animation", cost=100))        
      self.assertTrue(self.cart.apply_discount(20) == 80)

    def test_percent_over_100_raises(self):
        self.cart.add_dvd(DigitalVideoDisc("X", "Animation", cost=100))
        with self.assertRaises(ValueError):
            self.cart.apply_discount(150)

if __name__ == '__main__':
    unittest.main()