use std::fs;

// fn load_input(filepath: String) {
fn load_input(filepath: String) -> (Vec<i32>, Vec<i32>) {
    let mut first_list: Vec<i32> = Vec::new();
    let mut second_list: Vec<i32> = Vec::new();
    let contents = fs::read_to_string(filepath).expect("Could not read file");
    let contents_split = contents.split("\n");
    for ele in contents_split {
        if ele == "" {
            break;
        }
        let mut numbers = ele.split("   ");
        let first_number = numbers.next().unwrap();
        let second_number = numbers.last().unwrap();
        first_list.push(first_number.parse::<i32>().unwrap());
        second_list.push(second_number.parse::<i32>().unwrap());
    }
    return (first_list, second_list);
}

fn calculate_differences(mut location_list_1: Vec<i32>, mut location_list_2: Vec<i32>) -> i32 {
    // sort the two arrays
    location_list_1.sort();
    location_list_2.sort();
    // iterate through and calculate different at each index
    let mut difference = 0;

    for i in 0..(location_list_1.len()) {
        let location_id_1 = location_list_1.get(i).unwrap();
        let location_id_2 = location_list_2.get(i).unwrap();
        if location_id_1 > location_id_2 {
            difference += location_id_1 - location_id_2;
        } else {
            difference += location_id_2 - location_id_1;
        }

    }
    return difference; 
}


fn reconcile_lists_by_difference(filepath: String) -> i32 {
    // load the input
    let location_lists = load_input(filepath);
    // parse the rows into 2 arrays
    let difference = calculate_differences(location_lists.0, location_lists.1);
    return difference;
}

fn calculate_similarity(mut location_list_1: Vec<i32>, mut location_list_2: Vec<i32>) -> i32 {
    // sort the two arrays
    location_list_1.sort();
    location_list_2.sort();
    let mut unique_locations = location_list_1.to_vec();
    let mut total_similarity_score = 0;
    unique_locations.dedup();
    for location_id in unique_locations {
        // get the count of the location_id in the first list
        let first_count: i32 = location_list_1.iter().filter(|&n| *n == location_id).count().try_into().unwrap();
        // get the count of the location_id in the second list
        let second_count: i32 = location_list_2.iter().filter(|&n| *n == location_id).count().try_into().unwrap();
        let similarity_score = location_id * second_count * first_count;
        total_similarity_score += similarity_score;
    }
    return total_similarity_score;
}

fn reconcile_lists_by_similarity(filepath: String) -> i32 {
    // load the input
    let location_lists = load_input(filepath);
    // parse the rows into 2 arrays
    let similarity = calculate_similarity(location_lists.0, location_lists.1);
    return similarity;
}

fn main() {
    let difference = reconcile_lists_by_difference("./src/input_1.txt".to_string());
    println!("difference: {difference}");
    let similarity = reconcile_lists_by_similarity("./src/input_1.txt".to_string());
    println!("similarity: {similarity}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_reconcile_lists_by_difference() {
        let result = reconcile_lists_by_difference("./src/example_input.txt".to_string());
        assert_eq!(result, 11);
    }
    #[test]
    fn test_reconcile_lists_by_similarity() {
        let result = reconcile_lists_by_similarity("./src/example_input.txt".to_string());
        assert_eq!(result, 31);
    }
}
