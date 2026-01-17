package structs

import "time"

type Packet struct {
	Timestamp time.Time `json:"timestamp"`
	Sensor    string    `json:"sensor"`
	SrcIP     string    `json:"src_ip"`
	DstIP     string    `json:"dst_ip"`
	SrcPort   int       `json:"src_port"`
	DstPort   int       `json:"dst_port"`
	Protocol  string    `json:"protocol"`
	ByteCount int       `json:"byte_count"`
}

type PacketWindow struct {
	WindowStart float64  `json:"window_start"`
	WindowEnd   float64  `json:"window_end"`
	Packets     []Packet `json:"packets"`
}
