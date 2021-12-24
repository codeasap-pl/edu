fn calculate_sum(limit: u32) -> u32
{
    let mut i: u32 = 0;
    let mut sum: u32 = 0;
    
    while i < limit {
        if i % 3 == 0 || i % 5 == 0 {
            sum = sum + i;
        }
        i += 1;
    }
    return sum;
}

fn main()
{
    let limit: u32 = 1000;
    println!("{}", calculate_sum(limit));
}
