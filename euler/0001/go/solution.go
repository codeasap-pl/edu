package main

import "fmt"

func calculate_sum(n int) int {
    var i int = 0;
    var sum int = 0

    for ; i < n; i++ {
        if i % 3 == 0 || i % 5 == 0 {
            sum = sum + i
        }
    }
    return sum;
}

func main() {
    fmt.Println(calculate_sum(1000))
}
