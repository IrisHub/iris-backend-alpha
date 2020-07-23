package main

import (
	"github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/dynamodb"
    "github.com/aws/aws-sdk-go/service/dynamodb/dynamodbattribute"

    "encoding/json"
    "fmt"
    "io/ioutil"
    "os"
    // "strconv"
)
//CURRENTLY ONLY SUPPORTING YUMMLY JSON SCHEMA FOR ALPHA RELEASE
//CURRENTLY ONLY SUPPORTING MANUAL SCHEMA ENTRY
//JULY 22 2020
//TODO: CONVERT THIS FILE INTO LAMBDA AGNOSTIC OF JSON FROM S3

type Item struct {
	Attributes struct {
		Course  []string `json:"course"`
		Cuisine []string `json:"cuisine"`
	} `json:"attributes"`
	Attribution struct {
		HTML string `json:"html"`
		Logo string `json:"logo"`
		Text string `json:"text"`
		URL  string `json:"url"`
	} `json:"attribution"`
	CookTime          string  `json:"cookTime"`
	CookTimeInSeconds int64   `json:"cookTimeInSeconds"`
	Diet              string  `json:"diet"`
	Difficulty        float64 `json:"difficulty"`
	Flavors           struct {
		Bitter  float64 `json:"Bitter"`
		Meaty   float64 `json:"Meaty"`
		Piquant float64 `json:"Piquant"`
		Salty   float64 `json:"Salty"`
		Sour    float64 `json:"Sour"`
		Sweet   int64   `json:"Sweet"`
	} `json:"flavors"`
	ID     string `json:"id"`
	Images []struct {
		HostedLargeURL  string `json:"hostedLargeUrl"`
		HostedMediumURL string `json:"hostedMediumUrl"`
		HostedSmallURL  string `json:"hostedSmallUrl"`
		ImageUrlsBySize struct {
			Three60 string `json:"360"`
			Nine0   string `json:"90"`
		} `json:"imageUrlsBySize"`
	} `json:"images"`
	IngredientLines    []string `json:"ingredientLines"`
	Name               string   `json:"name"`
	NumberOfServings   int64    `json:"numberOfServings"`
	NutritionEstimates []struct {
		Attribute   string `json:"attribute"`
		Description string `json:"description"`
		Unit        struct {
			Abbreviation       string `json:"abbreviation"`
			Decimal            bool   `json:"decimal"`
			ID                 string `json:"id"`
			Name               string `json:"name"`
			Plural             string `json:"plural"`
			PluralAbbreviation string `json:"pluralAbbreviation"`
		} `json:"unit"`
		Value int64 `json:"value"`
	} `json:"nutritionEstimates"`
	PrepTime          string `json:"prepTime"`
	PrepTimeInSeconds int64  `json:"prepTimeInSeconds"`
	Rating            int64  `json:"rating"`
	Source            struct {
		SourceDisplayName string `json:"sourceDisplayName"`
		SourceRecipeURL   string `json:"sourceRecipeUrl"`
		SourceSiteURL     string `json:"sourceSiteUrl"`
	} `json:"source"`
	Spice              float64 `json:"spice"`
	TotalTime          string  `json:"totalTime"`
	TotalTimeInSeconds int64   `json:"totalTimeInSeconds"`
	UUID               string  `json:"uuid"`
	Yield              string  `json:"yield"`
}

func getItems() []Item {
	raw, err := ioutil.ReadFile("/Users/kanyes/Downloads/Yummly28K/Iris-Yummly-Data-Cleaning/all_yummly.json")
	if err != nil {
		fmt.Println(err.Error())
		os.Exit(1)
	}

	var items []Item
	json.Unmarshal(raw, &items)
	return items
}

func main(){
	sess := session.Must(session.NewSessionWithOptions(session.Options{
		SharedConfigState: session.SharedConfigEnable,
	}))

	svc := dynamodb.New(sess)

	items := getItems()

	tableName := "YummlyRecipes"

	for _, item := range items{
		av, err := dynamodbattribute.MarshalMap(item)
		if err != nil {
	        fmt.Println("Got error marshalling map:")
	        fmt.Println(err.Error())
	        os.Exit(1)
	    }

	    input := &dynamodb.PutItemInput{
	        Item:      av,
	        TableName: aws.String(tableName),
	    }

	    _, err = svc.PutItem(input)
	    if err != nil {
	        fmt.Println("Got error calling PutItem:")
	        fmt.Println(err.Error())
	        os.Exit(1)
	    }


	    fmt.Println("Added '" + item.Name + "' to table " + tableName)
	}
}