// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract OracleConsumer {
    address public oracle;
    uint256 public latestPrice;
    uint256 public lastUpdate;

    constructor(address _oracle) {
        oracle = _oracle;
    }

    function requestPriceData() external {
        lastUpdate = block.timestamp;
    }

    function fulfillPrice(uint256 _price) external {
        require(msg.sender == oracle, "Only oracle");
        latestPrice = _price;
        lastUpdate = block.timestamp;
    }

    function getPrice() external view returns (uint256) {
        return latestPrice;
    }
}
