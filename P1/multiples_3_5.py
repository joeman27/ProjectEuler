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


def mult_3(max):
    j = 0
    j_sum = 0
    
    while j < max:
        if j % 5 != 0:
            j_sum+=j
        j += 3
        
    return j_sum
    
    
def mult_5(max):
    k = 0
    k_sum = 0
    
    while k < max:
        k_sum+=k
        k+=5
        
    return k_sum
    
    
def findsum(max):
    print(mult_3(max) + mult_5(max))
    
    
if __name__ == "__main__":
    import sys
    
    try:
        import mult_test
        mult_test.main(sys.argv[2])
    except IndexError:
        pass
    
    max = int(sys.argv[1])
    findsum(max)
