//Смотрим шо такое этот ваш GoLang
package main

import (
	"errors"
	"fmt"
	"math"
	"math/rand"
	"reflect"
	"strconv"
)

type person struct {
	name string
	age int
}

//Отображение массива
func displayer(arr [5] int)  {
	fmt.Println("Функция displayer (5)")
	fmt.Println(arr)
}

//Сумма двух значений
func sum(a int, b int)  int {
	result := a+b
	return result
}

///Функция квадрата, которая может возвращать как квадрат
//Так и ошибку вычисления
func sqrt(x float64) (float64, error){
	if x < 0{
		return 0, errors.New("Аргумент меньше 0")
	}
	return math.Sqrt(x), nil
}

//Генерация float в заданных диапазонах
func randFloats(min, max float64, n int) []float64 {
	res := make([]float64, n)
	for i := range res {
		res[i] = min + rand.Float64() * (max - min)
	}
	return res
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

	fmt.Println(reflect.TypeOf(array5).String())

	//Динамические массивы (?)
	var someElements1 = [] int {1,2,3,4,5,6}
	var someElements2 = [] int {}

	for i := len(someElements1)-1; i >= 0; i--{
		someElements2 = append(someElements2, someElements1[i])
	}
	fmt.Println(someElements1)
	fmt.Println(someElements2)
	fmt.Println(reflect.TypeOf(someElements1).String())

	//maps aka питоновские словари
	mapExample := make(map[string]int)
	mapExample["triangle"] = 4
	mapExample["square"] = 15

	fmt.Println("Итерация по map'у:")
	fmt.Println(mapExample)
	for key, value := range mapExample {
		fmt.Printf("Ключ %s, значение %d\n", key, value)

		for i := 0; i < 10; i++ {
			//Удобно делать inc
			mapExample[key] ++
		}
	}

	fmt.Println(mapExample)
	delete(mapExample,"square")
	fmt.Println(mapExample)
	//Обращение такое же

	i := 0
	for i < 100  {
		fmt.Printf("Работает цикл while: %d\n", i)
		i++
	}

	arrayForIteration := []string{"кошкас1","кошкас2","кошкас3"}
	fmt.Println(arrayForIteration)
	for index, value := range arrayForIteration {
		fmt.Println("index", index, "value", value)
	}
	mapForIteration := make(map[string]string)
	mapForIteration["a"] = "aa"
	mapForIteration["b"] = "bb"
	mapForIteration["c"] = "cc"
	fmt.Println("\n")
	fmt.Println(mapForIteration)
	for key, value := range mapForIteration {
		fmt.Println("key", key, "value", value)
	}

	argA := 1
	argB := 8
	funcResult := sum(argA,argB)
	fmt.Printf("Результат работы функции sum с аргументами %d и %d = %d", argA, argB, funcResult)

	i = 0
	for _, value := range randFloats(-1.10, 526.98, 250){
		sqrtResult, err := sqrt(value)
		if err != nil{
			fmt.Println(err)
		} else{
			fmt.Printf("[Итерация %d] sqrt(%f) = %f\n",i, value,sqrtResult)
		}
		i++
	}

	//Структуры
	p := person{name: "Kot", age: 10}
	fmp.
	p
}
