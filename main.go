package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
	"strconv"
)

func main() {
	fmt.Println("Hello World!")
	var id int64 = 123456
	friends := get_friends(id)
	fmt.Println(friends)
}

func get_friends(user_id int64) string {
	resp, err := http.Get(
		"https://api.vk.com/method/friends.get?user_id=" + strconv.FormatInt(user_id, 10))
	if err != nil {
		// Handle error
		fmt.Println("Error occured")
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	return string(body)
}