import * as fs from 'fs';
import path from 'path';
import { callbackify } from 'util';

function loadInput(fileName: String): Array<String> {
    const srcFolder = path.dirname(__dirname);
    const filePath = path.join(srcFolder, "/res/", fileName.toString());
    let res = fs.readFileSync(filePath);
    let lines = res.toString().split("\n");
    return lines;
}

function insertSorted(val: number, array: Array<number>) {
    if (array.length == 0) {
        array.push(val);
        return;
    }
    // check if we're smaller than the first number
    if (val <= array[0]) {
        array.splice(0, 0, val)
        return;
    }

    // check if we're larger than the last number
    if (val >= array[array.length - 1]) {
        array.push(val);
        return;
    }

    // binary search to find home in array
    let low = 0;
    let high = array.length;

    while (true) {
        let midIndex = Math.floor((low + high) / 2)
        let midVal = array[midIndex]
        if (high <= low) {
            let targetIdx = (val > array[low]) ? (low + 1) : low
            array.splice(targetIdx, 0, val)
            break
        }
        if (val == midVal) {
            array.splice(midIndex, 0, val)
            break;
        }
        if (val < midVal) {
            high = midIndex - 1
            continue
        }
        if (val > midVal) {
            low = midIndex + 1
            continue
        }
        break
    }

}

function createSortedArrays(lines: Array<String>): [Array<number>, Array<number>] {
    let left: Array<number> = [];
    let right: Array<number> = [];
    for (let i = 0; i < lines.length; i++) {
        if (lines[i] == "") {
            continue;
        }
        let nums = lines[i].split("   ");
        let leftNum = nums[0];
        let rightNum = nums[1];
        insertSorted(parseInt(leftNum), left);
        insertSorted(parseInt(rightNum), right);
    }
    return [left, right];
}

function createArrays(lines: Array<String>): [number[], number[]] {
    let left: Array<number> = [];
    let right: Array<number> = [];
    for (let i = 0; i < lines.length; i++) {
        if (lines[i] == "") {
            continue;
        }
        let nums = lines[i].split("   ");
        let leftNum = nums[0];
        let rightNum = nums[1];
        left.push(parseInt(leftNum))
        right.push(parseInt(rightNum))
    }
    return [left, right]
}

function testInsertSorted(arr: number[]) {
    let destArr: number[] = []
    for (let i = 0; i < arr.length; i++) {
        insertSorted(arr[i], destArr);
    }
}

function calculateSimilarityScore(left: number[], right: number[]): number {
    let score = 0;
    let scoresMap: Map<number, number> = new Map;
    for (let rightIdx = 0; rightIdx < right.length; rightIdx++) {
        let target = right[rightIdx]
        if (!scoresMap.has(target)) {
            scoresMap.set(target, 1)
            continue
        }
        let currentCount: number = scoresMap.get(target)!
        scoresMap.set(target, currentCount + 1)
    }
    for (let leftIdx = 0; leftIdx < left.length; leftIdx++) {
        let target = left[leftIdx];
        if (!scoresMap.has(target)) {
            continue;
        }
        let multiplier: number = scoresMap.get(target)!
        score += (target * multiplier)
    }
    return score;
}

function addUpDistances(left: number[], right: number[]): number {
    let distance: number = 0
    for (let i = 0; i < left.length; i++) {
        distance += Math.abs(left[i] - right[i])
    }
    return distance
}

function main() {
    let lines: String[] = loadInput("input.txt");
    let arrays: [number[], number[]] = createSortedArrays(lines);
    let left: number[] = [...arrays[0]]
    let right: number[] = [...arrays[1]]

    let distance: number = addUpDistances(left, right)
    console.log(distance)
    let [distanceLeft, distanceRight] = createArrays(lines)
    let score: number = calculateSimilarityScore(distanceLeft, distanceRight)
    console.log(score)
}

main();
