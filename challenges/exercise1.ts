//TODO:Complete the js equivalent of the challenges done in the first chapter without relying on the answers of the original problems.

` Here I'll be tackling all the exercise questions from Problem solving in DS and Algorithms  chapter 1 `

const array = [1, 9, -5, 0, 12, 4]
const array2 = [[1, 4, 6], [2, 3, -8, 1], [2, 5, 7], [-10, -20, -9] ]
const array0 = [1, 0, 1, 0, 1, 1, 0, 0]
const array3 = [1, 2, 0, 2, 1, 2, 0, 1, 1, 2, 1, 0];

`1.  Find average of all the elements in a list O(n) run time`

function findAverage(array: number[]) {
    let sum = 0;
    let length = array.length;

    array.forEach((item: number) => sum += item);

    return sum / length;
}

function findAverageRecursionMethod(array: number[]): number {
    let average = 0;

    function sumArray(array: number[]):number {
        if (array.length == 0){
            return 0
        } else {
            if (array.length == 1) {
                return array[0]
            } else {
                return array[0] + sumArray(array.slice(1))
            }
        }
    }
    average = sumArray(array) / array.length;
    return average
}

console.log(`findAverage function: ${findAverage(array)}`);

console.log(`find average recursion method: ${findAverageRecursionMethod(array)}`);

`find the sum of a two multi dimensional array`

function multiDimensionalSum(array: number[][]):number {
    let sum = 0;
    let dimensions = array.length;

    for (let i = 0; i < dimensions; i++) {
        let subArray = array[i].length;

        for (let j=0; j < subArray; j++) {
            sum += array[i][j];
        }
    }
    return sum;
}

function multiDimensionalSumRecursion(array: number[][]):number {
    let sum = 0


    return sum
}

console.log(`find the sum of a multi dimensional array`, multiDimensionalSum(array2))