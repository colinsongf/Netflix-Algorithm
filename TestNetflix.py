#!/usr/bin/env python3

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Netflix import netflix_predict, netflix_rmse, netflix_print, netflix_print_rmse, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :
    # ----
    # predict
    # ----

    def test_predict_1 (self) :
        i = netflix_predict(5, 5)
        self.assertEqual(i,  5)

    def test_predict_2 (self) :
        i = netflix_predict(1,1)
        self.assertEqual(i,  1)
   

    # ----
    # rmse
    # ----
   
    def test_rmse_1 (self) :
        v = netflix_rmse((1,2), (1,2))
        self.assertEqual(v, 0)

    def test_rmse_2 (self) :
        v = netflix_rmse((1,2,3), (2,3,4))
        self.assertEqual(v, 1)

    def test_rmse_3 (self) :
        v = netflix_rmse((2,3,4), (4,5,6))
        self.assertEqual(v, 2)

    def test_rmse_4 (self) :
        v = netflix_rmse((2,3,4), (4,3,2))
        self.assertEqual(v, 1.632993161855452)

    def test_rmse_5 (self) :
        v = netflix_rmse((1,2,3), (7,8,9))
        self.assertEqual(v, 6)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        netflix_print(w, 3423)
        self.assertEqual(w.getvalue(), "3423\n")

    def test_print_2 (self) :
        w = StringIO()
        netflix_print(w, 92838)
        self.assertEqual(w.getvalue(), "92838\n")

    def test_print_3 (self) :
        w = StringIO()
        netflix_print(w, 11134234)
        self.assertEqual(w.getvalue(), "11134234\n")

    def test_print_4 (self) :
        w = StringIO()
        netflix_print(w, 1)
        self.assertEqual(w.getvalue(), "1\n")

    def test_print_5 (self) :
        w = StringIO()
        netflix_print(w, 9293277)
        self.assertEqual(w.getvalue(), "9293277\n")

    # -----
    # print rmse
    # -----

    def test_print_rmse_1 (self) :
        w = StringIO()
        netflix_print_rmse(w, .951)
        self.assertEqual(w.getvalue(), "RMSE: 0.95\n")

    def test_print_rmse_2 (self) :
        w = StringIO()
        netflix_print_rmse(w, 92)
        self.assertEqual(w.getvalue(), "RMSE: 92.00\n")

    def test_print_rmse_3 (self) :
        w = StringIO()
        netflix_print_rmse(w, 1.777)
        self.assertEqual(w.getvalue(), "RMSE: 1.78\n")

    def test_print_rmse_4 (self) :
        w = StringIO()
        netflix_print_rmse(w, 1.772)
        self.assertEqual(w.getvalue(), "RMSE: 1.77\n")

    def test_print_rmse_5 (self) :
        w = StringIO()
        netflix_print_rmse(w, 192.3)
        self.assertEqual(w.getvalue(), "RMSE: 192.30\n")

    # -----
    # solve
    # -----
"""
    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
"""

# ----
# main
# ----

if __name__ == "__main__" :
    main()


