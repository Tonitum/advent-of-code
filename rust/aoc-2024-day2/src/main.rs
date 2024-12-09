use std::fs;

fn load_input(filepath: &String) -> Vec<Vec<i32>> {
    let contents = fs::read_to_string(filepath).expect("Could not read file");
    let reports_contents = contents.split("\n");
    let mut report_vectors: Vec<Vec<i32>> = Vec::new();
    for report_line in reports_contents {
        if report_line == "" {
            break;
        }
        let converted_report: Vec<i32> = report_line
            .split(" ")
            .map(|x| x.parse::<i32>().unwrap())
            .collect();
        report_vectors.push(converted_report);
    }
    return report_vectors;
}

fn is_report_safe_with_damper(report: &Vec<i32>) -> bool {
    if is_report_safe(&report) {
        return true;
    }
    for level_index in 0..report.len() {
        let mut modified_report = report.clone();
        modified_report.remove(level_index);
        if is_report_safe(&modified_report) {
            return true;
        }
    }
    return false;
}

fn is_report_safe(report: &Vec<i32>) -> bool {
    let mut previous_level = report.get(0).expect("Could not load first index");
    for level_index in 1..report.len() - 1 {
        let current_level = report
            .get(level_index)
            .expect("Could not load current index");
        let next_level = report
            .get(level_index + 1)
            .expect("Could not load next index");
        let current_difference = previous_level - current_level;
        let next_difference = current_level - next_level;
        if current_difference == 0 {
            return false;
        }
        if current_difference.abs() > 3 || current_difference.abs() < 1 {
            return false;
        }
        // if difference is negative, we are ascending
        if current_difference < 0 {
            if next_difference > 0 {
                return false;
            }
            previous_level = current_level;
            continue;
        }
        if next_difference < 0 {
            return false;
        }
        // if it is possitive, we should be descending
        previous_level = current_level;
    }
    let last_difference = previous_level - report.get(report.len() - 1).unwrap();
    if last_difference.abs() > 3 || last_difference.abs() < 1 {
        return false;
    }

    return true;
}

fn get_count_of_safe_reports_with_damper(reports: &Vec<Vec<i32>>) -> i32 {
    let mut safe_reports = 0;
    for report in reports {
        if is_report_safe_with_damper(report) {
            safe_reports += 1;
        }
    }
    return safe_reports;
}

fn get_count_of_safe_reports(reports: &Vec<Vec<i32>>) -> i32 {
    let mut safe_reports = 0;
    for report in reports {
        if is_report_safe(report) {
            safe_reports += 1;
        }
    }
    return safe_reports;
}

fn main() {
    let reports = load_input(&"./src/input.txt".to_string());
    let safe_count = get_count_of_safe_reports(&reports);
    println!("Standard Safe: {safe_count}");
    let safe_with_damper_count = get_count_of_safe_reports_with_damper(&reports);
    println!("Safe With Damper: {safe_with_damper_count}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_count_of_safe_reports() {
        let report1 = Vec::from([7, 6, 4, 2, 1]);
        let report2 = Vec::from([1, 2, 7, 8, 9]);
        let report3 = Vec::from([9, 7, 6, 2, 1]);
        let report4 = Vec::from([1, 3, 2, 4, 5]);
        let report5 = Vec::from([8, 6, 4, 4, 1]);
        let report6 = Vec::from([1, 3, 6, 7, 9]);
        let reports = Vec::from([report1, report2, report3, report4, report5, report6]);
        let result = get_count_of_safe_reports(&reports);
        assert_eq!(2, result);
    }
    #[test]
    fn test_is_level_safe_without_damper() {
        let report1 = Vec::from([7, 6, 4, 2, 1]);
        let result1 = is_report_safe(&report1);
        assert!(result1);

        let report8 = Vec::from([9, 8, 7, 6, 1]);
        let result8 = is_report_safe(&report8);
        assert!(!result8);

        let report2 = Vec::from([1, 2, 7, 8, 9]);
        let result2 = is_report_safe(&report2);
        assert!(!result2);

        let report3 = Vec::from([9, 7, 6, 2, 1]);
        let result3 = is_report_safe(&report3);
        assert!(!result3);

        let report4 = Vec::from([1, 3, 2, 4, 5]);
        let result4 = is_report_safe(&report4);
        assert!(!result4);

        let report5 = Vec::from([8, 6, 4, 4, 1]);
        let result5 = is_report_safe(&report5);
        assert!(!result5);

        let report6 = Vec::from([1, 3, 6, 7, 9]);
        let result6 = is_report_safe(&report6);
        assert!(result6);

        let report7 = Vec::from([24, 25, 28, 31, 28]);
        let result7 = is_report_safe(&report7);
        assert!(!result7);
    }
    #[test]
    fn test_is_level_safe_with_damper_multi_directions() {
        let report4 = Vec::from([1, 3, 2, 4, 5]);
        let result4 = is_report_safe_with_damper(&report4);
        assert!(result4);
        let report_multi_directional = Vec::from([1, 4, 3, 2, 5]);
        let multi_directional_result = is_report_safe_with_damper(&report_multi_directional);
        assert!(!multi_directional_result);
    }
    #[test]
    fn test_is_level_safe_with_damper() {
        let report1 = Vec::from([7, 6, 4, 2, 1]);
        let result1 = is_report_safe_with_damper(&report1);
        assert!(result1);

        let report8 = Vec::from([9, 8, 7, 6, 1]);
        let result8 = is_report_safe_with_damper(&report8);
        assert!(result8);

        let report2 = Vec::from([1, 2, 7, 8, 9]);
        let result2 = is_report_safe_with_damper(&report2);
        assert!(!result2);

        let report3 = Vec::from([9, 7, 6, 2, 1]);
        let result3 = is_report_safe_with_damper(&report3);
        assert!(!result3);

        let report5 = Vec::from([8, 6, 4, 4, 1]);
        let result5 = is_report_safe_with_damper(&report5);
        assert!(result5);

        let report6 = Vec::from([1, 3, 6, 7, 9]);
        let result6 = is_report_safe_with_damper(&report6);
        assert!(result6);
    }
}
// 412 is too low
// 515 is too high
