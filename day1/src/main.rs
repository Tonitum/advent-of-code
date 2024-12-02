use std::{env::current_dir, fs};

fn load_input(filename: String) -> Vec<String> {
    let file_path = current_dir().unwrap().join(filename);
    println!("{}", file_path.display());
    // read the contents of the provided file, and return as a vector of strings
    let mut contents: Vec<String> = fs::read_to_string(file_path)
        .expect("Could not read file")
        .split("\n")
        .map(str::to_string)
        .collect();
    let _ = contents.split_off(contents.len() - 1);
    return contents;
}

fn get_index_of_spelled_digit(
    input_line: &String,
    target_digit: &String,
    current_index: &i32,
) -> i32 {
    if input_line.contains(target_digit) {
        let index = input_line
            .find(target_digit)
            .expect("Could not find expected digit string {target_digit}");
        let index_int: i32 = index.try_into().unwrap();
        if *current_index == -1 || *current_index > index_int {
            return index_int;
        }
    }
    return *current_index;
}

fn get_first_spelled_digit(input_line: &String) -> i32 {
    let mut digit_index = -1;
    digit_index = get_index_of_spelled_digit(input_line, &"zero".to_string(), &digit_index);
    digit_index = get_index_of_spelled_digit(input_line, &"one".to_string(), &digit_index);
    digit_index = get_index_of_spelled_digit(input_line, &"two".to_string(), &digit_index);
    digit_index = get_index_of_spelled_digit(input_line, &"three".to_string(), &digit_index);
    digit_index = get_index_of_spelled_digit(input_line, &"four".to_string(), &digit_index);
    digit_index = get_index_of_spelled_digit(input_line, &"five".to_string(), &digit_index);
    digit_index = get_index_of_spelled_digit(input_line, &"six".to_string(), &digit_index);
    digit_index = get_index_of_spelled_digit(input_line, &"seven".to_string(), &digit_index);
    digit_index = get_index_of_spelled_digit(input_line, &"eight".to_string(), &digit_index);
    digit_index = get_index_of_spelled_digit(input_line, &"nine".to_string(), &digit_index);
    return digit_index;
}


fn get_outer_numeric_digits(input_line: &String) -> (char, char) {
    let mut first_digit: char = 'N';
    let mut second_digit: char = 'N';
    for c in input_line.chars() {
        if c.is_digit(10) {
            first_digit = c;
            break;
        }
    }
    for c in input_line.chars().rev() {
        if c.is_digit(10) {
            second_digit = c;
            break;
        }
    }
    return (first_digit, second_digit);
}

fn get_calibration_input_for_line_by_digit(input_line: String) -> i32 {
    let digits = get_outer_numeric_digits(&input_line);
    let mut res_string = String::from(digits.0);
    res_string.push(digits.1);

    return res_string
        .parse::<i32>()
        .expect("Malformed input line, didn't find 2 digits");
}

fn get_calibration_value_for_input(input: Vec<String>) -> i32 {
    let mut result = 0;
    for line in input.iter() {
        result += get_calibration_input_for_line_by_digit(line.to_string());
    }
    return result;
}

fn get_calibration_value_numeric_only(input_filename: String) -> i32 {
    let input = load_input(input_filename);
    let digit_calibration = get_calibration_value_for_input(input);
    return digit_calibration;
}

fn main() {
    let result = get_calibration_value_numeric_only("src/input1.txt".to_string());
    println!("{result}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_load_input() {
        let result = load_input("src/example_input1.txt".to_string());
        assert_eq!(result.len(), 4);
    }

    #[test]
    fn test_get_calibration_value_from_line() {
        let result1 = get_calibration_input_for_line_by_digit("1abc2".to_string());
        assert_eq!(result1, 12);
        let result2 = get_calibration_input_for_line_by_digit("pqr3stu8vwx".to_string());
        assert_eq!(result2, 38);
        let result3 = get_calibration_input_for_line_by_digit("a1b2c3d4e5f".to_string());
        assert_eq!(result3, 15);
        let result4 = get_calibration_input_for_line_by_digit("treb7uchet".to_string());
        assert_eq!(result4, 77);
    }

    #[test]
    fn test_get_calibration_value_from_lines() {
        let mut input: Vec<String> = Vec::new();
        input.push("1abc2".to_string());
        input.push("pqr3stu8vwx".to_string());
        input.push("a1b2c3d4e5f".to_string());
        input.push("treb7uchet".to_string());
        let res = get_calibration_value_for_input(input);
        assert_eq!(res, 142);
    }

    #[test]
    fn test_get_index_of_spelled_digit() {
        let res = get_index_of_spelled_digit(&"abconecdf".to_string(), &"one".to_string(), &-1);
        assert_eq!(res, 3);
        let res = get_index_of_spelled_digit(&"abczerocdf".to_string(), &"zero".to_string(), &-1);
        assert_eq!(res, 3);
        let res = get_index_of_spelled_digit(&"abctwooneabc".to_string(), &"one".to_string(), &-1);
        assert_eq!(res, 6);
        let res = get_index_of_spelled_digit(&"abctwooneabc".to_string(), &"two".to_string(), &-1);
        assert_eq!(res, 3);
    }

    #[test]
    fn test_get_first_spelled_digit() {
        let res = get_first_spelled_digit(&"abctwooneabc".to_string());
        assert_eq!(res, 3);
    }
}
