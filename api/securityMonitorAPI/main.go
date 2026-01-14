package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"securityMonitorAPI/structs"
	_ "strconv"

	"github.com/gorilla/mux"
)

var packets []structs.Packet

func createPacket(w http.ResponseWriter, r *http.Request) {
	var packet structs.Packet
	_ = json.NewDecoder(r.Body).Decode(&packet)

	packets = append(packets, packet)

	w.Header().Set("Content-Type", "application/json")
	err := json.NewEncoder(w).Encode(packet)
	if err != nil {
		return
	}
}

func main() {
	r := mux.NewRouter()

	r.HandleFunc("/api/packets", createPacket).Methods("POST")

	fmt.Println("Server is running on port 8000...")
	log.Fatal(http.ListenAndServe(":8000", r))
}
