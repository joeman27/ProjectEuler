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

def streak(n):
    k = 0
    
    while (n+k)%(k+1) == 0:
        k+=1
    
    return k
    
def p_function(s, N):
    count = 0
    
    for n in range(2,N):
        if streak(n) == s:
            count += 1
            
    return count
    
    
def main():
    p_sum = 0
    
    for i in range(1,31):
        p_sum += p_function(i, 4**i)
        print("p_sum currently: ",p_sum)
    
    return p_sum
    
if __name__ == "__main__":
    main()
