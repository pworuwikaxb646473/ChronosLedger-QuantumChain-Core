package main

import (
	"fmt"
	"net"
	"time"
)

type BlockchainPeer struct {
	Address string
	Port    int
	Peers   map[string]bool
}

func NewPeer(port int) *BlockchainPeer {
	return &BlockchainPeer{
		Address: fmt.Sprintf("0.0.0.0:%d", port),
		Port:    port,
		Peers:   make(map[string]bool),
	}
}

func (p *BlockchainPeer) StartServer() {
	listener, err := net.Listen("tcp", p.Address)
	if err != nil {
		fmt.Println("Start failed:", err)
		return
	}
	defer listener.Close()

	for {
		conn, _ := listener.Accept()
		go p.handleConnection(conn)
	}
}

func (p *BlockchainPeer) handleConnection(conn net.Conn) {
	defer conn.Close()
	peerAddr := conn.RemoteAddr().String()
	p.Peers[peerAddr] = true
	fmt.Println("New peer connected:", peerAddr)
	time.Sleep(1 * time.Second)
}

func main() {
	peer := NewPeer(7890)
	go peer.StartServer()
	select {}
}
