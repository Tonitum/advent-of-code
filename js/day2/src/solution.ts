import * as fs from 'fs';
import path from 'path';

function loadInput(fileName: String): String[] {
    const srcFolder = path.dirname(__dirname);
    const filePath = path.join(srcFolder, "/res/", fileName.toString());
    let res = fs.readFileSync(filePath);
    let lines = res.toString().split("\n");
    return lines;
}

function parseLine(line: String): number[] {
    let parts = line.split(" ").map((item) => {
        return parseInt(item)
    })
    return parts
}

function isLevelSafe(level: number[]): boolean {
    let isUp = null;
    let curr = level[0]
    for (let i = 1; i < level.length; i++) {
        let next = level[i]
        if (curr === next) {
            return false;
        }

        if (i === 1) {
            isUp = curr < next
        }

        let difference = Math.abs(curr - next)

        if (3 < difference || 1 > difference) {
            return false;
        }

        if (curr > next && isUp) {
            return false
        }

        if (curr < next && !isUp) {
            return false;
        }
        curr = next
    }
    return true;
}

function isLevelPossiblySafe(level: number[]): boolean {
    if (isLevelSafe(level)) {
        return true;
    }
    for (let i = 0; i < level.length; i++) {
        let removedElement = level.splice(i, 1)
        if (isLevelSafe(level)) {
            return true;
        }
        level.splice(i, 0, removedElement[0])
    }

    return false;
}

function main() {
    let lines: String[] = loadInput("input.txt");
    let safeCount = 0;
    let possibleSafeCount = 0;
    lines.forEach((line) => {
        if (line == "") { return }
        let parsedLine = parseLine(line)
        if (isLevelSafe(parsedLine)) {
            safeCount++;
        }
        if (isLevelPossiblySafe(parsedLine)) {
            possibleSafeCount++;
        }
    })
    console.log(safeCount)
    console.log(possibleSafeCount)
}

main()
