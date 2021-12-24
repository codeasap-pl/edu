import Data.List (foldl')

my_filter n = n `mod` 3 == 0 || n `mod` 5 == 0
solve x = foldl' (+) 0 x

main = print(solve(filter my_filter [1..1000 - 1]))
