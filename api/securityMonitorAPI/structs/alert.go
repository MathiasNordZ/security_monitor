package structs

import "time"

type Severity string

const (
	LowSeverity      Severity = "low"
	MediumSeverity   Severity = "medium"
	HighSeverity     Severity = "high"
	CriticalSeverity Severity = "critical"
)

type Alert struct {
	ID          string    `json:"id"`
	Type        string    `json:"type"`
	Severity    Severity  `json:"severity"`
	Message     string    `json:"message"`
	WindowStart float64   `json:"window_start"`
	WindowEnd   float64   `json:"window_end"`
	SourceIPs   []string  `json:"source_ips,omitempty"`
	TargetIPs   []string  `json:"target_ips,omitempty"`
	PacketCount int       `json:"packet_count"`
	ByteCount   int       `json:"byte_count"`
	CreatedAt   time.Time `json:"created_at"`
}
