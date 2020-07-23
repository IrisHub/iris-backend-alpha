package main

import (
	"fmt"
	"context"
	"github.com/aws/aws-lambda-go/lambda"
)

type MyEvent struct {
	Name string `json:"name"`
}

func HandleRequest(ctx context.Context, name MyEvent) (string, error) {
	fmt.Printf("Hello %s! Using launch script with update this time!", name.Name )
	return "abcd", nil
}

func main() {
	lambda.Start(HandleRequest)
}