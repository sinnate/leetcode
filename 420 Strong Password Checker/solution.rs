impl Solution {
    pub fn put_marbles(weights: Vec<i32>, k: i32) -> i64 {
        if k == 1 {return 0}

        let mut distribution: Vec<i32> = Vec::new();
        for i in 1 .. weights.len(){
            distribution.push(weights[i-1] + weights[i]);
        }
        distribution.sort();
        let mut max_score = 0;
        let mut min_score = 0;
        for i in 0 .. (k - 1) as usize{
            min_score += distribution[i];
            max_score += distribution[distribution.len()- 1 - i];
        }
        (max_score - min_score).into()
    }
}