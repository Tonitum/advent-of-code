use std::fs;

fn load_input(filename: String) -> String {
    let contents = fs::read_to_string(filename).
        expect("Could not load file {filename}");
    contents
}

fn split_input_into_array(lines: &String)  -> Vec<&str>{
    let parts = lines.lines();
    let collection = parts.collect::<Vec<&str>>();
    collection
}

fn get_first_and_last_digit(input_line: &str) -> u32 {
    let mut first_digit: char;
    let mut second_digit: char;
    for char in input_line.chars().rev() {
       if !char.is_digit(10) {
           continue;
       }
       first_digit = char;
    }
    for char in input_line.chars() {
       if !char.is_digit(10) {
           continue;
       }
       second_digit = char;
    }
    (first_digit+second_digit)
    // need to combine the chars and then convert to integer
    // need to also chyage the vector to a single u32
}

fn sum_digit_pairs(pairs: &Vec<(u32,u32)>) -> u32 {
    let mut sum = 0;
    for pair in pairs {
        let pair_sum = pair.0 + pair.1;
        sum += pair_sum;
    }
    sum
}

fn main() {
    // load the input file
    let input_file_name:String = "src/resources/test_input.txt".into();
    let input_lines: String = load_input(input_file_name);
    // split into lines
    let split_lines = split_input_into_array(&input_lines);
    // for each line, get the first digit and last digit
    let mut pairs: Vec<(u32,u32)> = Vec::new();

    for line in split_lines {
        pairs.push(get_first_and_last_digit(line));
        dbg!(get_first_and_last_digit(line));
    }
    let total_sum = sum_digit_pairs(&pairs);
    dbg!(&total_sum);
}
