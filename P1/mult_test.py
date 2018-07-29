#Copyright (C) 2018 Joe Mankovecky
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

import multiples_3_5 as ml

def test_mult_3():
    assert ml.mult_3(0) == 0
    assert ml.mult_3(4) == 3
    assert ml.mult_3(6) == 3
    assert ml.mult_3(10) == 18

def test_mult_5():
    assert ml.mult_5(0) == 0
    assert ml.mult_5(6) == 5
    assert ml.mult_5(10) == 5
    assert ml.mult_5(11) == 15
    
def test_findsum():
    assert ml.findsum(0) == 0
    assert ml.findsum(6) == 8
    assert ml.findsum(10) == 23
    assert ml.findsum(100) == 2318

def main(args):
    
    if args == "--t" or args == "--v":
        test_mult_3()
        test_mult_5()
        test_findsum()
        if args == "--v":
            print("Tests completed successfully")

if __name__ == "__main__":
    main(None)
