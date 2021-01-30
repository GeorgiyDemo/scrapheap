//Смотрим шо такое этот ваш GoLang
package main

import (
	"fmt"
	"sort"
	"strconv"
)

func displayer(arr [5] int)  {
	fmt.Println("Функция displayer (5)")
	fmt.Println(arr)
}

func main() {
	fmt.Println("День добрый кароч")
	var result int = 0
	for i := 0; i < 10; i++ {
		result = result + i
		fmt.Println(i,result)
	}
	//Происвоение норм
	resultNew := 2 * result
	//Конкатинация строк и всякое такое
	fmt.Println("sum * 2 = "+strconv.Itoa(resultNew)+"\nsum = "+strconv.Itoa(result))

	//Числа делящийся на 3 (синтаксис if)
	for i := 0; i < 100; i++ {
		if i % 3 == 0 {
			fmt.Println("Число "+strconv.Itoa(i)+" делится на 3")
		} else {
			fmt.Println("...")
		}
	}
	//Статические массивы
	var array5[5] int //по-дефолту все в 0
	displayer(array5)
	array5[1] = 1
	displayer(array5)
	array5[len(array5)-1] = 4
	displayer(array5)

	//Динамические массивы (?)
	var someElements1 = [] int {1,2,3,4,5,6}
	var someElements2 = sort.Reverse(sort.IntSlice(someElements1))
	fmt.Println(someElements2)
	var result =  append(someElements1, someElements2)
	fmt.Println(someElements)




}
