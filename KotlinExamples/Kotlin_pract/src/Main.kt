fun alter(): Int {
    var NewString = "ХЫ"

    var max: Int = 0
    var min: Int = 99999
    var BufString: String = ""
    var conc: Int = 1

    for (i in 1..1000) {

        val obj = UserKotlin(i)
        var OutputField = obj.field
        println(OutputField)

        conc *= i
        if (max < i)
            max = i
        if (min > i)
            min = i

        BufString += i.toString()
    }

    println("$NewString $BufString\nMin: $min\nMax: $max")

    return conc
}

fun substring_example() {
    var A: Int = 8
    var B: Int = 10
    println("Сумма: ${A + B}")
}

fun main() {
    var check = "MEOW"
    println("Что говорят Koshkas?\n$check")

    alter()
    println("MEEWEKWOKKO")

    substring_example()
    val EmailObj = GetEmail("KOT@mail.ru")
    println(EmailObj.getvalue())

    val o = val_var()
    println(o.get_var())
    o.set_var(777)
    println(o.get_var())
    println(o.get_val())

}