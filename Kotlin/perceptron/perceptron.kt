/**
 * This example contains only a simple and restricted application of the Perceptron algorithm.
 * It was developed during my studies of the Kotlin language.
 * I am aware of your limitation.
 */

import kotlin.random.Random

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

class Perceptron(
    val X: Array<IntArray>,
    val y: IntArray,
    val eta: Double = 0.1,
    val epoch: Int = 1000,
) {
    val n: Int = X.size
    val m: Int = X[0].size
    val w = doubleArrayOf(
        -1.0,
        Random.nextDouble(from = -1.0, until = 1.0),
        Random.nextDouble(from = -1.0, until = 1.0)
    )
    
    fun train() {
        var n_epoch = 1
        
        while (true) {
            var erro: Boolean = false
            
            for (i in 0..n-1) {
                var u: Double = 0.0
                u += summation(X[i], w)
                
                var d: Int = activationFunction(u)
                
                if (d != y[i]) {
                    for (j in 0..m-1) {
                        w[j] += eta * (y[i] - d) * X[i][j]
                    }
                    erro = true
                }
            }
            n_epoch +=1
            
            if (n_epoch > epoch || !erro) { break }
        }
    }
    
    fun predict(x: IntArray) : Int {
        return activationFunction(summation(x, w))
    }
    
    /*
     * Auxiliary function to apply the summation
     */
    fun summation(X: IntArray, w: DoubleArray) : Double {
        var u: Double = 0.0
        
        for (i in 0..m-1) {
            u += X[i] * w[i]
        }
        return u
    }
    
    /*
     * Step Function
     */
    fun activationFunction(u: Double) : Int {
        if (u >= 0) {
            return 1
        } else {
            return 0
        }
    }
}
