import unittest

from lab_syntax import *


class TestSyntaxMolekyl(unittest.TestCase):

    def testMolekyl(self):
        """ Testar Atom, stora och små bokstäver """
        self.assertEqual(kollaSyntax("H2"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(kollaSyntax("P21"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(kollaSyntax("Ag3"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(kollaSyntax("Fe12"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(kollaSyntax("Xx5"), "Formeln är syntaktiskt korrekt")

    def testFelMolekyl(self):
        self.assertEqual(kollaSyntax("a"), "Saknad stor bokstav")
        self.assertEqual(kollaSyntax("cr12"), "Saknad stor bokstav")
        self.assertEqual(kollaSyntax("8"), "Saknad stor bokstav")
        self.assertEqual(kollaSyntax("Cr0"), "För litet tal")
        self.assertEqual(kollaSyntax("Pb1"), "För litet tal")

if __name__ == '__main__':
    unittest.main()