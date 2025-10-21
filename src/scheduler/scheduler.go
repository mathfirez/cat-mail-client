package scheduler

import "time"

// Queries the database for messages and sends to the printer queue based on the interval defined in the .env file.
// Sends a single message per run to avoid bloating.
func Scheduler(interval int) {
	seconds := time.Duration(interval) * time.Second
	for {
		time.Sleep(seconds)
		//Querying new messages from the API.

		// If no messages, sleep again.
		// Else, server updates message fields on DB based on models.Message and client (here) sends to printer.
	}
}
