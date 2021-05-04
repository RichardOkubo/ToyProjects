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
