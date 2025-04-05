# CPU
Made with Antares logic simulator.
```
	ALU
add                   0000
sub                   0001
greater_zero          0010
equal_zero            0011
greate_equal_zero     0100
greater		      0101
equal                 0110
less                  0111
greate_equal          1000
less_equal            1001


0 0 0  0 0
0 0 1  1 0
0 1 0  1 0
0 1 1  0 1
1 0 0  1 0
1 0 1  0 1
1 1 0  0 1
1 1 1  1 1


0 0 0  0 0
0 0 1  1 1
0 1 0  1 1
0 1 1  0 1
1 0 0  1 0
1 0 1  0 0
1 1 0  0 0
1 1 1  1 1

       CPU
0000 000  000 0000000000000000000000
cmd  from to          value

add                   0000
sub                   0001
greater_zero          0010
equal_zero            0011
greate_equal_zero     0100
greater		      0101
equal                 0110
less                  0111
greate_equal          1000
less_equal            1001
copy                  1010
set                   1011
jump                  1100
stop                  1101
```
