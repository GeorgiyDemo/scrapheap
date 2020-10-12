class UserKotlin {

    var field = 20

    init {
        println("Init block")
    }

    constructor(i: Int) {
        this.field = i
        println("Constructor")
    }
}

