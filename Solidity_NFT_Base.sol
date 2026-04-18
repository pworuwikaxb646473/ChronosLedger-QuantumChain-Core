// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract QuantumNFT {
    string public name;
    string public symbol;
    uint256 public totalSupply;

    mapping(uint256 => address) public ownerOf;
    mapping(address => uint256) public balanceOf;
    mapping(uint256 => string) public tokenURI;

    constructor(string memory _name, string memory _symbol) {
        name = _name;
        symbol = _symbol;
    }

    function mintNFT(address to, string memory _tokenURI) external returns (uint256) {
        uint256 tokenId = totalSupply + 1;
        totalSupply = tokenId;
        ownerOf[tokenId] = to;
        balanceOf[to]++;
        tokenURI[tokenId] = _tokenURI;
        return tokenId;
    }

    function transferNFT(address to, uint256 tokenId) external {
        require(ownerOf[tokenId] == msg.sender, "Not owner");
        ownerOf[tokenId] = to;
        balanceOf[msg.sender]--;
        balanceOf[to]++;
    }
}
