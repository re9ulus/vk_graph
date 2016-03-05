package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
	"strconv"
	"encoding/json"
)

type Response struct {
	Response []int64
}

type Node struct {
	Index int64
	Edges []Node
}

type Graph struct {
	Nodes []Node
}

func main() {
	fmt.Println("Hello World!")
	var id int64 = 123456
	friends := get_friends(id)

	var result Response
	json.Unmarshal([]byte(friends), &result)
	fmt.Println(result.Response)
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
	if err != nil {
		fmt.Println("Error while parsing response body")
	}
	return string(body)
}
