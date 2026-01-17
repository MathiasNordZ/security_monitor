package main

import (
	"encoding/json"
	"log"
	"net/http"
	"securityMonitorAPI/structs"

	"github.com/gorilla/mux"
)

var packets []structs.PacketWindow

func createPacket(w http.ResponseWriter, r *http.Request) {
	var packetWindow structs.PacketWindow
	if err := json.NewDecoder(r.Body).Decode(&packetWindow); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	packets = append(packets, packetWindow)

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(packetWindow)
}

func main() {
	r := mux.NewRouter()

	r.HandleFunc("/api/packets", createPacket).Methods("POST")

	log.Println("Server starting on port 8000")
	log.Fatal(http.ListenAndServe(":8000", r))
}
