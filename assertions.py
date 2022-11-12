assertEqual ("Selenium Python", "Selenium Python", "Comparison Done")
self.assertEqual(title1, "Yandex3", "not equal")

assertNotEqual ("Selenium", "Selenium Python", "Comparison Done")

assertTrue ( "2 > 1", "Comparison Done")

assertFalse ( "1 > 2", "Comparison Done")

#The first parameter in this assertion compares its value with the second parameter
assertIs("Selenium Python", "Selenium Python", "Comparison Done")

assertIsNot ("Selenium Python", "Selenium", "Comparison Done")


#The first parameter in this assertion is checked to see if it yields none
assertIsNone ( r , "Comparison Done")

assertIsNotNone ( r , "Comparison Done")

j = set(["Python", "Java", "C"])
assertIn ("Python", j , " Comparison Done")

j = set(["Python", "Java", "C"])
assertNotIn ("UFT", j , " Comparison Done")

assertListEqual([5, 6], [1, 3], message)

assertTupleEqual((4, 5), (4, 5), message)

assertSetEqual(s1, s2, message)

assertDictEqual ({1:4, 2:5},  {2:5, 3:6}, message)

assertGreater (3, 2, "Comparison Done")

assertLess(3, 2, "Comparison Done")