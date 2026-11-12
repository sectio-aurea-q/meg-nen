# Comparison of the two readings

50 values in each reading; 50 agree in value and error, digit for digit; none differs.
The comparison was made by program (value and error as strings, per source, table, column and temperature).

Differences that are not differences of value:
- S014: the value and its ± stand in separate cells. The first reading recorded them on separate lines, the second
  wrote them with one space ("3.65 ±0.06"). `as_printed` follows the second form.
- The second reading lists eight remarks; those that bear on the rows are taken up in `resolution.md`.
