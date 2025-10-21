package models

import "time"

type Message struct {
	Id         string
	Content    string
	Author     string
	Posted_on  time.Time
	Printed    bool
	Printed_on time.Time
}
