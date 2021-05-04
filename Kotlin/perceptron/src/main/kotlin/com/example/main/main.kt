/**
 * This example contains only a simple and restricted application of the Perceptron algorithm.
 * It was developed during my studies of the Kotlin language.
 * I am aware of your limitation.
 */
package com.example.main

import com.example.perceptron.Perceptron

fun main() {
    // AND
    val xAnd: Array<IntArray> = arrayOf(
        intArrayOf(-1, 0, 0),
        intArrayOf(-1, 1, 0),
        intArrayOf(-1, 0, 1),
        intArrayOf(-1, 1, 1)
    )
    val yAnd = intArrayOf(0, 0, 0, 1)

    val perceptronAnd = Perceptron(xAnd, yAnd)
    perceptronAnd.train()
    printResult("AND operator", xAnd, yAnd, perceptronAnd)

    // OR
    val xOr: Array<IntArray> = arrayOf(
        intArrayOf(-1, 0, 0),
        intArrayOf(-1, 1, 0),
        intArrayOf(-1, 0, 1),
        intArrayOf(-1, 1, 1)
    )
    val yOr = intArrayOf(0, 1, 1, 1)

    val perceptronOr = Perceptron(xOr, yOr)
    perceptronOr.train()

    printResult("\nOR operator", xOr, yOr, perceptronOr)

    // NOT
    val xNot: Array<IntArray> = arrayOf(
        intArrayOf(-1, 0),
        intArrayOf(-1, 1)
    )
    val yNot = intArrayOf(1, 0)

    val perceptronNot = Perceptron(xNot, yNot)
    perceptronNot.train()

    printResult("\nNOT operator", xNot, yNot, perceptronNot)

    // THEN
    val xThen: Array<IntArray> = arrayOf(
        intArrayOf(-1, 0, 0),
        intArrayOf(-1, 1, 0),
        intArrayOf(-1, 0, 1),
        intArrayOf(-1, 1, 1)
    )
    val yThen = intArrayOf(1, 0, 1, 1)

    val perceptronThen = Perceptron(xThen, yThen)
    perceptronThen.train()

    printResult("\nTHEN operator", xThen, yThen, perceptronThen)

    // XOR (bad)
    val xXor: Array<IntArray> = arrayOf(
        intArrayOf(-1, 0, 0),
        intArrayOf(-1, 1, 0),
        intArrayOf(-1, 0, 1),
        intArrayOf(-1, 1, 1)
    )
    val yXor = intArrayOf(0, 1, 1, 0)

    val perceptronXor = Perceptron(xXor, yXor)
    perceptronXor.train()

    printResult("\nXOR operator", xXor, yXor, perceptronXor)
}

fun printResult(msg: String, X: Array<IntArray>, y: IntArray, perceptron: Perceptron) {
    println(msg)

    // ...
}
