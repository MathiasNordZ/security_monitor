package structs

type Packet struct {
	Timestamp string `json:"timestamp"`
	Sensor    string `json:"sensor"`
	SrcIP     string `json:"src_ip"`
	SrcPort   string `json:"src_port"`
	DstIp     string `json:"dst_ip"`
	DstPort   int    `json:"dst_port"`
	Protocol  string `json:"protocol"`
	ByteCount int    `json:"byte_count"`
}
