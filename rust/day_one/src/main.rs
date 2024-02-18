use std::{fs, ops::Add};

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
    let mut first_digit: u32 = 0;
    let mut second_digit: u32 = 0;
    for char in input_line.chars().rev() {
       if !char.is_digit(10) {
           continue;
       }
       first_digit = char.to_digit(10).unwrap();
    }
    for char in input_line.chars() {
       if !char.is_digit(10) {
           continue;
       }
       second_digit = char.to_digit(10).unwrap();
    }
    let number_string = first_digit.to_string().add(&second_digit.to_string());
    dbg!(&number_string);
    let number = number_string.parse::<u32>().unwrap();
    number
}


fn main() {
    // load the input file
    let input_file_name:String = "src/resources/test_input.txt".into();
    let input_lines: String = load_input(input_file_name);
    // split into lines
    let split_lines = split_input_into_array(&input_lines);
    // for each line, get the first digit and last digit
    let mut total_sum: u32 = 0;

    for line in split_lines {
        total_sum = total_sum + get_first_and_last_digit(line);
    }
    dbg!(&total_sum);
}
