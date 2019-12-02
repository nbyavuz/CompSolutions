use std::fs::File;
use std::io::{BufRead, BufReader};

const FILE_NAME: &str = "../input/input.txt";

fn fuels(number: i32) -> i32 {
    let new_fuel: i32 = number / 3 - 2;
    if new_fuel <= 0 {
        return 0;
    }
    return new_fuel + fuels(new_fuel);
}

fn main() {
    let file = File::open(FILE_NAME).unwrap();
    let reader = BufReader::new(file);

    let mut result: i32 = 0;
    for line in reader.lines() {
        let line = line.unwrap().parse::<i32>().unwrap();
        result += fuels(line);
    }

    println!("{}", result);
}
