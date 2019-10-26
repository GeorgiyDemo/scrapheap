class val_var {
    //Неизменяемое поле
    private val example_val = 1;
    //Изменяемое поле
    private var example_var = 2;

    open fun set_var(i: Int){
        this.example_var = i
    }

    /*
    Ошибка!!
    open fun set_val(i: Int){
        this.example_val = i
    }
     */
    open fun get_val(): Int {
        return this.example_val
    }

    open fun get_var(): Int {
        return this.example_var
    }



}