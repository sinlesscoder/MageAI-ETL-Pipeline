## Strategy

1. Perform a fuzzy string match between the strings in the first DataFrame with the strings in the second DataFrame.

   - Use algorithm: Levenshtein's Distance (> 0.85 as a match)

2. Create a column called Match in one of the DataFrames.

   - Filter the DataFrame to only contain records where a fuzzy string match occurred (Match = True)

3. Based on records where the match is true, you need to replace the strings in that DataFrame with the ones that the match happened with.

4. Then you perform inner join in pandas based on the string columns.

### Resources

- [fuzzywuzzy](https://builtin.com/data-science/fuzzy-matching-python)
